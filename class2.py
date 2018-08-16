class Employee:
  'Common base class for all employees'
  empCount = 0
  def __init__(num,name, salary):
          num.new = name
          num.new2 = salary
          Employee.empCount =Employee.empCount+ 1
  def display(num):
            print "Total Employee %d" % Employee.empCount
  def displayEmployee(num):
            print "Name : ", num.new, ", Salary: ",num.new2
            "This would create first object of Employee class"
emp1 = Employee("Zara", 2000)
"This would create second object of Employee class"
emp2 = Employee("Manni", 5000)
emp1.displayEmployee()
emp2.displayEmployee()
print "Total Employee %d" % Employee.empCount
