from flask import Flask
#this will give access to the enviroment variables from Cloud 9
from os import environ

#create an instance of the class called app
app = Flask(__name__)
#This are the app.route methods that instruct where the following instructions will be run from
@app.route("/")
@app.route("/hello")
def say_hi():
    return "Hello World!"
    
@app.route("/hello/<name>")
def hello_person(name):
    html = """
        <h1>
            Hello {}!
        </h1>
        <p>
            Here's a picture of a kitten.  Awww...
        </p>
        <img src="http://beststuffformen.com/wp-content/uploads/2013/05/Reader-is-sexy.jpg">
    """
    return html.format(name.title())

@app.route("/jedi/<name>/<lastname>")
def hello_jedi(name,lastname):
    name=name[0:2]
    lastname=lastname[0:3]
    return "Jedi name is {}{}".format(lastname.title(),name)
    
if __name__ == "__main__":
    #app run method that uses host and port listening on cloud 9 anviroment
    app.run(host=environ['IP'],
            port=int(environ['PORT']))
