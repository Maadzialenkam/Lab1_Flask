from flask import Flask # importujemy bibliotekę Flask, za pomocą której utworzymy naszą pierwszą aplikację app = Flask(__name__)
from flask import request # umożliwia dostęp do żądania otrzymanego przez serwer
from flask import  render_template # pozwala wykorzystywać szablony w plikach HTML
from flask import abort, redirect, url_for, make_response # są użytecznymi modułami do obsługi błędów, przekierowania oraz modyfikowania nagłówka odpowiedzi HTTP
                    

app = Flask(__name__)
                    # tworzymy samą aplikację

#HOME
@app.route('/')
def home():
    return render_template('index.html')
                    # informuje Flask, że poniżej znajduje się funkcja która odpowiada za wyświetlenie treści w przeglądarce pod adresem '/'czyli przykładowo http://localhost:5000/. Jest to nasza strona główna.


#@app.route("/help")
#def help():
   # return "help me"
                    # wyświetlanie podstrony Help

# CONTACT
@app.route("/contact")
def contact():
    return render_template('contact.html')
                    # wyświetlanie podstrony Contact

# GALLERY
@app.route("/gallery")
def gallery():
    return render_template('gallery.html')

# ABOUT ME
@app.route("/aboutme")
def aboutme():
    return render_template('aboutme.html')

# OBSŁUGA ŻĄDAŃ HTTP

@app.route('/user/<username>', methods=['GET', 'POST'])
def show_user_profile(username):
    if request.method == 'POST':
        return 'HTTP POST for user %s with password %s' % (username, request.form['password'])
    else:
        return 'HTTP GET for user %s' % username

"""
# LOGOWANIE - PRACA Z FORMULARZAMI

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        return request.form["username"] + " + " + request.form["password"]
    else:
        return render_template('login.html')
"""
if(__name__)=='__main__':
    app.run(host='0.0.0.0')
                    # uruchamiamy aplikację