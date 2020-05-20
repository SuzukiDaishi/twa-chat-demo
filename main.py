from flask import Flask

app = Flask(__name__)

@app.route('/')
def home() :
    html = '<h1>Hello World</h1>'
    return html


if __name__ == "__main__":
    app.run(debug=True)