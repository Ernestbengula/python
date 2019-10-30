import pymysql as pymysql
from flask  import Flask
from flask import Flask, render_template,request, redirect, session

app = Flask(__name__)
@app.route('/login',methods=['GET', 'POST'])
def login():
       if request.method == 'POST':
           # we get inputs form from save them to our table
           EnterSurname = request.form['EnterSurname']
           EnterPassword = request.form['EnterPassword']

           if EnterSurname=="joe" and EnterPassword=="1234":
               return redirect('/codetest')

           else:
               return redirect('/login')


       else:
            return render_template('Login.html')



@app.route('/codetest',methods=['GET', 'POST'])
def codetest():
    return render_template('codetest.html')

if __name__ == '__main__':
    app.debug = True
    app.run(port=9000)
    app.run(debug=True)