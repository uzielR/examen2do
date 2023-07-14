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
    CC.execute('SELECT * FROM tbflores')
    condb_floreria= CC.fetchall() 
    print (condb_floreria)
    return render_template('index.html', Listaflor=condb_floreria)

@app.route('/guardar',methods=['POST'])
def guardar():
    if request.method == 'POST': 
        nombre=request.form['txtnombre']
        cantidad=request.form['txtcantidad']
        precio=request.form['txtprecio']
        print(nombre, cantidad, precio)

        #conectar a la bd
        CS = mysql.connection.cursor()
        CS.execute('INSERT INTO tbflores (nombre, cantidad, precio) VALUES (%s, %s, %s)', (nombre, cantidad, precio))

        mysql.connection.commit()
    
    flash('la flor fue agregado correctamente')
    return redirect(url_for('index'))

@app.route('/actualizar/<id>',methods=['POST'])
def eactualizar(id):

    if request.method == 'POST':
       varnombre = request.form ['txtnombre']
       varcantidad= request.form ['txtcantidad']
       varprecio = request.form ['txtprecio']

       cursorAct=mysql.connection.cursor()
       cursorAct.execute('update DB_floreria set nombre= %s, cantidad= %s, precio= %s where id = %s', (varnombre,varcantidad,varprecio,id))
       mysql.connection.commit()
    
    flash('Se actualizo el flor'+varnombre)
    return redirect(url_for('index'))


#ejecucion del servidor en el puerto 5000
if __name__ == '__main__':
  app.run(port=5000,debug=True)