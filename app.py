from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Web App with Python Flask!'


@app.route('/api/health')
def health():
    return 'Health okay'

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)
