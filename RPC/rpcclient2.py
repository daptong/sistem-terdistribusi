import requests
import json

def call_rpc(method, params):
    url = "http://rpc-server:4000"
    headers = {'content-type': 'application/json'}
    payload = {
        "jsonrpc": "2.0",
        "method": method,
        "params": params,
        "id": 1,
    }
    response = requests.post(url, data=json.dumps(payload), headers=headers).json()
    return response

try:
    while True:
        msg = input("enter a number in words ('one two three'): ")
        result_convert = call_rpc("convert", [msg])
        print(f"result: {result_convert['result']}")
except KeyboardInterrupt:
    print("\nstopped by user")