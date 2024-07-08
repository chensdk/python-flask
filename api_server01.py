from flask import Flask, request, jsonify

import sqlite3

 

app = Flask(__name__)

db_name = 'plc.db'

 

# Function to initialize the database if not exists

def init_db():

    conn = sqlite3.connect(db_name)

    cursor = conn.cursor()

    cursor.execute('''

        CREATE TABLE IF NOT EXISTS plc_tb (

            address TEXT PRIMARY KEY,

            value INTEGER

        )

    ''')

    conn.commit()

    conn.close()

 

# Initialize the database when the app starts

init_db()

 

@app.route('/api/put', methods=['POST'])

def post_data():

    try:

        data = request.get_json()

 

        # Extract address and value from JSON data

        address = data.get('address')

        value = data.get('value')

        print("get input :" ,address ,value)

        # Validate inputs

        if not address or not value:

            return jsonify({'error': 'Address and value are required.'}), 400

 

        # Connect to the database

        conn = sqlite3.connect(db_name)

        cursor = conn.cursor()

 

        # Check if the address already exists in the database

        cursor.execute('SELECT * FROM plc_tb WHERE address = ?', (address,))

        existing_data = cursor.fetchone()

 

        if existing_data:

            # Update existing record

            cursor.execute('UPDATE plc_tb SET value = ? WHERE address = ?', (value, address))

        else:

            # Insert new record

            cursor.execute('INSERT INTO plc_tb (address, value) VALUES (?, ?)', (address, value))

 

        conn.commit()

 

        # Fetch all records from plc_tb after update

        cursor.execute('SELECT * FROM plc_tb')

        updated_data = cursor.fetchall()

 

        conn.close()

 

        # Prepare response with updated data

        response_data = [{'address': row[0], 'value': row[1]} for row in updated_data]

 

        return jsonify({

            'msg': 'Data updated successfully.',

            'plc_tb': response_data

        }), 200

 

    except Exception as e:

        return jsonify({'error': str(e)}), 500

 

@app.route('/api/get', methods=['POST'])

def get_data():

    try:

        data = request.get_json()
        print("get",data)
 

        # Extract address from JSON data

        address = data.get('address')

 

        if not address:

            return jsonify({'error': 'Address is required.'}), 400

 

        # Connect to the database

        conn = sqlite3.connect(db_name)

        cursor = conn.cursor()

 

        # Retrieve data based on address

        cursor.execute('SELECT * FROM plc_tb WHERE address = ?', (address,))

        fetched_data = cursor.fetchone()

 

        conn.close()

 

        if fetched_data:

            # Prepare response if data found

            response_data = {'address': fetched_data[0], 'value': fetched_data[1]}

            return jsonify({

                'msg': 'Data found.',

                'plc_tb': response_data

            }), 200

        else:

            # Return message if no data found

            return jsonify({'msg': 'No data found for the provided address.'}), 404

 

    except Exception as e:

        return jsonify({'error': str(e)}), 500

 

if __name__ == '__main__':

    app.run(debug=True, port=5010)