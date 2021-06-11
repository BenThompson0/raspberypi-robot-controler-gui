from flask import Flask
from flask import render_template

# Importing in drive.py from robot folder
from robot import drive

X = 0
Y = 0

app = Flask(__name__)

# Will show main web page file
@app.route('/')
def hello():
    return render_template('main.html')

'''
def X():
    if X > 5:
        print("Good")
    elif X < -5:
        print("Bad")

def X():
    if Y > 5:
        print("Good")
    elif Y < -5:
        print("Bad")
'''

# Move robot FORWORD
@app.route('/api/forword', methods=['GET', 'POST'])
def forword():
    return drive.forword()

# Move robot BACKWORDS
@app.route('/api/backwords', methods=['GET', 'POST'])
def backwords():
    #drive.backwords()
    return()

# Move robot LEFT
@app.route('/api/left', methods=['GET', 'POST'])
def left():
    #drive.left()
    return()

# Move robot RIGHT
@app.route('/api/right', methods=['GET', 'POST'])
def right():
    #drive.right()
    return()


# Move robot UP
@app.route('/api/up', methods=['GET', 'POST'])
def up():
    drive.up()
    return()

# Move robot DOWN
@app.route('/api/down', methods=['GET', 'POST'])
def down():
    #drive.down()
    return()

# Robot Opening/closing
@app.route('/api/openclose', methods=['GET', 'POST'])
def openclose():
    #drive.open_close()
    return()

# Make robot SHOOT
@app.route('/api/shoot', methods=['GET', 'POST'])
def shoot():
    #drive.shoot()
    return()
