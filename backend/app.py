from flask import Flask

app = Flask(__name__)

@app.route("/")
def homepage():
    return "<p>Hello, World!</p>"

@app.route("/login", methods=["POST"])
def login():
    return 'login'

@app.route("/logout", methods=['POST'])
def logout():
    return 'logout'

@app.route('/register', methods=["POST"])
def register():
    return 'register'

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8000)