import json
import hashlib
import requests
import flask
from flask import request
app = flask.Flask(__name__)
app.config["DEBUG"] = True



@app.route('/zadanie1', methods=['Post'])
def change_json():
    data=request.json
    data['result']=data.pop('data_list')
    for person in data['result']:
        concat_string=person['first_name']+person['second_name']+person['birth_date']
        encoded = concat_string.encode()
        person['hash']=hashlib.sha256(encoded).hexdigest()
    data['result']=sorted(data['result'],key=lambda x:(x['second_name'],x['first_name']),reverse=False)
    data_response=json.dumps(data)
    return data_response


@app.route('/zadanie2', methods=['Post'])
def calculate_price():
    orderbook_data =json.loads(requests.get(
        'https://bitbay.net/API/Public/BTCPLN/orderbook.json').content)['asks']
    data = request.json

    amount=float(data['buy'])
    i=0
    price=0.0
    while(amount>0):
        print(amount)
        if(amount>float(orderbook_data[i][1])):
            price+=float(orderbook_data[i][0])*float(orderbook_data[i][1])
            amount-=float(orderbook_data[i][1])
            i+1
        else :
            price+=float(orderbook_data[i][0])*(float(orderbook_data[i][1])-amount)
            amount=0
    data_response=json.dumps({'price':price})
    return data_response

app.run(host='0.0.0.0')