from flask import Flask


app = Flask(__name__)


from routes import *
# http://127.0.0.1:5000/city?q=washington

if __name__ == '__main__':
    app.run(debug=True)
