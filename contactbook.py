
import os
print(os.getcwd())
contacts = []

# try: this was a mistake cuz i need name and phone
#     with open("ContactDetails.txt","r") as file:
#        contacts= file.read().splitlines()
# except FileNotFoundError:
#     pass

try:
    with open("ContactDetails.txt", "r") as file:
        for line in file:
            name, phone = line.strip().split(",")
            contacts.append([name, phone])
except FileNotFoundError:
    pass

        
while True:


        print("\nWelcome to the contacts menu \n")
        print("1. Add new contact")
        print("2. View saved contacts")
        print("3. Delete existing contact")
        print("4. Exit ")
        print("5. Search existing contact \n")


        try:
            choice = int(input("Enter your choice:\t \n"))
        except ValueError:
            print("Enter valid nnumber only.")
            continue

        if choice == 1:
            name = input("Name: ")
            phone = input("Phone: ")
            contacts.append([name,phone])
            
            with open("ContactDetails.txt", "w") as file:
                 for name, phone in contacts:
                     file.write(f"{name},{phone}\n")
            print("Task written successfully")
            

        elif choice == 2:
            print("Your Contact details are : \n")
            for i , (name,phone) in enumerate (contacts, start =1):

             print(f"{i}. {name} - {phone}")



        elif choice == 3:
            print("\nYour Contact details are : \n")

            if len(contacts)== 0:
                print("No contact details to show.\n")
                continue ## continue is used 
            else:
            
                for i , (name,phone) in enumerate (contacts, start =1):

                 print(f"{i}. {name} - {phone}")
                 print("\n")

            deleted_contact= int(input("enter the contact saved number to delete the contact:"))
            if (1 <= deleted_contact <= len(contacts) ):
                d_c = contacts.pop(deleted_contact -1)
                print(f"Deleted contact details of :{d_c[0]}\n")
                
                with open("ContactDetails.txt", "w") as file:
                     for name, phone in contacts:
                       file.write(f"{name},{phone}\n")


            else:
                print("Enter valid number.\n")

        elif choice == 4:
            print("Exited Contacts. \n")
            break ## break is used 


        elif choice == 5:
         search = input("🔍 Enter name to search: ").lower()

         found = False

         for name, phone in contacts:
           if search in name.lower():
            print(f"{name} - {phone}")
            found = True

        if not found:
            print("No contact found.")
        else:
         print("Invalid choice. Please select 1–5 only.\n")
