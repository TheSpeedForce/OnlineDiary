
# A very simple Bottle Hello World app for you to get started with...
from bottle import default_app, route, template, post

#other imports
import sqlite3

#set up db connection
diaryDB = sqlite3.connect("./mysite/diary.db")
diaryC = diaryDB.cursor()

@route('/')
def first():
    return template("./first.html")

@route('/bmi')
def start():
    return template("./start.html")

@post('/calculate')
def calculate():
    return template("./result.html")

@route('/test')
def test():
    return template("./test.html")

@route('/diary')
def project():
    return template("./mysite/project/start.html")

@route('/diary/signup')
def signup():
    return template("./mysite/project/signup.html")

@post('/diary/signupB')
def signupB():
    return template('./mysite/project/signupB.html' , c = diaryC, db = diaryDB)

@post('/diary/check')
def check():
    return template('./mysite/project/check.html', c = diaryC)

@post('/diary/login')
def login():
    return template('./mysite/project/login.html', c = diaryC)

@post('/diary/login/read')
def read():
    return template('./mysite/project/read.html', c = diaryC)

@post('/diary/login/readB')
def readB():
    return template('./mysite/project/readB.html', c = diaryC)

@post('/diary/login/write')
def write():
    return template('./mysite/project/write.html', c = diaryC)

@post('/diary/login/writeB')
def writeB():
    return template('./mysite/project/writeB.html', c = diaryC, db = diaryDB)

@post('/diary/login/delete')
def delete():
    return template('./mysite/project/delete.html', c = diaryC)

@post('/diary/login/deleteB')
def deleteB():
    return template('./mysite/project/deleteB.html', c = diaryC, db = diaryDB)

@post('/diary/login/deleteC')
def deleteC():
    return template('./mysite/project/deleteC.html', c = diaryC, db = diaryDB)

@route('/diary/recover')
def recover():
    return template('./mysite/project/recover.html')

@post('/diary/recoverB')
def recoverB():
    return template('./mysite/project/recoverB.html', c = diaryC)

@post('/diary/recoverC')
def recoverC():
    return template('./mysite/project/recoverC.html', c = diaryC)

application = default_app()
