from flask import Flask,render_template
app=Flask(__name__)

@app.route('/')
def test():
    return "goodbye world"

@app.route('/play')
def play():
    return render_template('playground.html',num=3,color='lightblue')

@app.route('/play/<int:num>')
def seven(num):
    return render_template('playground.html',num=num, color='lightblue')

@app.route('/play/<int:num>/color')
def color(num,color):
    return render_template('playground.html',num=num,color=color)


if __name__=='__main__':
    app.run(debug=True,port=8000)

