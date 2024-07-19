#Implement the following actions in response to menu selections:
#Adding a new contact with all relevant details.
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

def add_contact():
     add_name = input("Enter contact name: ")
     add_phone = input("Enter contact phone #: ")
     add_email = input("Enter contact email: ")
     add_city = input("Enter contact location (city): ")

     new_contact = {"name": add_name,  "phone": add_phone, "email": add_email, "city": add_city}
     contact_information[add_phone] = new_contact
     print(f'New contact added: {new_contact}')


def edit_contact():
     identifier_phone = int(input("Enter the phone number for the contact you wish to edit. "))
     updated_field = input("Which would you like to update? (name/phone/email/city)")

     if updated_field == "name":
         update_name = input(f'Enter the name you want on this account. ')
         contact_information[identifier_phone].update({"name": update_name})

     elif updated_field == "phone":
         update_phone = input(f'Enter the phone number you want on this account. ')
         contact_information[identifier_phone].update({"phone": update_phone})

     elif updated_field == "email":
         update_email = input(f'Enter the email you want on this account. ')
         contact_information[identifier_phone].update({"email": update_email})

     elif updated_field == "city":
         update_city = input(f'Enter the city you want on this account. ')
         contact_information[identifier_phone].update({"city": update_city})

     else:
         print("Please enter a valid field.")

     


def delete_contact():
    identifier_phone = int(input("Enter the phone number for the contact you wish to delete. "))
    del contact_information[identifier_phone]
    print(f'Contact: {identifier_phone} , has been deleted.')
    print(contact_information)

def search_contacts():
     pass

def display_contacts():
     print(contact_information)

def export_contacts():
     pass

def import_contacts():
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