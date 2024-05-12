import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as messagebox
import sqlite3
import re

class RockClimbingClub:
    def __init__(self):
        self.conn = sqlite3.connect("membership.db") # connection to SQLite database membership.db
        self.create_table() # method to create table

    def create_table(self):   # create table in database
        c = self.conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS memberships (
                  id INTEGER PRIMARY KEY, 
                  username TEXT, 
                  age INTEGER, 
                  email TEXT,
                  membership_type TEXT
                  )''')
        self.conn.commit()
   
    def add_membership(self, username, age, email, memebership_type): # adds new membership
        c = self.conn.cursor()
        c.execute ("INSERT INTO memberships (username, age, email, membership_type) VALUES (?,?,?,?)", (username, age, email, memebership_type)) #adds new rows to membership table
        self.conn.commit()  # commit changes to database

    def get_membership_details(self):  # retrieves all methods
        c = self.conn.cursor()
        c.execute("SELECT * FROM memberships") # selects all column
        return c.fetchall() # fetch rows and return as tuple
    
    def clear_all_memberships(self):
        c =self.conn.cursor()
        c.execute("DELETE FROM memberships")
        self.conn.commit()
class MembershipGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Climbing Club Membership Database")
        self.climbing_club = RockClimbingClub()

        # Entry Frame
        self.entry_frame = ttk.LabelFrame(root, text="Add Membership Details")
        self.entry_frame.grid(row=0, column=0, padx = 10, pady=10, sticky="nsew")

        self.username_label = ttk.Label(self.entry_frame, text="Username:")
        self.username_entry = ttk.Entry(self.entry_frame)

        self.age_label = ttk.Label(self.entry_frame, text="Age:")
        self.age_entry = ttk.Entry(self.entry_frame)

        self.email_label = ttk.Label(self.entry_frame, text="Email:")
        self.email_entry = ttk.Entry(self.entry_frame)

        self.membership_type_label = ttk.Label(self.entry_frame, text="Membership Type:")
        self.membership_type_combobox = ttk.Combobox(self.entry_frame, values=["Basic", "Premium", "VIP"])

        self.add_button = ttk.Button(self.entry_frame, text="Add Membership", command=self.add_membership)
        
        # Display Frame
        self.display_frame = ttk.LabelFrame(root, text = "Display Memberships")
        self.display_frame.grid(row=1, column=0, padx = 10, pady = 10, sticky ="nsew" )

        self.display_text = tk.Text(self.display_frame, height= 10, width= 50, state="disabled" )
        self.display_text.grid(row=0, column=0, padx= 10, pady =10)
        
        # Menu Frame
        self.menu_frame = ttk.LabelFrame(root, text = "Menu")
        self.menu_frame.grid(row=2, column=0, padx = 10, pady =10, sticky = "nsew")

        self.view_all_button = ttk.Button(self.menu_frame, text="View all", command=self.display_membership_details)
        self.clear_all_button = ttk.Button(self.menu_frame, text="Clear all", command=self.clear_all_memberships)

        # Grid placement for menu buttons
        self.view_all_button.grid(row=0, column=0, padx=5, pady=5)
        self.clear_all_button.grid(row=0, column=2, padx=5, pady=5)


        # Grid configuration of columns when window is resized 
        self.root.columnconfigure(0, weight=1)
        self.entry_frame.columnconfigure(1, weight=1)
        self.display_frame.columnconfigure(0, weight=1)

        # Grid placement
        self.username_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.username_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        self.age_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.age_entry.grid(row=1, column=1, padx=5, pady=5, sticky="ew")
        self.email_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.email_entry.grid(row=2, column=1, padx=5, pady=5, sticky="ew")
        self.membership_type_label.grid(row=3, column=0, padx=5, pady=5, sticky='e')
        self.membership_type_combobox.grid(row=3, column=1, padx=5, pady=5, sticky='ew')
        self.add_button.grid(row=4, column=0, columnspan=2, pady=10)
    
        self.display_text.grid(row=0, column=0)

    def add_membership(self): 
        username = self.username_entry.get() # gets text entered by user
        age = self.age_entry.get()
        email = self.email_entry.get()
        membership_type = self.membership_type_combobox.get()

        # data validation
        if self.validate_input(username, age, email):
            self.climbing_club.add_membership(username, age, email, membership_type)  # passes the values entered to the method and add the details to the db
            self.clear_entry_fields()  # to clear text entry fields
            self.membership_type_combobox.set("")
            tk.messagebox.showinfo("Success", "Membership successfully added!")
        else:
            tk.messagebox.showerror("Error", "Invalid input!")
    
    def validate_input(self, username, age, email):
        # username should not be empty
        if not username:
            return False
        
        # age should be positive int
        try: 
            age = int(age)
            if age <= 0:
                return False
        except ValueError:
            return False
        
        # email should be in valid format
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return False
        
        return True

    def display_membership_details(self):
        memberships = self.climbing_club.get_membership_details() # calls get_memebrship_details to retrieve all membership details in tuples
        self.display_text.config(state="normal") 
        self.display_text.delete("1.0", tk.END)

        for member in memberships: # iterates over each memebrship
            self.display_text.insert(tk.END, f"Username: {member[1]}\n")
            self.display_text.insert(tk.END, f"Age: {member[2]}\n")
            self.display_text.insert(tk.END, f"Email: {member[3]}\n")
        
        self.display_text.config(state="disabled") # preventing modification by user 

    
    def clear_entry_fields(self):
        self.username_entry.delete(0, tk.END)
        self.age_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)

    def clear_all_memberships(self):
        self.climbing_club.clear_all_memberships()
        self.username_entry.config(state="normal")
        self.age_entry.delete(0, tk.END)
        self.email_entry.config(state="disabled")
        self.display_membership_details()


if __name__ == "__main__":
    root = tk.Tk()
    app = MembershipGUI(root)
    root.mainloop()

