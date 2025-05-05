import os
from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Secret key
app.secret_key = os.getenv("SECRET_KEY", "9d367b3ba8e8654c6433379763e80c6e")

# Get the FLAG from the environment variable, or use a default value
FLAG = os.getenv("FLAG", "encryptCTF{comments_&_indentations_makes_johnny_a_good_programme}")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encryptCTF', methods=["GET"])
def getflag():
    return jsonify({'flag': FLAG})

# Don't use app.run() in production, Vercel will handle the server
if __name__ == '__main__':
    app.run(debug=False)
