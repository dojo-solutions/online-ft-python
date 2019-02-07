class User:
  def __init__(self, name, email):
    self.name = name
    self.email = email
    self.account_balance = 0

  def make_deposit(self, amount):
    self.account_balance += amount

  def make_withdrawal(self, amount):
    self.account_balance -= amount

  def display_user_balance(self):
    print(f"User: {self.name}, Balance: ${self.account_balance}")
  
  def transfer_money(self, other_user, amount):
    self.account_balance -= amount
    other_user.account_balance += amount

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