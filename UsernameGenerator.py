'''
This program generates prompts the user to enter their first name, last name and student ID from theri
if takes the first three letters of the first name (or if it is less than three letters long than it uses the full
first name, then it takes the first three letters of the last name (if the last name is shorter than three letters it uses all
of the last name, and it takes the last three characters of the student ID (if it is shorther than 3 letters then if uses all of the ID)
and concatenates them together to generate a user name. It then prompts the user to enter a password and ensures the password meets the criteria.
The criteria for the password is that it must have a lowercase letter, an uppercase letter and a number.
'''

def main():
    first_name = input("Enter first name: ")    #Prompts the user to enter their first name.
    
    last_name = input("Enter last name: ")      #Prompts the user to enter their last name.
    
    ID_num = input("Enter ID: ")    #Prompts the user to enter the user to enter their Student ID
    
    print("Your user name is", get_login_name(first_name, last_name, ID_num))    #Calls the get_login_name function and prints out the returned result.
    
    password_check = True   #boolean for a while loop check.
    
    while password_check:   #while loop which keeps repeating until password requirements are met. 
        
        password = input("Write a password below, it must be seven characters in length and have one uppercase, one lowercase and one digit") #Prompts user to enter desired password.
        
        if(any(x.isupper() for x in password) and any(x.islower() for x in password) and any(x.isdigit() for x in password) and len(password) >= 7): #Ensures password meets criteria, prompts user to enter password again if it does not.
            
            password_check = False  #If password meets criteria, it exits out of the loop.
            
            print("Password set")   #Lets the user know that the password has been set.
        else:
            
            print("Password did not meet requirements, try again")  #Lets user know to try again.
    
def get_login_name(first, last, ID):    #This method accepts the first name, last name and student ID and creates the username. 
    
    if len(first)>=3:   #Confirms whether it is greater than or equal to three characters.
        
        first = first[0:3]  #Stores the first three letters of first in the variable first.
    
    if len(last)>=3:    #Confirms whether it is greater than or equal to three characters.
        
        last = last[0:3]    #Stores the first three letters of last in the variable last.
    
    if len(last)>=3:
        
        ID = ID[-3:]    #Confirms whether it is greater than or equal to three characters.
    
    return first + last + ID    #Returns the results as a concatenation.

main()  #Executes starting from the main method.
