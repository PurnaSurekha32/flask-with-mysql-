from flask import Flask,redirect,url_for,render_template,jsonify,request
app=Flask(__name__)
data=[]
@app.route('/home')
def home():
    return render_template('index.html')
@app.route('/allinfo',methods=['GET'])
def info():
    return jsonify(data)
@app.route('/addstudents',methods=['GET','POST'])
def add():
    if request.method=='POST':
        id1=request.form['id']
        name=request.form['name']
        dept=request.form['dept']
        data.append({'id':id1,'name':name,'dept':dept})
        return redirect(url_for('home'))
    return render_template('add.html')
@app.route('/update',methods=['GET','POST'])
def update():
    if request.method=='POST':
        id1=request.form['id']
        name=request.form['name']
        dept=request.form['dept']
        for i in data:
            if i['id']==id1:
                i['name']=name
                i['dept']=dept
        return redirect(url_for('home'))
    return render_template('update.html')
@app.route('/delete',methods=['GET','POST'])
def delete():
    if request.method=='POST':
        id1=request.form['id']
        for i in data:
            if i['id']==id1:
                data.remove(i)
        return redirect(url_for('home'))
    return render_template('delete.html')
app.run(use_reloader=True)
    
    
        
    
