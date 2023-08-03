from app import app

@app.route("/")
def homepage():
    return "<p>Hello, World!</p>"

# @app.route("/login", methods=["POST"])
# def login():
#     return 'login'

# @app.route("/logout", methods=['POST'])
# def logout():
#     return 'logout'

# @app.route('/register', methods=["POST"])
# def register():
#     return 'register'