from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
from helpers.get_data import _get_trafikverket_data
import logging 

app = Flask(__name__)
CORS(app)
logging.basicConfig(level=logging.INFO)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_data')
def get_data():
    start_time = request.args.get('start_time')
    logging.info(f'Received request for get_data with start_time: {start_time}')
    
    try:
        data = _get_trafikverket_data(start_time=start_time)
        if data:
            logging.info('Data retrieved successfully')
            return jsonify({
                "total_situations": data["total_situations"],
                "message_type_counts": data["message_type_counts"]
            })
        else:
            logging.error('No data found')
            return jsonify({"error": "Kunde inte hämta data"}), 500
    except Exception as e:
        logging.error(f'Error occurred: {e}')
        return jsonify({"error": "An error occurred while processing your request."}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)