from flask import Flask, send_file, Response
from datetime import datetime
import pytz
from prometheus_client import Counter, generate_latest

app = Flask(__name__)

# Prometheus counters
gandalf_counter = Counter('gandalf_requests_total', 'Total requests to /gandalf')
colombo_counter = Counter('colombo_requests_total', 'Total requests to /colombo')

# Define a route for the home page
@app.route("/")
def home():
    return "Hello, This is an innovation from adcash. Joining the wonderful team soonest!"

@app.route("/gandalf")
def show_gandalf():
    gandalf_counter.inc()
    return send_file("gandalf.jpeg", mimetype='image/jpeg')

@app.route("/colombo")
def colombo_time():
    colombo_counter.inc()
    now = datetime.now(pytz.timezone('Asia/Colombo'))
    return f"Current time in Colombo: {now.strftime('%Y-%m-%d %H:%M:%S')}"

@app.route("/metrics")
def metrics():
    return Response(generate_latest(), mimetype='text/plain')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)




""" from flask import Flask, send_file
from datetime import datetime
import pytz
from prometheus_client import Counter, generate_latest
from flask import Response

app = Flask(__name__)

gandalf_counter = Counter('gandalf_requests_total', 'Total requests to /gandalf')
colombo_counter = Counter('colombo_requests_total', 'Total requests to /colombo')

@app.route('/gandalf')
def gandalf():
    gandalf_counter.inc()
    return send_file('gandalf.jpg', mimetype='image/jpeg')

@app.route('/colombo')
def colombo():
    colombo_counter.inc()
    time = datetime.now(pytz.timezone('Asia/Colombo'))
    return f"Current time in Colombo: {time.strftime('%Y-%m-%d %H:%M:%S')}"

@app.route('/metrics')
def metrics():
    return Response(generate_latest(), mimetype='text/plain')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
 """