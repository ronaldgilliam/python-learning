
# character_name = "Akram"
# character_age = 50
# is_male = True
# print("There once was a man named " + character_name + ", ")
# print("he was " + character_age + " years old.  ")

# character_name = "Mike"
# print("He really liked the name " + character_name + ",  ")
# print("but didn't like being " + character_age + ".")


#num1 = input("Enter a number: ")
#num2 = input("Enter another number: ")
#result = float(num1) + float(num2)

#print(result)

# Stopped at 58:25 / 4:36:52

#color = input("Enter a color: ")
#plural_noun = input("Enter a plural noun: ")
#celebrity = input("Enter a celebrity: ")

#print ("Roses are " + color)
#print (plural_noun + " are blue")
#print ("I love " +celebrity)

#lucky_numbers = [4, 20, 8, 15, 16, 23, 42]
#friends = ["Kevin", "Karen", "Jim", "Oscar", "Tony"]
#friends2 = friends.copy()

#lucky_numbers.sort()
#print(lucky_numbers)

#coordinates = (4, 5)
#coordinates[1] = 10
#print(coordinates[0])

#def say_hi(name, age):
 #   print("Hello " + name + ", you are" + age)

#name = input ("Enter your name:")
#age = input ("Enter your age:")

#say_hi()

#def cube(num):
 #   return num*num*num

#result = cube(4)
#print(result)

#is_male = False
#is_tall = False

#if is_male and is_tall:
#    print("You are a tall male")
#elif is_male and not(is_tall):
#    print("You are a short male")
#elif not(is_male) and is_tall:
#    print("You are not a male but are tall")
#else:
 #   print("You are either not male or not tall or both")

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


print(max_num(3, 4, 5))