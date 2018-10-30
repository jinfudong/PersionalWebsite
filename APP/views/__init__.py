from APP.views.middleware import load_middleware
from .login import login
from .uploads import uploads
from .error_pages import error_pages
from .home import home


def init_views(app):
    load_middleware(app)
    app.register_blueprint(error_pages)
    app.register_blueprint(home)
    app.register_blueprint(uploads)
    app.register_blueprint(login)
