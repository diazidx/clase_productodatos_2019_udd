from __future__ import division, print_function
# coding=utf-8
import numpy as np
import cv2
import os

# Flask utils
from flask import Flask, redirect, url_for, request, render_template, send_file, send_from_directory
from werkzeug.utils import secure_filename

# Define a flask app
app = Flask(__name__)


def model_predict(img_path):
    """
       model_predict will return the preprocessed image
    """
    AGE_BUCKETS = ["(0-2)", "(4-6)", "(8-12)", "(15-20)", "(25-32)", "(38-43)", "(48-53)", "(60-100)"]

    # load our serialized face detector model from disk
    # print("[INFO] loading face detector model...")
    prototxtPath = "models/face_detector/deploy.prototxt"
    weightsPath = "models/face_detector/res10_300x300_ssd_iter_140000.caffemodel"
    faceNet = cv2.dnn.readNet(prototxtPath, weightsPath)

    # load our serialized age detector model from disk
    # print("[INFO] loading age detector model...")
    prototxtPath = "models/age_detector/age_deploy.prototxt"
    weightsPath = "models/age_detector/age_net.caffemodel"
    ageNet = cv2.dnn.readNet(prototxtPath, weightsPath)

    # load the input image and construct an input blob for the image
    image = cv2.imread(img_path)
    (h, w) = image.shape[:2]
    blob = cv2.dnn.blobFromImage(image, 1.0, (300, 300), (104.0, 177.0, 123.0))

    # pass the blob through the network and obtain the face detections
    # print("[INFO] computing face detections...")
    faceNet.setInput(blob)
    detections = faceNet.forward()

    # loop over the detections
    for i in range(0, detections.shape[2]):
        # extract the confidence (i.e., probability) associated with the
        # prediction
        confidence = detections[0, 0, i, 2]

        # filter out weak detections by ensuring the confidence is
        # greater than the minimum confidence
        if confidence > 0.5:
            # compute the (x, y)-coordinates of the bounding box for the
            # object
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (startX, startY, endX, endY) = box.astype("int")

            # extract the ROI of the face and then construct a blob from
            # *only* the face ROI
            face = image[startY:endY, startX:endX]
            faceBlob = cv2.dnn.blobFromImage(face, 1.0, (227, 227), (78.4263377603, 87.7689143744, 114.895847746),
                                             swapRB=False)

            # make predictions on the age and find the age bucket with
            # the largest corresponding probability
            ageNet.setInput(faceBlob)
            preds = ageNet.forward()
            i = preds[0].argmax()
            age = AGE_BUCKETS[i]
            ageConfidence = preds[0][i]

            # display the predicted age to our terminal
            text = "{}: {:.2f}%".format(age, ageConfidence * 100)
            # print("[INFO] {}".format(text))

            # draw the bounding box of the face along with the associated
            # predicted age
            y = startY - 10 if startY - 10 > 10 else startY + 10
            cv2.rectangle(image, (startX, startY), (endX, endY), (0, 0, 255), 2)
            cv2.putText(image, text, (startX, y), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)

        # display the output image
        cv2.imwrite(img_path, image)
    return text
    # cv2.imshow("Image", image)
    # cv2.waitKey(0)


@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index.html')


file_name= ''


@app.route('/predict', methods=['GET', 'POST'])
def upload():
    global file_name
    if request.method == 'POST':
        # Get the file from post request
        f = request.files['file']

        # Save the file to ./uploads
        basepath = os.path.dirname(__file__)
        file_name = secure_filename(f.filename)
        file_path = os.path.join(basepath, 'uploads', file_name)
        f.save(file_path)

        # Make prediction
        preds = model_predict(file_path)
        return preds
    return None


@app.route('/get-file/', methods=['GET'])
def get_file():
    global file_name
    fpath = 'uploads/' + file_name
    return send_file(fpath, as_attachment=True, attachment_filename=file_name)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0/0", port=5000)
