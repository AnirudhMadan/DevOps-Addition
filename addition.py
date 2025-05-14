from flask import Flask, request, jsonify

app = Flask(__name__)

def add(a, b):
    """Function to add two numbers."""
    return a + b

@app.route('/add', methods=['GET'])
def add_numbers():
    """Endpoint to add numbers via HTTP request."""
    try:
        num1 = int(request.args.get('num1'))
        num2 = int(request.args.get('num2'))
        result = add(num1, num2)
        return jsonify({"result": result})
    except (ValueError, TypeError):
        return jsonify({"error": "Invalid input. Provide integers only."}), 400

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
