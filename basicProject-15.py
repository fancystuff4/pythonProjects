# engineer project

class engineer:
  def __init__(self, license_no):
    self.license_no= license_no
  def design_project(self):
    print("i am designing a project")
class seniorengineer(engineer):
  def __init__(self, license_no, num_project):
    super().__init__(license_no)
    self.num_project=num_project
  def deal_project(self):
    print(" I have got a project to do ")
    self.num_project+=1
class seniorcomputerengineer(seniorengineer):
  def __init__(self, license_no, num_project, current_project):
    super().__init__(license_no, num_project )
    self.current_project=current_project

harsh= engineer("84703")
harsh.design_project()

kapil = seniorengineer("35335", 3)
kapil.deal_project()
print("now kapil is working on "+str(kapil.num_project)+" projects")

kiran= seniorcomputerengineer("3678", 4, "networking")
print(kiran.num_project)
print(kiran.current_project)