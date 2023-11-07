from flask import (Flask, config, render_template, request, flash, json, send_file, session, jsonify, redirect, url_for)
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'mydb'
mysql = MySQL(app)

@app.route('/')
def main():
    link = mysql.connection.cursor() 
    link.execute("SELECT * FROM tbestudiantes") 
    data = link.fetchall()
    return render_template('index.html', estudiantes=data)

@app.route('/addestudiantes', methods=['POST', 'GET'])
def addestudiantes(): 
    if request.method == 'POST': 
        id = request.form['id'] 
        nombre = request.form['nombre'] 
        apellido = request.form['apellido'] 
        edad = request.form['edad'] 
        carrera = request.form['carrera']
        link = mysql.connection.cursor() 
        link.execute('INSERT INTO tbestudiantes(id, nombre, apellido, edad, carrera) VALUES(%s,%s,%s,%s,%s)',
                     (id, nombre, apellido, edad, carrera)) 
        mysql.connection.commit() 
        link.close() 
        flash("Estudiante registrado correctamente") 
    return redirect(url_for('main'))
    
@app.route('/viewestudiantes', methods=['POST','GET']) 
def viewestudiantes(): 
    if request.method == 'POST': 
        estudiantesId = request.form['id'] 
        link = mysql.connection.cursor() 
        link.execute("SELECT * FROM tbestudiantes WHERE id=%s", [estudiantesId]) 
        data = link.fetchall() 
    return jsonify({'htmlresponse': render_template('viewestudiantes.html', estudiantes=data)})

@app.route('/updateestudiantes', methods=['GET', 'POST'])
def updateestudiantes():
    if request.method == 'POST':
        estudiantesId = request.form.get('id') 
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        edad = request.form['edad']
        carrera = request.form['carrera']
        link = mysql.connection.cursor()
        link.execute("UPDATE tbestudiantes SET nombre=%s, apellido=%s, edad=%s, carrera=%s WHERE id=%s", (nombre, apellido, edad, carrera, estudiantesId))
        mysql.connection.commit()
        link.close()
        flash("Estudiante actualizado correctamente")
        return redirect(url_for('main'))

@app.route('/deleteestudiantes/<string:estudiantesId>', methods=['POST', 'GET'])
def deleteestudiantes(estudiantesId): 
    if request.method == 'GET': 
        link = mysql.connection.cursor() 
        sql = "DELETE FROM tbestudiantes WHERE id=%s" 
        estudiantesId = (estudiantesId, )
        link.execute(sql, estudiantesId) 
        mysql.connection.commit() 
        link.close() 
        flash("Estudiante eliminado correctamente") 
        return redirect(url_for('main'))


#Lo relacionado a las tabla libros:
@app.route('/libros')
def libros():
    link = mysql.connection.cursor() 
    link.execute("SELECT * FROM tblibros") 
    data = link.fetchall()
    return render_template('libros.html', libros=data)

@app.route('/viewlibros', methods=['POST','GET']) 
def viewlibros(): 
    if request.method == 'POST': 
        idLibro = request.form['idLibro'] 
        link = mysql.connection.cursor() 
        link.execute("SELECT * FROM tblibros WHERE idLibro=%s", [idLibro]) 
        data = link.fetchall() 
    return jsonify({'htmlresponse': render_template('viewlibros.html', libros=data)})

@app.route('/addlibros', methods=['POST', 'GET'])
def addlibros(): 
    if request.method == 'POST': 
        idLibro = request.form['idLibro'] 
        titulo = request.form['titulo'] 
        cantidad = request.form['cantidad'] 
        autor = request.form['autor'] 
        anio = request.form['anio'] 
        link = mysql.connection.cursor() 
        link.execute('INSERT INTO tblibros(idLibro, titulo, cantidad, autor, anio) VALUES(%s,%s,%s,%s,%s)',
                     (idLibro, titulo, cantidad, autor, anio)) 
        mysql.connection.commit() 
        link.close() 
        flash("Libro registrado correctamente") 
    return redirect(url_for('libros'))

@app.route('/updatelibros', methods=['GET', 'POST'])
def updatelibros():
    if request.method == 'POST':
        librosId = request.form.get('idLibro') 
        titulo = request.form['titulo']
        cantidad = request.form['cantidad']
        autor = request.form['autor']
        anio = request.form['anio']
        link = mysql.connection.cursor()
        link.execute("UPDATE tblibros SET titulo=%s, cantidad=%s, autor=%s, anio=%s WHERE idLibro=%s", (titulo, cantidad, autor, anio, librosId))
        mysql.connection.commit()
        link.close()
        flash("Libro actualizado correctamente")
        return redirect(url_for('libros'))
@app.route('/deletelibros/<string:librosId>', methods=['POST', 'GET'])
def deletelibros(librosId): 
    if request.method == 'GET': 
        link = mysql.connection.cursor() 
        sql = "DELETE FROM tblibros WHERE id=%s" 
        librosId = (librosId, )
        link.execute(sql, librosId) 
        mysql.connection.commit() 
        link.close() 
        flash("Libro eliminado correctamente") 
        return redirect(url_for('libros'))

if __name__=='__main__':
    app.secret_key = "crudpythonmysql"
    app.run(debug=True, host='0.0.0.0', port=5000, threaded=True)