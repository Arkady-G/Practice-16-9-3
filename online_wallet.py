class Client:
    def __init__(self, first_name, second_name, balance):
        self.first_name = first_name
        self.second_name = second_name
        self.balance = balance

    def getfirstname(self):
        return self.first_name

    def getsecondname(self):
        return self.second_name

    def getbalance(self):
        return self.balance

    def print_list(self):
        print('Клиент "{} {}". Баланс: {} рублей.'.format(self.first_name, self.second_name, self.balance))
