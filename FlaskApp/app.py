from flask import Flask
app = Flask(__name__)

# routes
@app.route('/login')
def login():
    return 'Welcome to login'


@app.route('/join')
def join():
    return 'Welcome to Join page'


@app.route('/withdraw')
def withdraw():
    return 'Welcome to withdraw'


@app.route('/taking_loans')
def taking_loans():
    return 'Welcome to taking loans'


@app.route('/Hello_Malindi')
def Hello_Malindi():
    return 'Hello Malindi'

if __name__ == '__main__':
   app.run()