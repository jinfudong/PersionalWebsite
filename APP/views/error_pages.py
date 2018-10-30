from flask import Blueprint, redirect, url_for

error_pages = Blueprint('error_pages', __name__)


@error_pages.app_errorhandler(404)
def handle_404(error):
    return redirect(url_for("home.home_page"))
