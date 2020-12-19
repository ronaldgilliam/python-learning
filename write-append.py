#example of using a reading, writing and ammending files; add a new lime with \n
employee_file = open("employees.txt", "r")

employee_file.write("Toby - HR")

employee_file.write("\nKelly - Customer Service")

employee_file.close()