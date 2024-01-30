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

def save_membership(memberships):
    with open("membership_details", "w") as file:
        json.dump(memberships, file)

def load_from_file():
    try:
        with open("membership_details.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
def search_member(memberships, query):
    for member in memberships:
        if query.lower() in member["Name"].lower() or query.lower() in member["Email"].lower():
            return member
    return None

