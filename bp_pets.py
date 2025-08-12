from models import Pets, session

#view pets function
#Takes in current user
#Loops over all of the current users pets (use the .pets relationship attribute to get list of pets)
#prints the pets info
def view_pets(current_user):
    print("-------My Pets--------")
    for pet in current_user.pets:
        pet.display()
        

#Create pets function
#gets pets info from user
#create Pets() from the info
#print new pet
def create_pet(current_user):
    name = input("Pet name: ")
    species = input("Species: ")
    breed = input("Breed: ")
    age = int(input("Age: ")) #Automatically gets converted to int by my model

    new_pet = Pets(name=name, species=species,breed=breed,age=age, owner_id=current_user.id)
    session.add(new_pet)
    session.commit()
    print("Pet Profile successfully created!")



#Update pets function
#display current users pets
#allow them to select a pet BY NAME
#query that pet from the database
#get updated info from the user
#set that pets info to the new info
#commit changes
#print new pet info
def update_pet(current_user):
    view_pets(current_user) #Calling my view_pets function to show all pets
    choice = input("Enter name of pet to update: ")

    pet = session.query(Pets).where(Pets.name.ilike(choice), Pets.owner_id==current_user.id).first() #Searching for a pet that has the given
    if pet:
        print("To keep information leave fields blank.")
        name = input("Pet name: ")
        species = input("Species: ")
        breed = input("Breed: ")
        age = input("Age: ")
        if name:
            pet.name = name
        if species:
            pet.species = species
        if breed:
            pet.breed = breed
        if age:
            pet.age = age
        session.commit()
        print("-------Updated Pet-------")
        pet.display()
    else:
        print("Invalid pet selection")



#Delete pets function
#display current users pets
#allow them to select a pet BY NAME
#query that pet from the database
#Ask user if they are sure they want to delete this pet
#delete pet from the session
#commit changes
def delete_pet(current_user):
    view_pets(current_user)

    choice = input("Enter pet's name you wish to delete: ")
    pet = session.query(Pets).where(Pets.name.ilike(choice), Pets.owner_id==current_user.id).first() #Searching for a pet that has the given
            #- ilike allows you to query strings case insensitive rHiA == Rhia
            # can have multiple conditions, must separate with a ','
    if pet:
        confirm = input("Confirm you want to delete this pet by typing 'delete': ")
        if confirm == 'delete':
            session.delete(pet)
            session.commit()
            print("Successfully delete this pet.")
    else:
        print("Invalid pet option.")





