class Store:
  def __init__(self, name):
    self.name = name
    self.products = []
  
  def add_product(self, new_product):
    self.products.append(new_product)
    return self

  def sell_product(self, id):
    self.products.pop(id).print_info()
    return self

  # this version is for the sensei bonus
  # def sell_product(self, id):
  #   # we need the index number so we can pop it directly from there (handy that python includes that)
  #   for i in range(len(self.products)):
  #     if self.products[i].id == id:
  #       self.products.pop(i).print_info()
  #   return self

  def inflation(self, percent_increase):
    for product in self.products:
      product.update_price(percent_increase, True)
    return self

  def set_clearance(self, category, percent_discount):
    for product in self.products:
      if product.category == category:
        product.update_price(percent_discount, False)