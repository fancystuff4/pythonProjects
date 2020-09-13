# employee salary

class employee:
  def __init__(self, basic_salary=500):
    self.basic_salary= basic_salary

class chef(employee):
  def __init__(self, hourly_wages ,hours , days):
    super().__init__(550)
    self.hourly_wages= hourly_wages
    self.hours = hours
    self.days=days
  def get_monthly_salary(self):
    return self.basic_salary+(self.hourly_wages*self.hours*self.days)

class waiter(employee):
  def __init__(self, monthly_salary ,tips):
    super().__init__(600)
    self.monthly_salary=monthly_salary
    self.tips = tips
  def get_monthly_salary(self):
    return self.basic_salary+(self.tips*0.5+self.monthly_salary)

class cleaner(employee):
  def __init__(self, monthly_salary ,extra_hours , extra_salary):
    super().__init__()
    self.monthly_salary= monthly_salary
    self.extra_hours = extra_hours
    self.extra_salary=extra_salary
  def get_monthly_salary(self):
    return self.monthly_salary+self.basic_salary+(self.extra_hours*self.extra_salary)

peter = chef(20,8,26)
peter_salary=peter.get_monthly_salary()
print(peter_salary)

gary = waiter(3000, 200)
gary_salary=gary.get_monthly_salary()
print(gary_salary)

michael= cleaner(3500,15,20)
michael_salary=michael.get_monthly_salary()
print(michael_salary)

income= 20000
profit= income-(peter_salary+gary_salary+michael_salary)
print(profit)