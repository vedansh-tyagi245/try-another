from flask import Flask, request, jsonify
from pymongo import MongoClient
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

app = Flask(__name__)

# MongoDB URI from MongoDB Atlas
MONGO_URI = os.getenv("MONGO_URI")

# Connect to MongoDB
client = MongoClient(MONGO_URI)
db = client['MyDB']  # Name of the database
collection = db['names']  # Name of the collection

@app.route('/add_name', methods=['POST'])
def add_name():
    try:
        # Get the name from the request body
        data = request.get_json()
        name = data.get('name')

        if not name:
            return jsonify({'error': 'Name is required'}), 400

        # Insert the name into MongoDB
        collection.insert_one({'name': name})

        return jsonify({'message': 'Name added successfully'}), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
