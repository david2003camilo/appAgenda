from flask import Flask,request,url_for
from flask import render_template
from flask_mysqldb import MySQL
app = Flask(__name__)
app.config["MYSQL_HOST"]="localhost"
app.config["MYSQL_USER"]="root"
app.config["MYSQL_PASSWORD"]=""
app.config["MYSQL_DB"]="contactos"
mysql=MySQL(app)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/update",methods=["GET","POST"])
def actualizar():
    if request.method == 'POST':
        detalles = request.form
        nombres = detalles['nombres']
        numero = detalles['numero']
        email = detalles['email']
        cur= mysql.connection.cursor()
        cur.execute("INSERT INTO mycontactos (NOMBRE,NUMERO,EMAIL )VALUES(%s,%s,%s)",(nombres,numero,email))
        mysql.connection.commit()
        cur.close()
        return "AGREGADO"
    return render_template("upda.html") 


if __name__=="__main__":
    app.run(port=1406,debug=True)

