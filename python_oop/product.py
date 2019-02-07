class Product:
  # this is for the sensei bonus
  current_id = 1

  def __init__(self, name, price, category):
    self.name = name
    self.price = price
    self.category = category

    # we're using an attribute that exists on the class as a whole, not on each instance
    self.id = Product.current_id
    Product.current_id += 1

  def update_price(self, percent_change, is_increased):
    if is_increased:
      self.price += self.price * percent_change
    else:
      self.price -= self.price * percent_change
    return self

  def print_info(self):
    print(f"Name: {self.name}, Category: {self.category}, Price: ${self.price}")
    return self