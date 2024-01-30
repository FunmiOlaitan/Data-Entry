import json

def get_membership_details():
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    contact_number = input("Enter your contact number: ")
    email = input("Enter your email: ")
    
    return {"Name": name, "Age": int(age), "Contact Number": contact_number, "Email": email}

def display_details(details):
    print("\nMembership Details")
    for key, value in details.items():
        print("f'{key}:{value}")

