from flask import Flask, request, jsonify

app = Flask(__name__)
last_data={
        'id': 0
    }
@app.route('/sensor', methods=['POST'])
def sensor():
    global last_data
    # Get the JSON data from the request
    data = request.get_json()
    last_data=data
    # Print the data to the console
    print(data)
    # Return a success message
    return 'JSON received!'

@app.route('/data')
def data():
    global last_data
    return jsonify(last_data)
