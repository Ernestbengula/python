import pymysql as pymysql
from flask import Flask, render_template,request, redirect, session

app = Flask(__name__)
app.secret_key = "234345^^^^^gggg$$$$777%%%%$$rffff5245"

@app.route('/')
def home():
    return render_template('Home.html')


import pymysql
@app.route('/join',methods = ['GET','POST'])
def join():
    # Application layer
    # SQL
    # check if the batton was click
    if request.method == 'POST':
        #we get inputs from from save them toour table
        email =request.form['email']
        surname = request.form['surname']
        password = request.form['password']
        residence = request.form['residence']
        career = request.form['career']
        phone = request.form['phone']


        connection = pymysql.connect("localhost","root","","auto_motors")
        cursor  = connection.cursor() # execute sql
        sql = '''INSERT INTO jointable (email, surname,password,residence,career,phone)VALUES (%s,%s,%s,%s,%s,%s);'''
        cursor.execute(sql,(email,surname,password,residence,career,phone))
        connection.commit()
        return render_template('join.html', msg="Saved Successfully")



    else:
        #user did not post anything ,we show the form
        return render_template('join.html')




#=====================

import pymysql
@app.route('/drivers',methods = ['GET','POST'])
def drivers():
    # Application layer
    # SQL
    # check if the batton was click
    if request.method == 'POST':
        #we get inputs from from save them toour table
       drivername=request.form['drivername']
       dl = request.form['dl']
       residence = request.form['residence']
       phone = request.form['phone']


       connection = pymysql.connect("localhost","root","","auto_motors")
       cursor  = connection.cursor() # execute sql
       sql = '''INSERT INTO drivers (drivername,dl,residence,phone)VALUES (%s,%s,%s,%s);'''
       cursor.execute(sql,(drivername,dl,residence,phone))
       connection.commit()
       return render_template('drivers.html', msg="Saved Successfully")



    else:
        #user did not post anything ,we show the form
        return render_template('drivers.html')


import pymysql

#=====================
@app.route('/Register', methods=['GET', 'POST'])
def Register():
    # Application layer
    # SQL
    # check if the batton was click
    if request.method == 'POST':
        # we get inputs from from save them toour table
        EnterSurname= request.form['EnterSurname']
        EnterPassword= request.form['EnterPassword']
        EnterAddress = request.form['EnterAddress' ]
        Career = request.form['Career']
        gender = request.form['gender']
        status = request.form['status']
        date = request.form['date']
        country = request.form['country']



        connection = pymysql.connect("localhost", "root","","TheDealsplace")
        cursor = connection.cursor()  # execute sql
        sql = '''INSERT INTO Register(EnterSurname,EnterPassword,EnterAddress,Career,gender,status,date,country)VALUES (%s,%s,%s,%s,%s,%s,%s,%s);'''
        cursor.execute(sql, (EnterSurname,EnterPassword,EnterAddress,Career,gender,status,date,country))
        connection.commit()
        return render_template('Register.html',msg="Saved Successfully")


    else:
        #user did not post anything ,we show the form
      return render_template('Register.html')



#=====================
@app.route("/searchdriver", methods =['GET','POST'])
def searchdriver():
    if request.method =='POST':# clicked
        dl = request.form['dl']  # receive DL from form

        conn = pymysql.connect("localhost", "root", "", "auto_motors")
        cursor = conn.cursor()
        sql = '''SELECT * FROM drivers WHERE dl = %s'''  # select all records
        cursor.execute(sql,(dl))  # run sql
        rows = cursor.fetchall()
        return render_template('searchdriver.html', msg=rows)
        # we now go and show  the rows in our HTML


    else:#Not clicked we show all
        conn = pymysql.connect("localhost","root","","auto_motors")
        cursor = conn.cursor()
        sql = '''SELECT * FROM drivers LIMIT 10''' # select all records
        cursor.execute(sql)# run sql
        rows = cursor.fetchall()
        return render_template('searchdriver.html',msg=rows)
        #we now go and show  the rows in our HTML

#==================

@app.route("/searchjoin", methods=['GET','POST'])
def searchjoin():
    if request.method == 'POST':  # clicked
        surname = request.form['surname ']  # receive surname from form

        conn = pymysql.connect("localhost", "root", "", "auto_motors")
        cursor = conn.cursor()
        sql = '''SELECT * FROM jointable WHERE surname  = %s'''  # select all records
        cursor.execute(sql, (surname ))  # run sql
        rows = cursor.fetchall()
        return render_template('searchjoin.html', msg=rows)
        # we now go and show  the rows in our HTML
    else:  # Not clicked we show all
        conn = pymysql.connect("localhost", "root", "", "auto_motors")
        cursor = conn.cursor()
        sql = '''SELECT * FROM jointable '''  # select all records
        cursor.execute(sql)  # run sql
        rows = cursor.fetchall()
        return render_template('searchjoin.html', msg=rows)
        # we now go and show  the rows in our HTML


#============

@app.route('/login',methods=['GET', 'POST'])
def login():
       if request.method == 'POST':
           # we get inputs form from save them to our table
           EnterSurname = request.form['EnterSurname']
           EnterPassword = request.form['EnterPassword']

           connection = pymysql.connect("localhost", "root","","TheDealsplace")
           cursor = connection.cursor()  # execute sql
           sql = '''SELECT * FROM `Register` WHERE `EnterSurname` = %s AND EnterPassword = %s '''
           cursor.execute(sql, (EnterSurname,EnterPassword ))
           rows = cursor.rowcount
           if rows==0:
               return render_template('login.html',msg="Login failed")

           else:
               session['surname'] = EnterSurname   # we set logged in username to a sessions
               return redirect('/Searchdeals')


       else:
            return render_template('login.html')





#==================

@app.route("/searchpersldetails", methods=['GET','POST'])
def searchpersldetails():
    if request.method == 'POST':  # clicked
        EnterSurname = request.form['EnterSurname ']  # receive surname from form

        conn = pymysql.connect("localhost", "root", "", "User_form")
        cursor = conn.cursor()
        sql = '''SELECT * FROM persldetails WHERE EnterSurname  = %s'''  # select all records
        cursor.execute(sql, (EnterSurname ))  # run sql
        rows = cursor.fetchall()
        return render_template('searchpersldetails.html', msg=rows)
        # we now go and show  the rows in our HTML
    else:  # Not clicked we show all
        conn = pymysql.connect("localhost", "root", "", "User_form")
        cursor = conn.cursor()
        sql = '''SELECT * FROM persldetails '''  # select all records
        cursor.execute(sql)  # run sql
        rows = cursor.fetchall()
        return render_template('searchpersldetails.html', msg=rows)
        # we now go and show  the rows in our HTML


import pymysql
@app.route('/Dealsplace', methods=['GET', 'POST'])
def Dealsplace():
        # Application layer
        # SQL
        # check if the batton was click
        if request.method == 'POST':
            # we get inputs from from save them toour table
            Type = request.form['Type']
            Model = request.form['Model']
            Make = request.form['Make']
            Pickpoint = request.form['Pickpoint']
            Droppoint = request.form['Droppoint']
            Transmission = request.form['Transmission']
            Miles = request.form['Miles']
            Fuel = request.form['Fuel']
            Cost = request.form['Cost']
            Color = request.form['Color']

            connection = pymysql.connect("localhost", "root", "", "TheDealsplace")
            cursor = connection.cursor()  # execute sql
            sql = '''INSERT INTO Dealsplace (Type, Model,Make,Pickpoint,Droppoint,Transmission,Fuel,Cost,Miles,Color)VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'''
            cursor.execute(sql, (Type,Model,Make,Pickpoint,Droppoint,Transmission,Fuel,Cost,Miles,Color))
            connection.commit()
            return render_template('Dealsplace.html', msg="Saved Successfully")



        else:
            # user did not post anything ,we show the form
            return render_template('Dealsplace.html')

    # =====================

#=====================
@app.route("/Searchdeals", methods =['GET','POST'])
def Searchdeals():
    if 'surname' in session:
        if request.method =='POST':# clicked
            car= request.form['car']  # receive DL from form

            conn = pymysql.connect("localhost", "root", "", "TheDealsplace")
            cursor = conn.cursor()
            sql = '''SELECT * FROM Dealsplace WHERE Make = %s'''  # select all records
            cursor.execute(sql,(car))  # run sql
            rows = cursor.fetchall()
            return render_template('Searchdeals.html', msg=rows)
            # we now go and show  the rows in our HTML


        else:#Not clicked we show all
            conn = pymysql.connect("localhost","root","","TheDealsplace")
            cursor = conn.cursor()
            sql = '''SELECT * FROM Dealsplace LIMIT 10''' # select all records
            cursor.execute(sql)# run sql
            rows = cursor.fetchall()
            return render_template('Searchdeals.html',msg=rows)
            #we now go and show  the rows in our HTML

    else:
        return redirect('/login')

@app.route('/logout')
def logout():
   # remove the username from the session if it is there
   session.pop('surname', None)
   return redirect('/login')




if __name__ == '__main__':
    app.debug = True
    app.run()
    app.run(debug=True)