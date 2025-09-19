import requests
import argparse
import sys

BASE = 'http://rest-server:5152'

def call(endpoint, a, b):
    try:
        r = requests.get(f"{BASE}/{endpoint}", params={'a': a, 'b': b}, timeout=3)
        if r.status_code == 200:
            data = r.json()
            print(f"{endpoint}({a}, {b}) = add: {data['add']}, mul: {data['mul']}")
        else:
            print(f"{endpoint} error {r.status_code}: {r.text}")
    except Exception as e:
        print(f"{endpoint} exception: {e}")

def main():
    parser = argparse.ArgumentParser(description="rest client for calc")
    parser.add_argument('-a', type=int, default=10)
    parser.add_argument('-b', type=int, default=5)
    args = parser.parse_args()
    call('calc', args.a, args.b)

if __name__ == '__main__':   
    sys.exit(main())