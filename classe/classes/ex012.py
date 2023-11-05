class AccountInvestiment:
    def __init__(self, num_account, name_account, taxa_juros, saldo=0):
        self.num_account = num_account
        self.name_account = name_account
        self.taxa_juros = taxa_juros
        self.saldo = saldo

    def addJuros(self):
        juros = self.taxa_juros * self.saldo

        self.saldo -= juros


savings_accounts = AccountInvestiment("6666 666 6", 'Daniel', 10.4/100, 10343)

savings_accounts.addJuros()
print(savings_accounts.saldo)
savings_accounts.addJuros()
savings_accounts.addJuros()
savings_accounts.addJuros()
savings_accounts.addJuros()

print(savings_accounts.saldo)


