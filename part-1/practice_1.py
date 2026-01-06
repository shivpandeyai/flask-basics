# Exercise 1.1: Change the return message

from flask import Flask

app = Flask(__name__)

@app.route('/')

def home():
    return "Hello, my Name is Shiv Pandey"

#if __name__== '__main__':

    #app.run(debug=True)

#Exercise 1.2: Return HTML instead of plain text

#def home():
    #return "<h1> Hello , This is Shiv on HTML </h1> <p> Cheacking HTML web Page </p>"

#if __name__== '__main__':

    #app.run(debug=True)

# Exercise 1.3: Add a second route

@app.route('/about')

def about():
    return "<h1> This is Aboutttt Page</h1>"

if __name__== '__main__':

    app.run(debug=True)


