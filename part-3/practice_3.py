
from flask import Flask, render_template
app = Flask(__name__)

# Exercise 3.1: Add more data
#   - Add more fields to the profile (email, city, etc.)
#   - Display them in profile.html

print("-----Practice 3.1: Adding more data to profile and display them in template.-----\n")

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
        'is_enrolled': False
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
@app.route('/skills')
def skills():
    programming_skills = ['Python', 'TensorFlow', 'Keras', 'Pandas', 'NumPy']
    return render_template('skills.html', skills=programming_skills)  # Pass list to loop through in template

@app.route('/projects') 
def projects():
    project_list = [  # List of dictionaries - common pattern for database-like data
        {'name': 'AI Chatbot', 'status': 'Completed', 'tech': 'Python/TensorFlow'},
        {'name': 'Image Classifier', 'status': 'In Progress', 'tech': 'Python/Keras'},
        {'name': 'Data Analysis Tool', 'status': 'Planned', 'tech': 'Python/Pandas'},
    ]
    return render_template('projects.html', project=project_list)

#Exercise 3.2: Conditional display
#   - In profile.html, show "Enrolled" or "Not Enrolled" based on is_enrolled
#   - Use {% if is_enrolled %} ... {% else %} ... {% endif %}

print("-----Practice 3.2: Conditional display based on enrollment status.-----\n")

#Exercise 3.3: Create a grades page
#   - Create a new route /grades
#   - Pass a dictionary of subjects and grades
#   - Display them in a table using a for loop


print("-----Practice 3.3: Creating grades page and displaying subjects with grades in a table.-----\n")
@app.route('/grades')
def grades():
    subjects_grades = {
        'Mathematics': 85,
        'Physics': 92,
        'Chemistry': 78,
        'Biology': 88
    }
    return render_template('grades.html', subjects_grades=subjects_grades)

if __name__ == '__main__':
    app.run(debug=True)
