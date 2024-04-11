import tkinter as tk
from tkinter import ttk
import json

class RockClimbingClub:
    def __init__(self):
        self.memberships = []
    
    def add_memebership_details(self, name, age, email):
        membership = {
            'Name': name,
            'Age': age,
            'Email': email
        }
        self.memberships.append(membership)
    
    def get_membership_details(self):
        return self.memberships
    
    def save_to_file(self, filename='member_details.json'):
        with open(filename, 'w') as file:
            json.dump(self.memberships, file)
    
    def load_from_file(self, filename='member_details.json'):
        try:
            with open(filename, 'r') as file:
                self.memberships = json.load(file)
        except FileNotFoundError:
            print("File not found.")

class MembershipGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Climbing Club Membership Database")
        self.climbing_club = RockClimbingClub()

        # Entry Frame
        self.entry_frame = ttk.LabelFrame(root, text="Add Membership Details")
        self.entry_frame.grid(row=0, column=0, padx = 10, pady=10, sticky="nsew")

        self.name_label = ttk.Label(self.entry_frame, text="Name:")
        self.name_entry = ttk.Entry(self.entry_frame)

        self.age_label = ttk.Label(self.entry_frame, text="Age:")
        self.age_entry = ttk.Entry(self.entry_frame)

        self.email_label = ttk.Label(self.entry_frame, text="Email:")
        self.email_entry = ttk.Entry(self.entry_frame)

        self.add_button = ttk.Button(self.entry_frame, text="Add Membership")
        
        # Display Frame 
        self.display_frame = ttk.LabelFrame(root, text = "Display Memberships")
        self.display_frame.grid(row=1, column=0, padx = 10, pady = 10, sticky ="nsew" )

        self.display_text = tk.Text(self.display_frame, height= 10, width= 50, state="disabled" )
        self.display_text.grid(row=0, column=0, padx= 10, pady =10)

if __name__ == "__main__":
    root = tk.Tk()
    app = MembershipGUI(root)
    root.mainloop()

