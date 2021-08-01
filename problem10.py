
''' 
    Name : AbdElrahman Ibrahim Zaki 
    Task : Assignment 1 
    email : abdelrahmanzaki.aez@gmail.com  
'''

''' ---------------------------------------------------------------------------------------------------------------------------------- '''
''' 
    10- Ask the user for his name then confirm that he has entered his name 
    (not an empty string/integers). then proceed to ask him for his email and print all this data
'''
name = input("Please enter your name: ")
while(name == ""):
    print("Invalid input")
    name = input("Please enter your name: ")

email = input("Please enter your email: ")
while(email == ""):
    print("Invalid input")
    email = input("Please enter your email: ")

print("Your name is: %s\nYour email is: %s" %(name, email))
    
