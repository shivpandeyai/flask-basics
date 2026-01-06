#global code for practice_2

from flask import Flask, render_template

app= Flask(__name__)

#Exercise 2.1: Modify the templates

#@app.route('/')
#def home():
    #return render_template('index.html')
#@app.route('/about')
#def about():
    #return render_template('about.html')

#if __name__ == '__main__':
    #app.run(debug=True)



#Exercise 2.2: Create a new contact page 

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)

