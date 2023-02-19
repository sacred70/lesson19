from dec_cons.constants import PWD_HASH_SALT, PWD_HASH_ITERATIONS
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
        user_data['password'] = self.get_hash(user_data.get('password'))
        return self.dao.create(user_data)

    def update(self, user_data):
        user_data['password'] = self.get_hash(user_data.get('password'))
        return self.dao.update(user_data)

    def delete(self, uid):
        return self.dao.delete(uid)

    def get_hash(self, password):
        """Принимает пароль, отдает хэш"""
        return base64.b64encode(hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        ))

    def compare_passwords(self,pass_hash, password):
        """Принимает хешированный пароль и введенный пароль, создает хеш введенного пароля,
            сравнивает их, возвращает True/False"""

        return hmac.compare_digest(pass_hash, self.get_hash(password))
