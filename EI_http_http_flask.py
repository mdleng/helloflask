from flask import Flask, request

app = Flask(__name__)

@app.route('/sensor', methods=['POST'])
def sensor():
    # Get the JSON data from the request
    data = request.get_json()
    # Print the data to the console
    print(data)
    # Return a success message
    return 'JSON received!'
