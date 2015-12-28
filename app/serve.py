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
  # First get the filepaths ordered.
  ordered_filepaths = []
  for filename in os.listdir(SAVE_DIR):
    ordered_filepaths.append(os.path.join(SAVE_DIR, filename))
  ordered_filepaths = sorted(ordered_filepaths, reverse=True)
  # Read each file.
  notes = []
  for filepath in ordered_filepaths:
    with open(filepath) as savefile:
      contents = savefile.read()
    notes.append({
      'filename': os.path.basename(filepath),
      'contents': contents,
    })
  return render_template('index.html', notes=notes)


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


if __name__ == '__main__':
  app.run(debug=True)
