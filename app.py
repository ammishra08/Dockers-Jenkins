from flask import Flask, render_template

# Create a Flask app
app = Flask(__name__, template_folder = '.')

# Define a route and its handler
@app.route('/')
def hello_world():
    return render_template('index.html')

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')