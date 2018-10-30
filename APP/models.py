from APP.ext import login_manager, models


# 登录查库操作，传入用户唯一标示，返回用户对象
@login_manager.user_loader
def load_user(userid):
    return User.get(userid)


# 数据库用户表
class User(models.Model):
    id = models.Column(models.Integer, primary_key=True)
    username = models.Column(models.String(32))
    user_password = models.Column(models.String(256))
    is_authenticated = models.Column(models.Boolean)
    is_active = models.Column(models.Boolean)
    is_anonymous = models.Column(models.Boolean)

    def get_id(self):
        return self.id

    def save(self):
        models.session.add(self)
        models.session.commit()


# 数据库学生表
class Student(models.Model):
    id = models.Column(models.Integer, primary_key=True)
    s_name = models.Column(models.String(20))
    s_password = models.Column(models.String(256))


class News(models.Model):
    id = models.Column(models.Integer, primary_key=True)
    title = models.Column(models.String(64))
    content = models.Column(models.Text)

    def save(self):
        models.session.add(self)
        models.session.commit()
