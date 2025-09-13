from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Flask API!"

# 1) Static route with the exact message
@app.get('/birthday/monisha')
def birthday_monisha():
    return "Happy birthday monisha. wish u success and good health"

# 2) Dynamic route to reuse the wish for any name
@app.get('/birthday/<name>')
def birthday_any(name):
    return f"Happy birthday {name}. wish u success and good health"

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
