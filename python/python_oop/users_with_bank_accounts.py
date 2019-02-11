from bank_account import BankAccount

class User:
  def __init__(self, name, email):
    self.name = name
    self.email = email
    self.primary_account = BankAccount(0.02)
    self.other_accounts = []

  def make_deposit(self, amount, account=None):
    if account == None:
      account = self.primary_account
    account.deposit(amount)

  def make_withdrawal(self, amount, account=None):
    if account == None:
      account = self.primary_account
    account.withdraw(amount)

  def display_user_balance(self, account=None):
    if account == None:
      account = self.primary_account
    print(f"User: {self.name}, Balance: ${account.balance}")

  def transfer_money(self, other_user, amount, user_account=None, other_account=None):
    if user_account == None:
      account = self.primary_account

    if other_account == None:
      other_account = other_user.primary_account

    account.withdraw(amount)
    other_account.deposit(amount)


# I did my own testing rather than following the instructions on platform
wes = User("Wes", "wharper@codingdojo.com")
jenny = User("Jenny", "fake@fake.com")

wes.make_deposit(1000)
jenny.make_deposit(1000)

wes.make_withdrawal(250)
wes.display_user_balance()

jenny.transfer_money(wes, 100)
jenny.display_user_balance()
wes.display_user_balance()
