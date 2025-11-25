from flask import Flask, jsonify, request

app = Flask(__name__)

def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

@app.route("/")
def home():
    return jsonify({"message": "Calculator API is running!"})

@app.route("/add")
def add_route():
    a = float(request.args.get("a"))
    b = float(request.args.get("b"))
    return jsonify({"result": add(a, b)})

@app.route("/hello")
def hello_route():
    return jsonify({"message": "Hello from CI/CD + Jenkins + Docker + Render!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
