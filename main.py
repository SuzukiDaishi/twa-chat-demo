from flask import Flask, render_template, jsonify, request
from  spotsSearch import *
import json

app = Flask(__name__)

@app.route('/')
def home() :
    return render_template('index.html')

@app.route('/chat')
def chat() :
    return render_template('chat.html')

@app.route('/api/chat')
def chat_api():
    chat_doc = request.args.get('text', default="", type=str)
    json_open = open('database/database.json', 'r',encoding='utf-8_sig')
    spots_data = json.load(json_open)
    chat_res = spotSortByDocuments(chat_doc, spots_data)
    return jsonify(chat_res)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)