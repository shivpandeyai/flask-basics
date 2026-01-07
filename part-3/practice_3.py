# Exercise 3.1: Add more data
#   - Add more fields to the profile (email, city, etc.)
#   - Display them in profile.html

from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def home():
    student_name = 'Shiv Pandey'
    location = 'New Delhi'
    return render_template(
        'index.html',
        name=student_name,
        location=location
    )

@app.route('/profile')
def profile():
    user_data = {
        'name': 'Shiv Pandey',
        'email': 'shivpandey.ai@gmail.com',
        'phone': 99999999,
        'city': 'New Delhi',
        'course': 'AI & Deep Learning',
        'is_enrolled': True
    }

    return render_template(
        'profile.html',
        name=user_data['name'],
        email=user_data['email'],
        phone=user_data['phone'],
        city=user_data['city'],
        course=user_data['course'],
        is_enrolled=user_data['is_enrolled']
    )

if __name__ == '__main__':
    app.run(debug=True)
