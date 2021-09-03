from flask import render_template, request
from flask import redirect, url_for
import os
from PIL import Image
from app.utils import pipeline_model
from app.utils import face_recognition

UPLOAD_FLODER = 'static/uploads'
def base():
    return render_template('base.html')


def index():
    return render_template('index.html')

def faceapp():
    return render_template('faceapp.html')

def faceapp2():
    return render_template('faceapp2.html')

def getwidth(path):
    img = Image.open(path)
    size = img.size # width and height
    aspect = size[0]/size[1] # width / height
    w = 300 * aspect
    return int(w)

def gender():

    if request.method == "POST":
        f = request.files['image']
        filename=  f.filename
        path = os.path.join(UPLOAD_FLODER,filename)
        f.save(path)
        w = getwidth(path)
        # prediction (pass to pipeline model)
        pipeline_model(path,filename,color='bgr')


        return render_template('gender.html',fileupload=True,img_name=filename, w=w)


    return render_template('gender.html',fileupload=False,img_name="freeai.png")

def predict():
    if request.method == "POST":
        f = request.files['image']
        filename=  f.filename
        path = os.path.join(UPLOAD_FLODER,filename)
        f.save(path)
        w = getwidth(path)
        face_recognition(path,filename,color='bgr')
        return render_template('predict.html',fileupload=True,img_name=filename, w=w)
    return render_template('predict.html',fileupload=False,img_name="freeai.png")


