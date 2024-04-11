import tkinter as tk
from tkinter import ttk
import sqlite3

class RockClimbingClub:
    def __init__(self):
        self.conn = sqlite3.connect("membership.db") # connection to SQLite database memebrships.db
        self.create_table() # method to create table

    def create_table(self):   #create table in database
        c = self.conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS memberships (id INTEGER PRIMARY KEY, name TEXT, age INTEGER, email TEXT)''')
        self.conn.commit()
   
    def add_membership_details(self, name, age, email):
        c = self.conn.cursor()
        c.execute ("INSERT INTO memberships (name, age, email) VLAUES (?,?,?)", (name, age, email))
        self.conn.commit()

    def get_membership_details(self):
        c = self.conn.cursor()
        c.execute("SELECT * FROM memberships")
        return c.fetchall()
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
        
        # Menu Frame
        self.menu_frame = ttk.LabelFrame(root, text = "Menu")
        self.menu_frame.grid(row=2, column=0, padx = 10, pady =10, sticky = "nsew")
        
        self.save_button = ttk.Button(self.menu_frame)
        self.load_button = ttk.Button(self.menu_frame)

if __name__ == "__main__":
    root = tk.Tk()
    app = MembershipGUI(root)
    root.mainloop()

