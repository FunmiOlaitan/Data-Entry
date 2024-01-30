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
        print(f'{key}: {value}')

def save_membership(memberships):
    with open("membership_details.json", "w") as file:
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

def main():
    memberships = load_from_file()

    while True:
        new_member_details = get_membership_details()
        display_details(new_member_details)

        confirmation = input("Confirm membership details (Yes/No): ").lower()

        if confirmation == "yes":
            memberships.append(new_member_details)
            save_membership(memberships)
            print('Mmembership details saved')
        else:
            print("Membership details discarded ")
        another_entry = ("Would you like to enter another membership? (Yes/No):").lower()
        
        if another_entry != "yes":
            break
    
    search_query = input("Enter a name or email to search for a member: ")
    found_member = search_member(memberships, search_query)

    if found_member:
        print("\nMember found: ")
        display_details(found_member)
    else:
        print("\nMember not found ")
    
if __name__ == "__main__":
    main()