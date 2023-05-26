from flask import Flask, render_template, Response
import cv2

app = Flask(__name__)
camera = cv2.VideoCapture(0)


def generate_frames():
    while True:

        ## read the camera frame
        success, frame = camera.read()
        if not success:
            break
        else:
            # frame=camera.
            ret, buffer = cv2.imencode('.jpg', frame)

            frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


def index():
    return render_template('2.html')


@app.route('/video')
def video():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == "__main__":
    app.run(debug=True)




____________________________________________________________________________________


def generate_frames(string_data):
    while True:
        # Generate or retrieve the frame data
        frame = get_frame_data()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n'
               b'Additional string data: ' + string_data.encode() + b'\r\n')

string_data = "Hello, world!"  # Example string data
return Response(generate_frames(string_data), mimetype='multipart/x-mixed-replace; boundary=frame')

