from flask import Flask

from flask_ngrok import run_with_ngrok

app = Flask(__name__)

def ngrok_callback(ngrok_address):
    print("Doing something with the %s" % ngrok_address)

run_with_ngrok(app, ngrok_callback)  # Start ngrok when app is run


@app.route("/")
def hello():
    return "Hello World!"


if __name__ == '__main__':
    app.run()
