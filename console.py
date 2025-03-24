from auth_service import AuthService


class Console:

    def __init__(self):
        self.service = AuthService()

    @staticmethod
    def console():

        console_instance = Console()

        while True:
            choice = int(input("1 - регистрация \n 2 - авторизация \n 3 - выход и из программы \n Ваш выбор: "))
            match choice:
                case 1:
                    console_instance.service.register()
                case 2:
                    console_instance.service.login()
                case 3:
                    print("Программа завершила свою работу")
                    break