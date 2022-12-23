from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Web App with Python Flask!!'

@app.route('/api/health')
def index():
    return 'Health okay'

app.run()
