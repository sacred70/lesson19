from dao.model.user import User


class UserDAO:
    def __init__(self, session):
        self.session = session


    def get_all(self):
        return self.session.query(User).all()


    def get_user_id(self, uid):
        return self.session.query(User).get(uid)


    def get_user_username(self, username):
        return self.session.query(User).filter(User.username == username).first()

    def create(self, user_d):
        user = User(**user_d)
        self.session.add(user)
        self.session.commit()
        return user

