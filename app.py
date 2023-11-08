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
        estudiantesId = request.form['id'] 
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

#Sobre libros
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

@app.route('/updatelibros', methods=['POST'])
def updatelibros():
    if request.method == 'POST':
        libroId = request.form.get('idLibro')
        titulo = request.form['titulo']
        cantidad = request.form['cantidad']
        autor = request.form['autor']
        anio = request.form['anio']
        link = mysql.connection.cursor()
        link.execute("UPDATE tblibros SET titulo=%s, cantidad=%s, autor=%s, anio=%s WHERE idLibro=%s", (titulo, cantidad, autor, anio, libroId))
        mysql.connection.commit()
        link.close()
        flash("Libro actualizado correctamente")
        return redirect(url_for('libros'))
@app.route('/deletelibros/<string:idLibro>', methods=['POST', 'GET'])
def deletelibros(idLibro): 
    if request.method == 'GET': 
        link = mysql.connection.cursor() 
        sql = "DELETE FROM tblibros WHERE idLibro=%s" 
        idLibros = (idLibro, )
        link.execute(sql, idLibros) 
        mysql.connection.commit() 
        link.close() 
        flash("Libro eliminado correctamente") 
        return redirect(url_for('libros'))

#Sobre prestamos
#Lo relacionado a las tabla prestamos:
@app.route('/prestamos')
def prestamos():
    link = mysql.connection.cursor() 
    link.execute("SELECT * FROM prestamos") 
    data = link.fetchall()
    return render_template('prestamos.html', prestamos=data)

@app.route('/viewprestamos', methods=['POST','GET']) 
def viewprestamos(): 
    if request.method == 'POST': 
        idprestamo = request.form.get('idprestamo')
        link = mysql.connection.cursor() 
        link.execute("SELECT * FROM prestamos WHERE idprestamo=%s", [idprestamo]) 
        data = link.fetchall() 
    return jsonify({'htmlresponse': render_template('viewprestamos.html', prestamos=data)})

@app.route('/addprestamos', methods=['POST', 'GET'])
def addprestamos():
    if request.method == 'POST':
        idprestamo = request.form['idprestamo']
        idestudiante = request.form['id']
        idlibro = request.form['idlibro']
        fechaprestamo = request.form['fechaprestamo']
        fechadevolucion = request.form['fechadevolucion']
        estado = request.form['estadoprestamo']

        # Actualiza la cantidad de libros disponibles
        link = mysql.connection.cursor()
        link.execute("SELECT cantidad FROM tblibros WHERE idlibro = %s", [idlibro])
        cantidad = link.fetchone()[0]
        
        if cantidad> 0:
            # Resta 1 a la cantidad disponible
            cantidad -= 1
            
            # Actualiza la cantidad disponible en la tabla de libros
            link.execute("UPDATE tblibros SET cantidad = %s WHERE idlibro = %s", (cantidad, idlibro))
            
            # Registra el préstamo en la tabla prestamos
            link.execute('INSERT INTO prestamos(idprestamo, id, idlibro, fechaprestamo, fechadevolucion, estadoprestamo) VALUES(%s,%s,%s,%s,%s,%s)',
                         (idprestamo, idestudiante, idlibro, fechaprestamo, fechadevolucion, estado))
            
            mysql.connection.commit()
            link.close()
            flash("préstamo registrado correctamente")
        else:
            flash("No hay libros disponibles con el ID especificado")
    
    return redirect(url_for('prestamos'))


@app.route('/updateprestamos', methods=['POST'])
def updateprestamos():
    if request.method == 'POST':
        prestamoId = request.form.get('idprestamo')
        id = request.form['id'] 
        idlibro = request.form['idlibro'] 
        fechaprestamo = request.form['fechaprestamo'] 
        fechadevolucion = request.form['fechadevolucion'] 
        estado = request.form['estadoprestamo'] 
        link = mysql.connection.cursor()
        link.execute("UPDATE prestamos SET id=%s, idlibro=%s, fechaprestamo=%s, fechadevolucion=%s, estadoPrestamo=%s WHERE idprestamo=%s", (id, idlibro, fechaprestamo, fechadevolucion, estado, prestamoId))
        mysql.connection.commit()
        link.close()
        flash("prestamo actualizado correctamente")
        return redirect(url_for('prestamos'))
    
@app.route('/deleteprestamos/<string:idprestamo>', methods=['POST', 'GET'])
def deleteprestamos(idprestamo): 
    if request.method == 'GET': 
        link = mysql.connection.cursor() 
        sql = "DELETE FROM prestamos WHERE idprestamo=%s" 
        idprestamos = (idprestamo, )
        link.execute(sql, idprestamos) 
        mysql.connection.commit() 
        link.close() 
        flash("prestamo eliminado correctamente") 
        return redirect(url_for('prestamos'))

if __name__=='__main__':
    app.secret_key = "crudpythonmysql"
    app.run(debug=True, host='0.0.0.0', port=5000, threaded=True)