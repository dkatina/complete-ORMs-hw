from models import Owners, session

#View profile function
#displays the current users info
def view_owner(current_user):
    current_user.display()
    


#Update profile function
#dsiplays current user info
#allows user to update any of the fields
#commits changes 
#shows changes and returns update current_user
def update_owner(current_user):
    current_user.display()
    print("Fill in desired changes, to keep current values leave blank")
    name = input("Name: ")
    email = ''
    while True:
        email = input("Email: ") #Continuously ask the user for an email until theygive you one that is not taken
        taken_user = session.query(Owners).where(Owners.email==email).first()
        if taken_user:
            print("This email is taken.")
            continue
        break
    password = input("Password: ")
    phone = input("Phone: ")
    if name:
        current_user.name = name
    if email:
        current_user.email = email #Could pose a problem, what if they change their email to a taken.
    if password:
        current_user.password = password
    if phone:
        current_user.phone = phone
    session.commit() #Commiting changes to the db
    print("---------Update Info-----------")
    current_user.display()
    return current_user

#Delete profile function
#Ask user to confirm they want to delete
#if so delete the current user from the session
#commits changes 
#call main() to start the program over

def delete_owner(current_user):
    choice = input("To confim you want to delete you account type 'delete': ")
    if choice == 'delete':
        session.delete(current_user)
        session.commit()
    else:
        print("Opted out, back to menu.")