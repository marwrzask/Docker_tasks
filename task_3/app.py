from flask import Flask, render_template
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis', port=6379)


@app.route('/')
def hello():
    str =  f"To add new user type url address in the following manner: 'http://127.0.0.1:5000/set/your_name/your_surname' " \
           f"<br/> To get information about the user type url address in the following manner: 'http://127.0.0.1:5000/get/your_name'"
    return str

@app.route('/set/<name>/<surname>')
def write(name, surname):
    redis.set(name, surname)
    str = f'New account informations: <br/>name: {name} <br/> surname: {surname}'
    return str

@app.route('/get/<name>')
def read(name):
    user = redis.get(name)
    return f"User surname: {user.decode()}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)