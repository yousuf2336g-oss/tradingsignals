import requests
from flask import Flask, request

app = Flask(__name__)

TELEGRAM_TOKEN = "8386452477:AAF2GhicIHYtZsqHa7dmahspEcvt1YCbMN4"
CHAT_ID = "7123799580"

@app.route('/signal', methods=['POST'])
def signal():
    data = request.json
    message = data.get('message', '🚨 New Trading Signal!')
    requests.get(f'https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage',
                 params={'chat_id': CHAT_ID, 'text': message})
    return 'ok', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

