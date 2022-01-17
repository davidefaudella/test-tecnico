#!/usr/bin/env python
# encoding: utf-8

from flask import Flask, request, make_response
from flask_cors import CORS
from models.Receipt import Receipt
from utils import parse

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route("/api/v1/receipts", methods=['POST'])
def create_receipt():
    input_data = request.get_data(as_text=True)
    items = parse(input_data)
    receipt = Receipt(items)
    response = make_response(receipt.toString(), 200)
    response.mimetype = "text/plain"
    return response


if __name__ == "__main__":
    app.run(debug=True)
