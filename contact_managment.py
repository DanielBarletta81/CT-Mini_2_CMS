
#Editing an existing contact's information (name, phone number, email, etc.).
#Deleting a contact by searching for their unique identifier.

#Searching for a contact by their unique identifier and displaying their details.
#Displaying a list of all contacts with their unique identifiers.
#Exporting contacts to a text file in a structured format.
#Importing contacts from a text file and adding them to the system. * BONUS

contact_information = {
     4019198881:{"name": "Daniel", "phone": 4019198881, "email": "dswanson18@gmail.com", "city": "Warwick"},
     4012223200: {"name": "Doug", "phone": 4012223200, "email": "ddiggins88@gmail.com", "city": "Providence"},
     4014199133: {"name": "Christie", "phone": 4014199133, "email": "cmajor890@gmail.com", "city": "Attleboro"}
     }

#Good
def add_contact():
     add_name = input("Enter contact name: ")
     add_phone = int(input("Enter contact phone #: "))
     add_email = input("Enter contact email: ")
     add_city = input("Enter contact location (city): ")

     new_contact = {"name": add_name,  "phone": add_phone, "email": add_email, "city": add_city}
     contact_information[add_phone] = new_contact
     print(f'New contact added: {new_contact}')

# In Progress
def edit_contact():
     identifier_phone = int(input("Enter the phone number for the contact you wish to edit. "))
     updated_field = input("Which would you like to update? (name/phone/email/city)")

     if updated_field == "name":
         update_name = input(f'Enter the name you want on this account. ')
         contact_information[identifier_phone].update({"name": update_name})
         print(f'\n Contact {updated_field}, has been updated to : {update_name}')
         print(f'\n Contact details after update:')
         for field, value in contact_information[identifier_phone].items():
            print(f'{field.capitalize()} : {value}')

     elif updated_field == "phone":
         update_phone = input(f'Enter the phone number you want on this account. ')
         contact_information[identifier_phone].update({"phone": update_phone})
         print(f'Contact {updated_field}, has been updated to : {update_phone}')
         print(f'\n Contact details after update:')
         for field, value in contact_information[identifier_phone].items():
            print(f'{field.capitalize()} : {value}')

     elif updated_field == "email":
         update_email = input(f'Enter the email you want on this account. ')
         contact_information[identifier_phone].update({"email": update_email})
         print(f'Contact {updated_field}, has been updated to : {update_email}')
         print(f'\n Contact details after update:')
         for field, value in contact_information[identifier_phone].items():
            print(f'{field.capitalize()} : {value}')

     elif updated_field == "city":
         update_city = input(f'Enter the city you want on this account. ')
         contact_information[identifier_phone].update({"city": update_city})
         print(f'Contact {updated_field}, has been updated to : {update_city}')
         print(f'\n Contact details after update:')
         for field, value in contact_information[identifier_phone].items():
            print(f'{field.capitalize()} : {value}')

     else:
         print("Please enter a valid field.")

     

#Good
def delete_contact():
    identifier_phone = int(input("Enter the phone number for the contact you wish to delete. "))
    del contact_information[identifier_phone]
    print(f'Contact: {identifier_phone} , has been deleted.')
    print(contact_information)
#In Progress
def search_contacts():
     identifier_phone = int(input("Enter the phone number for the contact you wish to locate. "))
     if identifier_phone in contact_information:
         print(f'\n Contact details for contact id: {identifier_phone} : {contact_information[identifier_phone]}', sep="\n")
#Good
def display_contacts():
     for contact_id, info in contact_information.items():
        print("\n Contact ID:", contact_id)
        for key in info:
            print(key + ':', info[key])
     
#Not Started
def export_contacts():
     #send contacts to text file
     pass
#Not Started
def import_contacts():
     #read contacts from a text file
     pass




def contact_management():
    try:
        while True:
            print('*** Welcome to the Contact Management System!! ***')
            print('Menu:')
            print("1. Add new contact")
            print("2. Edit a contact")
            print("3. Delete a contact")
            print("4. Search for contact")
            print("5. Display all contacts")
            print("6. Export contacts to text file")
            print("7. Import contacts from text file")
            print("8. Quit")

            selection = int(input("Please make a selection (1-8). "))

            if selection == 1:
                add_contact()

            elif selection == 2:
                edit_contact()

            elif selection == 3:
                delete_contact()

            elif selection == 4:
                search_contacts()

            elif selection == 5:
                display_contacts()

            elif selection == 6:
                 pass

            elif selection == 7:
                 pass

            elif selection == 8:
                print("Thank you for using the contact management system today!")
                break
    
            else:
                print("Please make a valid selection.")

    except ValueError:
        print(ValueError , "Please enter a valid selection, numbers only.")
        if ValueError:
             contact_management()  


contact_management()