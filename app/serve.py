"""The solilo server."""

import datetime
import os

from flask import Flask
from flask import render_template
from flask import request


app = Flask(__name__)
SAVE_DIR = 'saved-notes'


@app.route('/')
def index():
  return render_template('index.html')


@app.route('/write')
def write():
  return render_template('write.html')


@app.route('/save', methods=['POST'])
def save():
  if not os.path.exists(SAVE_DIR):
    os.makedirs(SAVE_DIR)
  now = datetime.datetime.now().strftime('%Y-%m-%d-at-%H:%M')
  filename = '%s.txt' % now
  filepath = os.path.join(SAVE_DIR, filename)
  with open(filepath, 'w') as savefile:
    savefile.write(request.form['text'])
  return ''


@app.route('/read')
def read():
  return render_template('read.html')


if __name__ == '__main__':
  app.run(debug=True)
