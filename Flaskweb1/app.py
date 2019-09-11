from flask import Flask,render_template

app =Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/services')
def services():
    return render_template('services.html')


#
#
@app.route('/Members')
def Members():
     return render_template('Members.html')



#create a route about us

@app.route('/about_us')
def about_us():
    return render_template('about_us.html')



@app.route('/register')
def register():
    return render_template('register.html')



if __name__ =='__main__':
    app.debug = True
    app.run()
    app.run(debug=True)
