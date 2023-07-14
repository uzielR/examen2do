from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

#inicializacion del APP
app = Flask (__name__)
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='db_floreria'
app.secret_key = 'mysecretkey'
mysql = MySQL(app)

#declaracion de las rutas

#declaracion de la ruta al local host
@app.route('/')
def index():
    CC= mysql.connection.cursor()
    CC.execute('SELECT * FROM tbFlores')
     = CC.fetchall() 
    print ()
    return render_template('index.html', =)

@app.route('/guardar',methods=['POST'])
def guardar():
    if request.method == 'POST': 
        =request.form['txt']
        =request.form['txt']
        =request.form['txt']
        print(, , )

        #conectar a la bd
        CS = mysql.connection.cursor()
        CS.execute('INSERT INTO  (, , ) VALUES (%s, %s, %s)', ())

        mysql.connection.commit()
    
    flash('')
    return redirect(url_for('index'))

@app.route('/actualizar/<id>',methods=['POST'])
def eactualizar(id):

    if request.method == 'POST':
       var = request.form ['txt']
       var= request.form ['txt']
       var = request.form ['txt']

       cursorAct=mysql.connection.cursor()
       cursorAct.execute('update  set = %s, = %s, = %s where id = %s', ())
       mysql.connection.commit()
    
    flash(''+)
    return redirect(url_for('index'))


#ejecucion del servidor en el puerto 5000
if __name__ == '__main__':
  app.run(port=5000,debug=True)