import os
from datetime import timedelta


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def get_db_uri(dbinfo):

    engine = dbinfo.get("ENGINE") or "sqlite"
    driver = dbinfo.get("DRIVER") or "sqlite"
    user = dbinfo.get("USER") or ""
    password = dbinfo.get("PASSWORD") or ""
    host = dbinfo.get("HOST")
    port = dbinfo.get("PORT")
    name = dbinfo.get("NAME")
    return "{}+{}://{}:{}@{}:{}/{}".format(engine, driver, user, password, host, port, name)


class Config:
    # 数据库配置
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # 上传配置
    UPLOADED_PHOTOS_DEST = "/var/www/PW/static/uploads"
    # UPLOADED_IMAGES_DEST = os.getcwd()
    MAX_CONTENT_LENGTH = 2 * 1024 * 1024
    SECRET_KEY = os.urandom(24)
    PERMANENT_SESSION_LIFETIME = timedelta(days=7)  # 设置session的保存时间。


class DevelopConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:////var/www/PW/PW.db"


class TestConfig(Config):
    TESTING = True

    dbinfo = {

        "ENGINE": "mysql",
        "DRIVER": "pymysql",
        "USER": "theodore",
        "PASSWORD": "1997112Lxd6035.",
        "HOST": "10.0.122.205",
        "PORT": "3306",
        "NAME": "PW",

    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(dbinfo)


class StagingConfig(Config):

    dbinfo = {
        "ENGINE": "mysql",
        "DRIVER": "pymysql",
        "USER": "theodore",
        "PASSWORD": "1997112Lxd6035.",
        "HOST": "10.0.122.205",
        "PORT": "3306",
        "NAME": "PW",
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(dbinfo)


class ProductConfig(Config):
    dbinfo = {
        "ENGINE": "mysql",
        "DRIVER": "pymysql",
        "USER": "theodore",
        "PASSWORD": "1997112Lxd6035.",
        "HOST": "10.0.122.205",
        "PORT": "3306",
        "NAME": "PW",
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(dbinfo)


envs = {
    "development": DevelopConfig,
    "testing": TestConfig,
    "staging": StagingConfig,
    "product": ProductConfig,
    "default": DevelopConfig
}

