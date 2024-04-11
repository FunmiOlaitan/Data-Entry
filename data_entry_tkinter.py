import tkinter as tk
from tkinter import ttk
import json

class RockclimbingClub:
    def __init__(self):
        self.memberships = []
    
    def add_memebership_details(self, name, age, email):
        membership = {
            'Name': name,
            'Age': age,
            'Email': email
        }
        self.memberships.append(membership)
    
    def get_memebership_details(self):
        return self.memberships
    
    def save_to_file(self, filename='member_details.json'):
        with open(filename, 'w') as file:
            json.dump(self.memberships, file)
    
    def load_from_file(self, filename='member_details.json'):
        try:
            with open(filename, 'r') as file:
                self.memebrships = json.load(file)
        except FileNotFoundError:
            print("File not found.")


