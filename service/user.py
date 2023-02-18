from constants import PWD_HASH_SALT, PWD_HASH_ITERATIONS
import base64
import hashlib
import hmac
from dao.user import UserDAO


class UserService:
    def __init__(self, dao: UserDAO):
        self.dao = dao
    def get_one(self, uid):
        return self.dao.get_user_id(uid)


    def get_username(self, username):
        return self.dao.get_user_username(username)


    def get_all(self):
        return self.dao.get_all()

    def create(self, user_data):
        user_data['password'] = self.get_hash(user_data['password'])
        return self.dao.create(user_data)


