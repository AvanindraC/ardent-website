from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('tabbed.html')

@app.route("/login")
def login():
    pass


if __name__ == '__main__':
    app.run(debug=True, use_reloader=False, host='0.0.0.0', port=5000)
