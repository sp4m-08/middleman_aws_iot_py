from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

SUPABASE_URL = "https://ioxmssaxiqqvhqowrxwi.supabase.co"
SUPABASE_API_KEY = os.getenv("SUPABASE_API_KEY")
TABLE_NAME = "Data"

@app.route("/", methods=["GET", "POST"])
def receive():

    # AWS confirmation
    if request.method == "GET" and "confirmationToken" in request.args:
        print("AWS Confirmation Successful")
        return "", 200

    if request.method == "POST":
        try:
            data = request.get_json(force=True)
            print("Received:", data)

            headers = {
                "apikey": SUPABASE_API_KEY,
                "Authorization": f"Bearer {SUPABASE_API_KEY}",
                "Content-Type": "application/json"
            }

            response = requests.post(
                f"{SUPABASE_URL}/rest/v1/{TABLE_NAME}",
                headers=headers,
                json=data
            )

            print("Supabase response:", response.status_code, response.text)

            return jsonify({"status": "stored"}), 200

        except Exception as e:
            print("Error:", str(e))
            return jsonify({"error": str(e)}), 500

    return "", 400
