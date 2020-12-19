#example of using a read commant to grab info from files
employee_file = open("employees.txt", "r+")
#r=read; w=write; r+=read/write
for employee in employee_file.readlines():
    print(employee)

employee_file.close()
