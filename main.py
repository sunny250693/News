from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index_page():
    return render_template('index.html', title="Sunny's Site")

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
