from flask import Flask, render_template, request
import os
from flask.globals import request
from werkzeug.utils import secure_filename

app = Flask(__name__)
Username = "WENHUIZHU"
ALLOWED_EXTENSIONS = {'png', 'jpg', 'JPG', 'PNG', 'bmp','mp4','ts'}

@app.route('/')
def test():
    return 'server is running'

@app.route('/upload')
def upload_file(): 
    return render_template('./upload.html')

@app.route('/predic', methods = ['POST'])
def image_preprocess(): 
    f = request.files['file']
    gestureName = request.headers.get('gesture')
    ext = f.filename.rsplit('.', 1)[1]
    basepath = os.path.dirname(__file__)
    savepath = 'upload/'+gestureName
    checkpath = os.path.join(basepath,savepath)
    PracticeNumber  = len(os.listdir(checkpath)) + 1
    new_filename = gestureName + '_PRACTICE_'+ str(PracticeNumber) + '_' + Username + '.'+ext
    upload_file = os.path.join(basepath,savepath, new_filename)
    f.save(upload_file)
    return 'file upload successfully!'

if __name__ == '__main__':
    app.run(host= '192.168.0.81',port=8088,debug=True)