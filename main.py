from flask import Flask, request
import redis

app = Flask(__name__)
r = redis.Redis(host='redis', port=6379)

@app.route('/set', methods=['POST'])
def set_key():
    key = request.form['key']
    value = request.form['value']
    r.set(key, value)
    return f'Key {key} set to value {value}'

# http://localhost:5000/get?key=mykey
@app.route('/get')
def get_value():
    key = request.args.get('key')
    value = r.get(key)
    if value:
        return f'The value of {key} is {value.decode()}'
    else:
        return f'No value found for {key}'

if __name__ == '__main__':
    app.run(debug=True)

