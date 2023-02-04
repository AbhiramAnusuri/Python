import json
class Employee:
  def __init__(self, name, dob, height, city, state):
    self.name = name
    self.dob = dob
    self.height = height
    self.city = city
    self.state = state
  
  def __repr__(self):
    return f"Name: {self.name}\nDOB: {self.dob}\nHeight: {self.height}\nCity: {self.city}\nState: {self.state}"
    
with open("employee.json", "r") as file:
  employee_data = json.load(file)
  employees = []
  for employee in employee_data:
    employees.append(Employee(employee["Name"], employee["DOB"], employee["Height"], employee["City"], employee["State"]))
print(employees)