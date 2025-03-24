from auth_service import AuthService


class Console:

    def __init__(self):
        self.service = AuthService()

    @staticmethod
    def console():

        console_instance = Console()

        try:
            while True:
                choice = int(input("1 - регистрация\n2 - авторизация \n3 - выход и из программы\nВаш выбор: "))
                match choice:
                    case 1:
                        console_instance.service.register()
                    case 2:
                        console_instance.service.login()
                    case 3:
                        print("Программа завершила свою работу")
                        break
                    case _:
                        print("Вы ввели что-то не то, повторите снова!")
                        break

        except ValueError:
            print("Ты ввел вброс, лейм, сделай реопен проги epta")
            return
