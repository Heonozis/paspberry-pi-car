from flask import Flask, jsonify, request, render_template
from car import Car

app = Flask(__name__)
car = Car()
car.start()


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "OK"})


@app.route("/drive", methods=["GET"])
def drive():
    return render_template('drive.html')


@app.route("/ride", methods=["POST", "OPTIONS"])
def ride():
    json_request = request.get_json()
    print('Incoming request: {}'.format(json_request))
    angle = json_request["angle"]
    radius = json_request["radius"]
    car.ride(radius, angle)
    return jsonify({"status": "OK"})


@app.route("/stop", methods=["GET"])
def stop():
    car.stop()


@app.route("/start", methods=["GET"])
def start():
    car.start()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)

print("Server is down now")
car.stop()








