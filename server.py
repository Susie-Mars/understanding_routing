from flask import Flask  
app = Flask(__name__)    

# RETURN HELLO WORLD
@app.route('/')
def hello_world():
    return 'Hello World!'

# RETURN DOJO
@app.route('/dojo')
def dojo():
    return 'Dojo'

# RETURN HELLO "NAME"
@app.route('/say/<name>')
def say(name):
    print(name)
    return "Hello," + name

# RETURN REPEATING WORDS
@app.route('/repeat/<int:number>/<word>')
def mult(number, word):
    print(f"Multiplying {word} by {number}")
    return word * number



if __name__=="__main__":
    app.run(debug=True)

