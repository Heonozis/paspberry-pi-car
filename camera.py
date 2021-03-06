from flask import Flask, jsonify, Response
from flask_cors import cross_origin
from app.camera import Camera
from app.car import Car

app = Flask(__name__)
car = Car()
car.start()


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "OK"})


@cross_origin()
@app.route('/')
def video_feed():
    camera = Camera()
    return Response(camera.stream(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8081, debug=True)

print("Camera is down now")
