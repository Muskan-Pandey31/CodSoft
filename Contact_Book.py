contacts = {}
while True:
    print("\nContact Book")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Delete Contact")
    print("4. Update Contact")
    print("5. Search Contact")
    
    choice = input("Enter your choice:")
    if choice == "1":
        name = input("Enter your name:")
        if name in contacts:
            print(f"Contact name{name} already exists!")
        else:
            email = input("Enter email:")
            mobile = input("Enter mobile number:")
            address = input("Enter your address:")
            contacts[name] = {"email": email, "mobile": mobile, "address": address}
            print(f"Contact name{name} has been created successfully!")

    elif choice == "2":
          name = input("Enter contact name to view:")
          if name in contacts: 
              contact = contacts[name]
              print(f"Name: {name}, Mobile Number: {mobile}, Email: {email}, Address: {address}")    
          else:
              print("Contact not found") 

    elif choice == "3":
         name = ("Enter contact name to delete:")
         if name in contacts:
              del contacts[name]
              print(f"Contact name {name} has been deleted successfully!")
         else:
              print("Contact not found")             

    elif choice == "4":
        name = ("Enter name to update contact:")
        if name in contacts:
             email = input("Enter email:")
             mobile = input("Enter mobile number:")
             address = input("Eter your address")
             contacts[name] = {"email": email, "mobile": mobile, "address": address}
        else:
              print("Contact not found") 

    elif choice == "5":
         search_name = input("Enter contact name to search:")
         found = False
         for name, contact in contacts.items():
              if search_name.lower() in name.lower():
                   print(f"Found - Name {name}, Mobile Number:{mobile}, Email:{email}, Address: {address}")
                   found = True
         if not found:
              print("No contact found with this name")

                   

         


   