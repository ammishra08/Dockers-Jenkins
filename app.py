from flask import Flask

# Create a Flask app
app = Flask(__name__)

# Define a route and its handler
@app.route('/')
def hello_world():
    return 'Hello, World! This is a basic Flask web application.'

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')