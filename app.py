from flask import Flask, jsonify
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Hello, Jenkins + Docker!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
