class BankAccount:
  def __init__(self, interest_rate, balance=0):
    self.interest_rate = interest_rate
    self.balance = balance

  def deposit(self, amount):
    self.balance += amount
    return self

  def withdraw(self, amount):
    if self.balance > amount:
      self.balance -= amount
    else:
      print("Insufficient funds: Charging a $5 fee")
      self.balance -= 5
    return self

  def display_account_info(self):
    print(f"Balance: ${self.balance}")
    return self

  def yield_interest(self):
    if self.balance > 0:
      self.balance += self.balance * self.interest_rate
    return self

# I did my own testing rather than working form the platform directions
ba = BankAccount(0.05)
other = BankAccount(0.01, 100)

ba.deposit(100).withdraw(200).display_account_info().yield_interest().display_account_info()

other.withdraw(50).display_account_info()