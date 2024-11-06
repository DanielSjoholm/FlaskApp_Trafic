from flask import Flask, render_template, jsonify, request
from helpers.get_data import _get_trafikverket_data

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_data')
def get_data():
    try:
        data = _get_trafikverket_data()
        if data:
            return jsonify({
                "total_situations": data["total_situations"],
                "message_type_counts": data["message_type_counts"]
            })
        else:
            print('No data found')
            return jsonify({"error": "Kunde inte hämta data"}), 500
    except Exception as e:
        print(f'Error occurred: {e}')
        return jsonify({"error": "An error occurred while processing your request."}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)