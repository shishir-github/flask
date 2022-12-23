from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Web App with Python Flask!'


@app.route('/api/health')
def health():
    return 'Health okay'

app.run(debug=True)
