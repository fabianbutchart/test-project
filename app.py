from flask import Flask, redirect, render_template, request
#need to remember to add styling here

app = Flask(__name__)
tasks = []

@app.route('/', methods=['GET', 'POST'])
def hello_world():  # put application's code here
    if request.method == 'POST':
        tasks.append(request.form['task'])
        return redirect('/')
    return render_template('index.html', list=tasks)

if __name__ == '__main__':
    app.run()
