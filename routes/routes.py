from classifier.resnet50_classifier import classify_image
from flask import Blueprint
from flask import render_template, request, redirect, session, url_for

routes = Blueprint('routes', __name__)


@routes.route("/whatsonthatimage")
def whatonthatimage_main():
    if 'filename' in session:
        path_to_uploaded_image = 'static/images/' + session['filename']
    else:
        path_to_uploaded_image = 'static/images/elephant.jpg'

    classifications = classify_image(path_to_uploaded_image)

    return render_template('main.html',
                           path_to_uploaded_image=path_to_uploaded_image,
                           classifications=classifications)


@routes.route('/uploader', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save('static/images/' + f.filename)
        session['filename'] = f.filename

        return redirect(url_for(".whatonthatimage_main"))
