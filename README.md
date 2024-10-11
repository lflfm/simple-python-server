# Flask Server Instructions

## Setup and Run the Server

1. Create Virtual Environment

   `python -m venv venv && source venv/bin/activate`

2. Install Dependencies

   `pip install -r requirements.txt`

3. Run the Server

   `python app.py`  
   The server will start on http://0.0.0.0:5000.

## Run Tests

1. Activate Virtual Environment (if not already activated)

   `python -m venv venv && source venv/bin/activate`

2. Install Dependencies

   `pip install -r requirements.txt`

3. Run Tests

   `python -m unittest tests.py`  
   This will execute all the unit tests for the Flask server.
