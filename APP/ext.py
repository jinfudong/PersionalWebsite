import os
from flask_debugtoolbar import DebugToolbarExtension
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_uploads import configure_uploads, UploadSet, IMAGES


models = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
photos = UploadSet('photos', IMAGES)


def init_ext(app):
    # 注册数据库插件
    models.init_app(app)
    # 加入迁移指令 python manage.py db migrate
    # 加入迁移指令 python manage.py db upgrade
    migrate.init_app(app, models)
    # 注册登录组件
    login_manager.init_app(app)
    # 更新配置信息并加入上传插件配置
    configure_uploads(app, (photos,))
    # 注册DebugToolbar
    if os.environ.get("FLASK_ENV") == "development":
        DebugToolbarExtension(app)
