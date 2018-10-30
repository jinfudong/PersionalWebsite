# !usr/bin/env python
# -*- coding:utf-8 _*-


def load_middleware(app):
    @app.before_request
    def before_request():
        pass

    @app.after_request
    def after_request(response):
        return response
