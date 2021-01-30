from flask import Flask

app = Flask(__name__)


@app.route('/')
def main():
    """Doc string."""
    return b'Hello World!'
