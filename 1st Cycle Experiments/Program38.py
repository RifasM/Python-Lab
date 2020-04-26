"""
An organization has decided to provide salary hike to its employees based on their job level.
Employees can be in job levels 3, 4 or 5. Hike percentage based on job levels are given below:
Job level	Hike Percentage (applicable on current salary)
    3	            15
    4	            7
    5	            5
In case of invalid job level, consider hike percentage to be 0.
Given the current salary and job level, write a python program to find and display the new salary of an employee.
"""

job = {
    3: 15,
    4: 7,
    5: 5
}

lev, sal = map(int, input("Enter Job level and Salary: ").split())

hike = 0
if lev in job.keys():
    hike = job[lev]

print("Salary hike = ", hike, "%")
print("New Salary = ", sal*(hike/100)+sal)

"""
OUTPUT
    Enter Job level and Salary: 3 1000
    Salary hike =  15 %
    New Salary =  1150.0
    
    Enter Job level and Salary: 8 2000
    Salary hike =  0 %
    New Salary =  2000.0
"""