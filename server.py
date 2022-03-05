from ast import Num
from turtle import color
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def board():
    return render_template('index.html', num=8, w=8)

@app.route('/<int:num>')
def heighth(num):
    return render_template('index.html', num=num, w=8)

@app.route('/<int:num>/<int:w>')
def height_width(num, w):
    return render_template('index.html', num=num, w=w)

@app.route('/<int:num>/<int:w>/<string:color>')
def color1(num, w, color):
    return render_template('index.html', num=num, w=w, color=color)

@app.route('/<int:num>/<int:w>/<string:color>/<string:difcolor>')
def colors(num, w, color, difcolor):
    return render_template('index.html', num=num, w=w, color=color, difcolor=difcolor)

if __name__=="__main__":
    app.run(debug=True)