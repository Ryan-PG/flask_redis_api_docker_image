from flask import Flask, request, jsonify
import redis

app = Flask(__name__)
r = redis.Redis(host='redis', port=6379)

# http://localhost:5000/get?key=mykey
# USAGE: curl -X POST localhost:5000/set -H 'Content-Type: application/json' -d '{"key":name","value":"Ryan Heida"}'
@app.route('/set', methods=['POST'])
def set_key():
    if request.method == 'POST':
        data = request.get_json()
        key = data['key']
        value = data['value']
        print(key, value) 
        r.set(key, value)
        return f'Key {key} set to value {value}\n', 200
    else:
        return 'Request method is not correct\n', 400

# http://localhost:5000/get?key=mykey
# USAGE: curl localhost:5000/get?key=mykey
@app.route('/get')
def get_value():
    key = request.args.get('key')
    value = r.get(key)
    if value:
        return f'The value of {key} is {value.decode()}\n'
    else:
        return f'No value found for {key}\n'

if __name__ == '__main__':
    app.run(debug=True)


