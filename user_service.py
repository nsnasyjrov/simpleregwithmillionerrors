import json
import os
from datetime import datetime
from user import User

class UserService:

    path = "data/users.json"

    def __init__(self, file_path = None):
        self.file_path = file_path or UserService.path
        self.ensure_file_exists()

    @staticmethod
    def create_user(username: str,
                    password: str,
                    location: str,
                    birthday: str) -> User:
        user = User()
        user.username = username
        user.password = password
        user.location = location

        try:
            user.birthday = datetime.strptime(birthday, '%Y-%m-%d')
        except ValueError:
            raise ValueError('Неправильный формат даты рождения')

        return user

    def ensure_file_exists(self):
        if not os.path.exists(self.file_path):
            os.makedirs(os.path.dirname(self.file_path), exist_ok=True)
            with open(self.file_path, 'w') as file:
                json.dump([], file)

    def write_user_to_file(self, user: User):
        with open(self.file_path, 'r') as file:
            users = json.load(file)
            users.append({
                'id': user.id,
                'username': user.username,
                'password': user.password,
                'location': user.location,
                'birthday': user.birthday.strftime('%Y-%m-%d')
            })
            with open(self.file_path, 'w') as file:
                json.dump(users, file)

    def find_user_by_username(self, username: str)  -> User:
        try:
            with open(self.file_path, 'r') as file:
                users = json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError("Файл не найден")

        for user in users:
            if user['username'] == username:
                return user