

contacts = []

try:
    with open("ContactDetails.txt","r") as file:
       contacts= file.read().splitlines()
except FileNotFoundError:
    pass

        
while True:


        print("\nWelcome to the contacts menu \n")
        print("1. Add new contact")
        print("2. View saved contacts")
        print("3. Delete existing contact")
        print("4. Exit \n")


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
            print("Exit Contacts. \n")
            break ## break is used 
        else:
         print("Invalid choice. Please select 1–4 only.\n")