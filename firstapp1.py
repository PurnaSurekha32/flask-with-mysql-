from flask import Flask,redirect,url_for,render_template,jsonify,request
from flaskext.mysql import MySQL
app=Flask(__name__)
app.config['MYSQL_DATABASE_HOST']='localhost'
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']='1999'
app.config['MYSQL_DATABASE_DB']='student'
mysql=MySQL(app)
@app.route('/home')
def home():
    return render_template('index.html')
@app.route('/allinfo',methods=['GET'])
def info():
    cursor=mysql.get_db().cursor()
    cursor.execute('select * from student')
    data=cursor.fetchall()
    cursor.close()
    return jsonify(data)
@app.route('/addstudent',methods=['GET','POST'])
def add():
    if request.method=='POST':
        id1=request.form['id']
        name=request.form['name']
        dept=request.form['dept']
        cursor=mysql.get_db().cursor()
        cursor.execute('insert into student(id,name,dept) values(%s,%s,%s)',[id1,name,dept])
        mysql.get_db().commit()
        cursor.close()
        return redirect(url_for('home'))
    return render_template('add.html')
@app.route('/update',methods=['GET','POST'])
def update():
    if request.method=='POST':
        id1=request.form['id']
        name=request.form['name']
        dept=request.form['dept']
        cursor=mysql.get_db().cursor()
        cursor.execute('update student set name=%s,dept=%s where id=%s',[name,dept,id1])
        mysql.get_db().commit()
        cursor.close()
        return redirect(url_for('home'))
    return render_template('update.html')
@app.route('/delete',methods=['GET','POST'])
def delete():
    if request.method=='POST':
        id1=request.form['id']
        cursor=mysql.get_db().cursor()
        cursor.execute('delete from student where id=%s',[id1])
        mysql.get_db().commit()
        cursor.close()
        return redirect(url_for('home'))
    return render_template('delete.html')
app.run(use_reloader=True)


