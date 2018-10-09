from flask import Flask, url_for, render_template

app = Flask(__name__)



@app.route('/')
def profile():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=False, use_reloader=True)        


