# name = input("Please enter your name: ").strip()
# age = int(input("Please enter your age: "))
# email = input("Please enter your email: ").strip()
# city = input("Plase enter your city name: ").strip()
# school_name = input("Please enter your school name: ").strip()
# cgpa = float(input("Please enter your cgpa: "))

# print("Name: " + name)
# print("Age: " + str(age))
# print("Email: " + email)
# print("City" + city)
# print("School Name: " + school_name)
# print("CGPA: " + str(cgpa))

# print(name + "\n" + str(age) + "\n" + email + "\n" + city + "\n" + school_name + "\n" + str(cgpa))

# text = " My name is Blue"

# text = text.upper()
# print(text)

# text = text.lower()

# print(text)

# print(len(text))

# para = "This is paragraph for searching or to find any word within this para"
# word_looking_for = "find"
# reslt = str(para.find(word_looking_for))

# if reslt != "-1":
#     print("Great the word is found at the posotion of " + reslt)
# else:
#     print("Word not found " + reslt)

# print(para.startswith(word_looking_for))

# print(para.endswith(word_looking_for))

# sp = "Hello, My, name"
# seperator = "_"

# splt = sp.split(seperator)
# print(splt)

# date = ["2026", "1", "9"]

# jn = "-".join(date)
# print(jn)



# data = "2026/01/08"
# separator = "/"

# parts = data.split(separator)
# print(parts)

# joiner = "/"

# joint = joiner.join(parts)
# print(joint)


# para = "Hello find me in this paragraph"
# word = "find"

# if word != "-1":
#     print("word found " + word)
#     para = para.replace(word, "Finder")
# else:
#     print("word not found")
        
# print(para)

# text = "Test text"

# print(f"{text} emmbed me please")


# userid = 101

# user_id = str(userid)
# print("User ID: " + user_id)

# roll_number = int(input("Enter your roll No please"))

# print(roll_number)

# print(type(roll_number))

# #type casting

# float_roll_no = float(roll_number)

# print(float_roll_no)
# print(type(float_roll_no))


# first_name = input("Enter your First Name please: ").strip()

# last_name = input("Enter your last Name  please: ").strip()

# first_name = first_name.capitalize()
# last_name = last_name.capitalize()

# first_name = first_name.title()
# last_name = last_name.title()

# print(first_name + " " + last_name)


# mylist = "apple"
# print(type(mylist))
# mylist = mylist.upper()

# separator = "   "

# new_mylist = separator.join(mylist)
# print(new_mylist)

# date = "2022", "23" , "12"
# sep = "/"
# date = sep.join(date)
# print(date)

# password = "Amnao42345"
# password_len = len(password)

# print(password_len)

# print(password[0])
# print(password[-3])

# mydate = "2026/01/10"
# my_date = mydate[0:4]

# print(my_date)

# text = "This is a string to find a word"

# word = "me"

# result = text.find(word)

# print(type(result))

# if result != -1:
#     text = text.replace(word, "Found")
#     print(text)
# else:
#     print("Word not found please")
    
    
    
# indexing = text.count("is")

# print(indexing)

# # print(text.startswith("This"))
# # print(text.endswith("word"))

# text = "this is text"
# space = " "
# print(text.isalpha())

# print(text.isalnum())

# print(text.isdecimal())

# print(text.isdigit())

# print(space.isspace())


# text = "apple, orange, mango"

# print(type(text))
# print(text)

# text_split = text.split(",")
# print(text_split)

# print(type(text_split))

# path = "/home/user/file.txt"
# file_name = path.rsplit("/", 1)[1]

# print(file_name)

# file_exten ="check.pdf"
# check_exten = file_exten.rsplit(".", 1)[1]

# print(check_exten)

# text = "line1\nline2\n ted"
# lines = text.splitlines()
# print(lines)
# print(type(lines))

# data = "tech world"

# # data_enco = data.encode("utf-8")

# # print(data_enco)

# # deco = data_enco.decode("utf-8")
# # print(deco)


# text = "End"

# print(text.zfill(7))

# email = "user@mail.com"
# user, symb, domain = email.partition("@")

# print(user + "\n" + symb + "\n" + domain)

# url = "https//:www.com"

# pref = url.removesuffix(".com")

# print(pref)

# print( 9 // 2)


# myList = [1, 2, 3,7, 9, 4, 5, 6]
# myList1 = ["One", "Two", "Three", "Four", "Five"]

# for item in myList:
#     print(item) 
    
# for item in range(len(myList)):
#     print(myList[item])
    
# print(myList[0])

# print(myList[-1])

# myList.append("World")
# print(myList[-1])
# myList.remove("World")
# print(myList)

# print(len(myList))

# myList.sort()

# print(myList)

# myList.reverse()

# myList.insert(0, "Testing")

# myList.extend(myList1)

# myList1 [0:3] = "Banana", "Apple"

# myList1.pop(2)       # Delete Specific element
# del myList1[0]       # Delete Specific element
# del myList1          # Delet entire list

# myList1.clear()      # List exist but element not exist


# print(myList1)

# for x in myList1:
#     print(x)
    
# for x in range(len(myList1)):
#     print(myList1[x])

# i = 0
# while i < len(myList1):
#     print(myList1[i])
#     i = i + 1 

# [print(x) for x in myList1]

# for x in myList1:
#     print(x)

# for x in range(len(myList1)):
#     print(myList1[x])

# i = 0

# while i < len(myList1):
#     print(str(i) + " " + myList1[i])
#     i += 1

# new_word = "o"
# newlist =[]

# for x in myList1:
#     if new_word in x:
#         newlist.append(x)
        
# print(newlist)


# fruits = ["Banana", "apple", "Orange", "Mango", "cherry", "Green", "Blue", "red"]

# newlist = [x for x in fruits if "a" in x ]

# print(newlist)

# fruits.sort(key = str.lower)
# print(fruits)
# fruits.sort(reverse = True)
# print(fruits)

# fruits.reverse()
# print(fruits)

# -------- Copy List -------
# myfru = fruits.copy()
# myfru = list(fruits)
# myfru = fruits[:]

# print(myfru)

# ------- Join two Lists -------
# vag = ["ptato", "red chili", "black paper"]

# newlist = fruits + vag
# print(newlist)

# fruits.extend(vag)
# print(fruits)

# for x in fruits:
#     vag.append(x)  
# print(vag)

# Count the numbers value appear 
# print(fruits.count("apple"))


# tup = ("Banana", "Apple", "Orange")
# print(tup)


# for x in range(len(tup)):
#     print(str(x) , tup[x])
    
# print(type(tup))

# my_tup = tuple(("One", 3, "Two", False , "Three"))

# print(my_tup)

# t = (6, 4, 5, 9, "Last")
# l = list(t)
# print(l)
# l.append("First")
# print(l)

# t = tuple(l)
# print(t)

# tup = ("Banana", "Apple", "Orange", "Green", "Yellow")

# (one, two, *three) = tup
# print(one)

# print(three)

# i = 0
# while i < len(tup):
#     print(str(i) + " " + tup[i])
    
#     i += 1

# tup1 = (1, 2, 3, 4, 2)

# tup1 = tup1 * 2

# print(tup1)

# print(tup1.count(2))

# s = {"Banana", "Apple", "Orange"}
# print(type(s))

# print("Hello world world")


# products = []


# while True:
    
#     print("1. To Add Product ")
#     print("2. To View Products ")
#     print("3. To Exit Program ")
    
#     chos_num = input("Enter number please: ")
    
#     if chos_num == "1":
#         name = input("Enter product name: ")
#         price = float(input("Enter product price: "))
#         category = input("Enter product category: ")
        
#         products.append([name, price, category])
#         print("\nProduct is added !\n")
        
#     elif chos_num == "2":
#         if len(products) == 0:
#             print("There is no product available")
#         else:
#             print("\nYour Products")
            
#             for i in products:
#                 print("Name: " , i[0])
#                 print("Price: ", i[1])
#                 print("Category: ", i[2])
#                 print("--------")
                
#     elif chos_num == "3":
#         print("Thank for Adding products Program is exited")
#         break
# else:
#     print("Invalid number")
      
      
# Mini project to add items in cart            
        
# cart = []

# while True:
    
#     print("Press 1 to product in cart: ")
#     print("press 2 to view cart and total amount: ")
#     print("Press 3 to exit program: ")
    
#     choice = input("Please enter Number 1 to 3:")
    
#     if choice == "1":
      
#       name = input("Enter name of the product: ")
#       price = float(input("Enter price of the product: "))
#       cart.append([name, price])
#       if len(cart) == 0:
#         print("Product is not added in cart ! ")
    
#       else:
      
#         print("\nItem is added in cart successfully: ")
      
#     elif choice == "2":
#         if len(cart) == 0:
            
#             print("There no product in the cart")
        
#         else:
#             total = 0

#             print("-----------------------------------")
#             print(f"{'Product Name':<20} {'Price':>10}")
#             print("-----------------------------------")

#             for item in cart:
#                 print(f"{item[0]:<20} {item[1]:>10}") #<20 → Left align with width 20 >10 → Right align with width 10
#                 total += item[1]

#             print("-----------------------------------")
#             print(f"{'Total amount':<20} {total:>10}")

#     elif choice == "3":
        
#         print("Thank you for Shopping: ")
#         break
#     else:
#         print("-------------------------")
#         print("invalid Number")        
#         print("-------------------------")
                
        
            
            
# Mini project of sudents where we will achive the following goals:
# 1 Add new student
# 2 View all students
# 3 Update student marks
# 4 Delete student
# 5 Search student
# 6 Exit

# we will create list of student where we will add students as lists of list
# Sudents has rollNomuber name and marks 

# student = []

# while True:
    
#     print("\nPress 1 to add new student ")
#     print("Press 2 to view all students ")
#     print("Press 3 to Update student Marks ")
#     print("Press 4 to delete student ")
#     print("Press 5 to search student ")
#     print("Pres 6 to exist")
    
#     choice = input("Plesase Enter number 1 to 6: ")
    
#     # add new student
#     if choice == "1":
#         roll_no = input("Enter Roll No: ")
#         name = input("Enter Name: ")
#         marks = float(input("Enter student marks: "))
        
#         student.append([roll_no, name, marks])
        
#         if len(student) == 0:
#             print("Ops Student is not added !")
#         else:
#             print("Student is added successfully ")
      
#     # View all sudents        
#     elif choice == "2":
        
#         if len(student) == 0:
#             print("Student list is empty")
#         else:
#             print("\nRoll No    Name           Marks")
#             print("---------------------------------")
#             for s in student:
#                 print(f"{s[0]:<8} {s[1]:<20} {s[2]:>5}")
        
#     # Update student marks
#     elif choice == "3":

#         roll = input("Please enter roll Number to update marks: ")
#         found = False
        
#         for i in student:
#             if i[0] == roll:
#                 i[2] = input("Please enter new marks: ")
#                 print("Marks updated successfully ")
#                 found = True
#                 break
#             if not found:
#                 print("Student not found. ")
        
#         # Delete student        
#     elif choice == "4":
            
#         roll = input("Please enter student Roll No that you want to remove or delete ")
#         for i in student:
#             if i[0] == roll:
#                 student.remove(i)
#                 print("Student removed successfully ")
#                 break
#             else:
#                 print("Student no found. ")
                
#         # Search Student
#     elif choice == "5":
            
#             roll =  input("Please enter student Roll No to search ")
            
#             for i in student:
#                 if i[0] == roll:
#                     print("Student found: ")
#                     print(f"Roll No: {i[0]}, Name: {i[1]}, Marks: {i[2]}")
#                     break
#                 else:
#                     print("Student not found. ")  
            
#         # Exit
#     elif choice == "6":
#         print("Thank You")
#         break
#     else:
#         print("Invalid Number ")
            

# tuple in python
# tuple is immutable(can not be changed) while list element can be changed(mutable)
# tuple has few funtions while list has many functions
# tuple faster and use less memory as compared to list
#  tuple can be dictionary key because element are immuatable

order1 = (101, "Usman", "Laptop", 1, 800)
order2 = (102, "Ali", "Iphone", 2, 600)
order3 = (103, "Majid", "Handfree", 3, 300)
order4 = (104, "Amjad", "Moble", 2, 500)

orders = [order1, order2, order3, order4]

# for order in orders:
#     print(f"Order Id: {order[0]}")
#     print(f"Customer Name: {order[1]}")
#     print(f"Product: {order[2]}")
#     print(f"Qty: {order[3]}")
#     print(f"Price: {order[4]}")


# this for loop is tuple unpacking concept where each element in a tuple is assigned to an each element like order_id, customer, product etc.

# for order_id, customer, product, qty, price in orders:
#     total = qty * price
#     print(f"Customer {customer} Ordered: {product}, Qty: {qty}, unit price: {price}")
#     print(f"Total Bill PKR {total}")
#     print("-" * 50)
    

# Set

# A = {1,2,3,4}
# B = {5,6,7,8}

# print(A ^ B)

# Dictionary

# student = {
    
#     "name": "Kamal",
#     "age": 20,
#     "Deg": "MS (SE)"
# }

# for key in student:
#     print(key)

# a mini project using dictionary where we will achive following goals 
# declear empty dictioary
# press 1 to add new student (id, name, age, subject, score, city)
# presss 2 to view all students
# press 3 to search a student by id and name
# press 4 to update name, age and city of student
# persss 5 delete a student
# press 6 to exit program


# students = []

# while True:
    
#     print("Press 1 to add new student: ")
#     print("Press 2 to view all students: ")
#     print("Press 3 to search a student weather by id or by name: ")
#     print("Press 4 to update name, age and city of a student: ")
#     print("Press 5 to delete or remove a student: ")
#     print("Press 6 to exit program: ")
    
#     choice = input("\nPlease enter 1 to 6 number:")
    
#     if choice == "1":
#         id = int(input("Please enter student Id: "))
#         name = input("Please enter student name: ")
#         age = int(input("please enter student age: "))
#         subject = input("Please enter subject name: ")
#         score = float(input("Plase enter subject score: "))
#         city = input("Please enter city name of student: ")
        
#         students.append({
#             "id": id,
#             "name": name,
#             "age": age,
#             "subject": subject,
#             "score": score,
#             "city": city
#         })
#         if len(students) == 0:
#             print("Ops data is not submitted ! someting wrong")
#         else:
#             print("\nData is submitted successfully: \n")
    
#     if choice == "2":
#         if len(students) == 0:
#             print("There student List it empty: ") 
#             print("-" * 30)      
#         else:
#             for student in students:
#                 for key, value in student.items():
#                     print(f"{key} : {value}")
#                 print("-" * 30)
        
             
#     if choice == "3":
        
#         search = input("Please enter id or name of student: ")
#         for student in students:
#             if (search.isdigit() and student["id"] == int(search)) or student["name"] == search:
#                 print(f"Student is found: {student}")
#                 break
        
#     if choice == "4":
        
#         update_s = input("please enter student name or id that your want to update: ")
#         found = False
#         for stu in students:
#             if (update_s.isdigit() and stu["id"] == int(update_s)) or stu["name"] == update_s:
                
#                 stu["name"] = input("Please enter student name: ")
#                 stu["age"] = int(input("please enter student age: "))
#                 stu["city"] = input("Please enter sutdent's city name: ")
                
#                 print("\nStudent record is updated successfully: \n")
#                 found = True
#                 break
            
#         if not found:
#             print("Record not found: ")
            
    
#     if choice == "5":
        
#         delete_s = input("Please enter student name or id that you want to remove: ")
        
#         for stud in students:
#             if (delete_s.isdigit() and stud["id"] == int(delete_s)) or stud["name"].lower() == delete_s.lower():
#                 students.remove(stud)
#                 print("\nStudent is removed successfully: \n")
#                 break
    
#     if choice == "6":
#         print("Thank you program is exited !")
#         break
# else:
#     print("Invalid Number: ")   
   

# def myfn(name = "Defualt Name"):
    
#     print(name)
    
    
# myfn()

# def myfucntion(*name):
#     print(name + " Hello")
    
# myfucntion("Shakeel Raza", " Sandhu")

# name  = "shakeel raza sandhu sab"

# print(name.title())
