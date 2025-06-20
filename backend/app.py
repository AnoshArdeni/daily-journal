from flask import Flask, jsonify, request
from flask_cors import CORS
from database import get_db_connection, initialize_db
import requests

app = Flask(__name__)
CORS(app)

initialize_db()

# Initialize the database and create the journal_entries table if it doesn't exist
@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Daily Journal API!"})

# Endpoint to get all journal entries
# Returns a list of all entries in descending order by creation date
@app.route('/api/journal', methods=['GET'])
def get_entries():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM journal_entries ORDER BY created_at DESC')
    entries = cursor.fetchall()
    conn.close()

    if not entries:
        print("No entries found.")
        return jsonify([]), 200  # Or return a message if preferred

    print(f"Fetched {len(entries)} entries.")
    return jsonify([dict(entry) for entry in entries]), 200

# Endpoint to create a new journal entry
# Expects a JSON payload with 'date', 'mood', and 'entry' fields
@app.route('/api/journal', methods=['POST'])
def create_entry():
    data = request.get_json()
    if not data or 'date' not in data or 'mood' not in data or 'entry' not in data:
        return jsonify({"error": "Invalid input"}), 400
    
    date = data.get('date')
    mood = data.get('mood')
    entry = data.get('entry')

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO journal_entries (date, mood, entry)
        VALUES (?, ?, ?)
    ''', (date, mood, entry))

    conn.commit()
    conn.close()

    return jsonify({"message": "Entry created successfully",
                    "date" : date, "mood" : mood, "entry" : entry}), 201


@app.route('/api/quote', methods=['GET'])
def get_quote():
    try:
        response = requests.get('https://api.quotable.io/random', timeout=5)
        response.raise_for_status()
        quote_data = response.json()
        return jsonify({
            "quote": quote_data.get("content"),
            "author": quote_data.get("author")
        }), 200
    except requests.RequestException:
        # fallback quote if the API call fails
        print("Failed to fetch quote from API, using fallback quote.")
        return jsonify({
            "quote": "Keep your face always toward the sunshine—and shadows will fall behind you.",
            "author": "Walt Whitman"
        }), 200

# Endpoint to get a specific journal entry by date
@app.route('/api/journal/<date>', methods=['GET'])
def get_entry_by_date(date):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM journal_entries WHERE date = ?', (date,))
    entries = cursor.fetchall()
    conn.close()
    if entries:
        return jsonify([dict(e) for e in entries]), 200
    else:
        return jsonify({"error": "No entries found for that date"}), 404


if __name__ == '__main__':
    app.run(debug=True)

