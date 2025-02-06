from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# MySQL database configuration
db_config = {
    'user': 'root',
    'password': 'root',
    'host': 'localhost',
    'database': 'vehicle_db'
}

state_names = {
    "AP": "Andhra Pradesh", "AR": "Arunachal Pradesh", "AS": "Assam", "BR": "Bihar", "CG": "Chhattisgarh",
    "CH": "Chandigarh", "DD": "Daman and Diu", "DL": "Delhi", "GA": "Goa", "GJ": "Gujarat", "HR": "Haryana",
    "HP": "Himachal Pradesh", "JH": "Jharkhand", "JK": "Jammu and Kashmir", "KA": "Karnataka", "KL": "Kerala",
    "LA": "Ladakh", "LD": "Lakshadweep", "MH": "Maharashtra", "ML": "Meghalaya", "MN": "Manipur", "MP": "Madhya Pradesh",
    "MZ": "Mizoram", "NL": "Nagaland", "OD": "Odisha", "PB": "Punjab", "PY": "Puducherry", "RJ": "Rajasthan",
    "SK": "Sikkim", "TN": "Tamil Nadu", "TR": "Tripura", "TS": "Telangana", "UK": "Uttarakhand", "UP": "Uttar Pradesh", "WB": "West Bengal"
}

special_boards = {"CD": "Diplomatic Corps", "UN": "United Nations", "XX": "Special Test Vehicles", "IND": "Government of India", "BH": "Bharat (Electric Vehicles)"}

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        make = request.form['make']
        model = request.form['model']
        color = request.form['color']
        plate = request.form['plate'].upper()
        
        state_code = plate[:2]
        state_name = state_names.get(state_code, special_boards.get(state_code, "Unknown"))

        # Connect to the MySQL database
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)

        # Query the database
        query = """
        SELECT * FROM vehicle_data
        WHERE Model = %s AND Color = %s AND License_Plate = %s
        """
        cursor.execute(query, (model, color, plate))
        match = cursor.fetchone()

        cursor.close()
        conn.close()
        
        if state_name == "Unknown":
            result = f"⚠️ WARNING: Vehicle {plate} has an invalid state code ({state_code})."
        elif match is None:
            result = f"🚨 ALERT: Mismatch detected! Vehicle {plate} ({model}, {color}) is not in the database and registered under {state_name}."
        else:
            result = f"✅ Verified: Vehicle {plate} ({model}, {color}) is authentic and registered under {state_name}."
    
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
