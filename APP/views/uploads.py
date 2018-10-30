from flask import Blueprint, request, render_template, flash, redirect, url_for
from APP.ext import photos

uploads = Blueprint("uploads", __name__)


@uploads.route("/upload/", methods=['GET', 'POST'])
def upload_page():
    if request.method == "GET":
        return render_template('upload.html')
    elif request.method == "POST":
        file = request.files['photo']
        photos.save(request.files['photo'])
        flash("Photo saved.")
    return redirect(url_for("uploads.upload_page"))
