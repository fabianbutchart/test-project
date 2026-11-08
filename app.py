import csv
import os

from flask import Flask, redirect, render_template, request
#need to remember to add styling here

app = Flask(__name__)
TASKS_FILE = 'tasks.csv'


def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, newline='', encoding='utf-8') as f:
        return [row[0] for row in csv.reader(f) if row]


def save_task(task):
    with open(TASKS_FILE, 'a', newline='', encoding='utf-8') as f:
        csv.writer(f).writerow([task])


@app.route('/', methods=['GET', 'POST'])
def hello_world():  # put application's code here
    if request.method == 'POST':
        save_task(request.form['task'])
        return redirect('/')
    return render_template('index.html', list=load_tasks())

if __name__ == '__main__':
    app.run()
