from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/admin')
def admin():
    return "<p>this is admin</p>"

@app.route('/<name>')
def Learn(name):
    return f"<p>Welcome {name} to the Flask Web App!</p>"

if __name__ == '__main__':
    app.run(debug=True)
