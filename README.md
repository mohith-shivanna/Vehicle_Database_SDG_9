# Vehicle Verification System

## Overview
The **Vehicle Verification System** is a web application that allows users to verify vehicle information based on its make, model, color, and license plate. The system checks against a database and provides feedback on whether the vehicle details are valid, mismatched, or have an invalid state code.

## Features
- Web-based interface for vehicle verification.
- License plate state code validation.
- Database query to check vehicle authenticity.
- Color-coded alerts for verification results.
- Responsive design for desktop and mobile use.

## Technologies Used
- **Frontend:** HTML, CSS (in `templates/index.html`)
- **Backend:** Flask (Python)
- **Database:** MySQL

## Project Structure
```
Vehicle_Database_SDG_9/
│-- app.py                 # Flask application handling vehicle verification
│-- database_commands.txt  # SQL commands for setting up the database
│-- templates/
│   └── index.html         # Frontend web interface
│-- updated_vehicle_database.csv  # Sample vehicle database (CSV format)
```

## Setup Instructions

### 1. Install Dependencies
Ensure you have Python and MySQL installed. Then install the required Python packages:
```sh
pip install flask mysql-connector-python
```

### 2. Set Up MySQL Database
Run the SQL commands in `database_commands.txt` to create the `vehicle_db` database and `vehicle_data` table:
```sh
mysql -u root -p < database_commands.txt
```

### 3. Add Vehicle Data
Insert vehicle records into the `vehicle_data` table manually or by importing `updated_vehicle_database.csv`.

### 4. Run the Flask Application
Start the Flask server using:
```sh
python app.py
```
By default, it runs on `http://127.0.0.1:5000/`.

## How to Use
1. Open the application in your browser.
2. Enter the **Make**, **Model**, **Color**, and **License Plate** of a vehicle.
3. Click **Verify Vehicle**.
4. The system will check the database and return:
   - ✅ **Verified:** If the vehicle details match.
   - 🚨 **Alert:** If the details mismatch or are missing.
   - ⚠️ **Warning:** If the state code is invalid.

## Future Enhancements
- API integration for real-time RTO data verification.
- User authentication for secure access.
- Extended vehicle data attributes (owner details, registration year, etc.).


