class cor_account:
    def __init__(self, num_account, name_corr, saldo=0):
        self.num_account = num_account
        self.name_corr = name_corr
        self.saldo = saldo

    def after_name(self, new_name):
        self.name_corr = new_name

    def deposit(self, value):
        self.saldo = self.saldo + value

    def withdrawal(self, value):
        self.saldo -= value

account = cor_account(66666666, 'Daniel Lima', 45234)
print(account.name_corr)
print(account.num_account)
print(account.saldo)

account.after_name('Joaquim')
account.deposit(20234)
account.withdrawal(2345)
print(account.name_corr)
print(account.num_account)
print(account.saldo)