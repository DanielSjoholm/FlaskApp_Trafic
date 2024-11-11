from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
from helpers.get_data import get_trafikverket_data
from helpers.filter_data import filter_trafikverket_data
from dotenv import load_dotenv
import logging

app = Flask(__name__)
CORS(app)

load_dotenv()
logging.basicConfig(level=logging.INFO)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get_data')
def get_data():
    start_time = request.args.get('start_time')
    logging.info(f'Received request for get_data with start_time: {start_time}')
    
    try:
        # Steg 1: Hämta rådata från API
        raw_data = get_trafikverket_data()
        
        if raw_data:
            logging.info('Raw data retrieved successfully')

            # Steg 2: Filtrera och bearbeta rådata
            filtered_data = filter_trafikverket_data(raw_data, start_time=start_time)
            
            logging.info('Data filtered successfully')
            return jsonify({
                "total_situations": filtered_data["total_situations"],
                "message_type_counts": filtered_data["message_type_counts"]
            })
        else:
            logging.error('No data found')
            return jsonify({"error": "Kunde inte hämta data"}), 500
    except Exception as e:
        logging.error(f'Error occurred: {e}')
        return jsonify({"error": "An error occurred while processing your request."}), 500


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)
