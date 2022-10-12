from datetime import date, datetime
from urllib import request
from flask import Flask, render_template, request

app = Flask(__name__)
global studentOrganisationDetails
studentOrganisationDetails = dict()
# Assign default 5 values to studentOrganisationDetails for Application  3.



@app.get('/')
def index():
    # Complete this function to get current date and time assign this value to currentDate, display this data on index.html
    return render_template('index.html', current_datetime=datetime.utcnow())


@app.get('/calculate')
def displayNumberPage():
    # Complete this function to display form.html page
    return render_template('form.html')


@app.route('/calculate', methods=['POST'])
def checkNumber():
    # Get Number from form and display message according to number
    # Display "Number {Number} is even" if given number is even on result.html page
    # Display "Number {Number} is odd" if given number is odd on result.html page
    # Display "No number provided" if value is null or blank on result.html page
    # Display "Provided input is not an integer!" if value is not a number on result.html page
    global number
    number = request.form['number']
    if not number:
        return render_template('result.html')
    try: 
        number = int(number)
    except ValueError:
        return render_template('result.html', invalid = True)
    even = number % 2 == 0
    return render_template('result.html', even=even, number=number)
        
    # Write your to code here to check whether number is even or odd and render result.html page


@app.get('/addStudentOrganisation')
def displayStudentForm():
    # Complete this function to display studentFrom.html page
    return render_template('studentForm.html')


@app.route('/addStudentOrganisation', methods=['POST'])
def displayRegistrationPage():
    # Get student name and organisation from form.
    studentName = request.form['name']
    org = request.form['org']
    studentOrganisationDetails[studentName] = org
    # Append this value to studentOrganisationDetails

    # Display studentDetails.html with all students and organisations
    return render_template('studentDetails.html', studentOrganisationDetails=studentOrganisationDetails)
