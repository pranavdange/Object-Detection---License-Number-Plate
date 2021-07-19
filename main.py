from flask import *
import os
import shutil
import glob
import shutil


app = Flask(__name__)


@app.route('/')
def upload():
    return render_template("index.html")


@app.route('/success', methods=['POST'])
def success():
    if request.method == 'POST':
        f = request.files['file']
        f.save("static/img.jpg")

        command = "python detect.py --weights ./checkpoints/custom-416 --size 416 --model yolov4 --images static\img.jpg"
        os.system(command)

        return render_template("output.html")




if __name__ == '__main__':
    app.run(debug=True)