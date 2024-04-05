from flask import Flask, request, jsonify
import os
import decipher_sdk

app = Flask(__name__)

decipher_sdk.init(
    codebase_id="CODEBASE_NAME_HERE",
    customer_id="CUSTOMER_ID_HERE"
)

@app.route("/")
def hello_world():
    return '''
    <html>
        <head>
            <title>Submit Data</title>
            <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
        </head>
        <body>
            <button id="submitBtn">Submit</button>
            <script>
                $(document).ready(function() {
                    $("#submitBtn").click(function() {
                        $.ajax({
                            url: "/submit",
                            type: "POST",
                            contentType: "application/json",
                            data: JSON.stringify({ "name": "vincent" }),
                            success: function(response) {
                                alert("Data submitted successfully!");
                            },
                            error: function(xhr, status, error) {
                                alert("An error occurred: " + xhr.responseText);
                            }
                        });
                    });
                });
            </script>
        </body>
    </html>
    '''

@app.route("/submit", methods=['POST'])
def submit_data():
    data = request.json
    print("Entered /submit")
    print("Received data:", data)
    loadInit(data)
    return jsonify({"status": "success", "received_data": data}), 200

@app.route("/items/<int:item_id>", methods=['GET'])
def get_item(item_id):
    # Here you would typically retrieve and return an item based on the item_id
    return jsonify({"item_id": item_id, "item": "Item details would be here"}), 200

@app.route("/items", methods=['POST'])
def create_item():
    item_data = request.json
    # Here you would typically save the item_data to a database
    return jsonify({"created_item": item_data}), 201

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(debug=True, host='0.0.0.0', port=port)