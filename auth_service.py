from user_service import UserService

class AuthService:
    def __init__(self):
        self.service = UserService(UserService.path)
        self.service.ensure_file_exists()

    @staticmethod
    def password_verification():
        while True:
            password = input("Пароль: ")
            repeated_password = input("Повторите пароль: ")
            if password == repeated_password:
                return password
            else:
                print("Пароли не совпадают, повторите ввод")

    def register(self):
        print("Введите данные для регистрации")
        username = input("Имя пользователя: ")
        password = self.password_verification()
        location = input("Город: ")
        birthday = input("Дата рождения в формате 'YYYY-MM-DD': ")

        user = self.service.create_user(username, password, location, birthday)

        self.service.write_user_to_file(user)
        print(f"Пользователь {username} успешно зарегистрирован!")


    def login(self):
        username = input("Введите имя пользователя для авторизации: ")
        find_user = self.service.find_user_by_username(username)

        if find_user is None:
            return False

        inputed_pass = input("Введите пароль: ")
        user_pass = find_user['password']

        if inputed_pass != user_pass:
            print("Неверный пароль, доступ запрещен!")
            return False

        print("Доступ разрешен!")
        return True


