from flask import Flask, request, render_template, send_from_directory
import json
import requests

app = Flask(__name__)
@app.route('/bab'):
  return "hello bab"
@app.route('/')
def home_page():
  return send_from_directory('LinkCru', 'index.html')

@app.route('/<path:path>')
def pages(path):
  return send_from_directory('LinkCru', path)

if __name__ == '__main__':
  app.run()
