#importato la librerias
from flask import Flask,request,url_for,flash,redirect
from flask import render_template
from flask_mysqldb import MySQL
#configurar de la app
app = Flask(__name__)
app.config["MYSQL_HOST"]="localhost"
app.config["MYSQL_USER"]="root"
app.config["MYSQL_PASSWORD"]=""
app.config["MYSQL_DB"]="contactos"
mysql=MySQL(app)
app.secret_key='mysecretKey'
#abro el  metodo  POST y hace la url                    
@app.route('/',methods=['GET','POST'])
def login():
    error = None
    if request.method =="POST":
        if request.form['usuario'] != 'admin' or request.form['password'] != 'admin':
            error = 'ESTA ALGO MAL'
        else:
            return redirect(url_for('Index'))    
    return render_template('login.html',error=error)
@app.route("/index")
def Index():
    cur=mysql.connection.cursor()
    #comando que nos permite mostar el contenido es decir los datos 
    cur.execute('SELECT * FROM mycontactos')
    datos=cur.fetchall()
    return render_template('index.html',contactos = datos)

@app.route("/update",methods=["GET","POST"])
def anadirContacto():
    if request.method == 'POST':
        detalles = request.form
        nombres = detalles['nombre']
        numero = detalles['numero']
        email = detalles['email']
        cur= mysql.connection.cursor()
        cur.execute("INSERT INTO mycontactos (NOMBRE,NUMERO,EMAIL )VALUES(%s,%s,%s)",(nombres,numero,email))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('Index'))
    return render_template("upda.html") 

@app.route("/editar/<id>")
def editar(id):
    cur=mysql.connection.cursor()
    cur.execute('SELECT * FROM mycontactos WHERE id = %s',(id))
    dato= cur.fetchall()
    return render_template('upda.html',contacto= dato[0])
@app.route('/actualizar/<id>', methods= ['POST'])
def actualizar(id):
    if request.method == 'POST':
        nombre=request.form['nombre']
        numero=request.form['numero']
        email=request.form['email']
        cur=mysql.connection.cursor()
        #comando de mysql que permite actualizar los datos 
        cur.execute("""
            UPDATE mycontactos
            SET nombre =%s,
                email=%s,
                numero=%s
            WHERE id=%s
        """,(nombre, email,numero,id))
        mysql.connection.commit()
        #direcciona a la pagina principal 
        return redirect(url_for('Index'))

@app.route("/eliminar/<string:id>")
def eliminar(id):
    cur= mysql.connection.cursor()
    cur.execute('DELETE FROM mycontactos WHERE id = {0}'.format(id))
    mysql.connection.commit()
    #direcciona a la pagina principal 
    return redirect(url_for('Index'))

if __name__=="__main__":
    app.run(port=1406,debug=True)

