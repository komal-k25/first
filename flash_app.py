from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "hello world"

@app.route('/sit1')
def sit():
    return "SIT rocks!"    


@app.route('/sheela')
def sheela():
    return f"sheela ki jawani umar {stored_age}"

@app.route('/sheela/<age>')
def sheela_age(age):
    return f"sheela ki umar {age}"

@app.route('/sheela/<cage>', methods=['POST'])
def sheela_post(age):
    global stored_age
    stored_age = age
    return "done"

app.run()