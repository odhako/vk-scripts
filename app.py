from flask import Flask
from flask import render_template, redirect, request, flash
import os

app = Flask(__name__)
app.secret_key = '_aeWaoPNeRsivNAiNHpQng'


@app.route("/", methods=['GET'])
def hello_world():
    if os.path.exists('static/groups.txt'):
        with open('static/groups.txt', 'r') as file:
            groups = file.readlines()
        return render_template('index.html', groups=groups)
    else:
        return render_template('index.html')


@app.route("/add", methods=['POST'])
def add_group():
    form = request.form
    with open('static/groups.txt', 'a') as groups:
        group_url = form['group']
        if group_url.endswith('vk.com') or group_url.endswith('vk.com/'):
            flash('Неправильный адрес')
            return redirect('/')
        if group_url.startswith('https://vk.com'):
            pass
        elif group_url.startswith('vk.com'):
            group_url = 'https://' + group_url
        else:
            flash('Неправильный адрес')
            return redirect('/')
        groups.write(group_url + '\n')
    return redirect('/')
