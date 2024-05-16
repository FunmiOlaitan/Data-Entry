# Data Entry: Rock Climbing Club Membership Database

## Introduction
This Python project is a Rock Climbing Club Membership Management System, designed to help manage membership details including usernames, ages, emails, and membership types. It utilizes the `tkinter` library for the graphical user interface, and `sqlite3` for database management. The system also incorporates database backup, logging, data validation, and data visualization using `matplotlib`.

## Features
- **Add Membership**: Users can add new memberships by providing username, age, email, and membership type details.
- **Display Memberships**: Users can view all existing memberships stored in the database.
- **Clear All Memberships**: Option to clear all memberships from the database.
- **Automatic Backup**: The system automatically backs up the database at regular intervals.
- **Data Insights**: Utilizes SQLite views to provide insights into membership data such as total members, average age, membership type counts, and latest members.
- **GUI Interface**: Provides a user-friendly graphical interface using Tkinter for interaction.


## Dependencies
- `tkinter`: For creating the graphical user interface.
- `sqlite3`: Database management system for storing membership data.
- `matplotlib`: For data visualization.
- `re`: For email validation.
- `os`, `shutil`: For file operations and directory management.
- `datetime`: For working with date and time.
- `logging`: For logging membership additions and other events.

## Usage
1. **Add Membership**: Enter username, age, email, and select membership type, then click "Add Membership".
2. **View Memberships**: Click "View all" to display existing memberships.
3. **Clear Memberships**: Click "Clear all" to delete all memberships.
4. **Analytics**: Analytical insights can be obtained by running the script directly. Total members, average age, membership type counts, and latest members will be printed and a bar chart of membership type counts will be saved as an image (`membership_type_counts_plot.png`).

## How to Run
1. Ensure Python is installed on your system.
2. Run the script `membership.py` using Python.
3. The GUI application will open. Interact with the application using the provided functionalities.

## Author
This project was developed by Funmilola Olaitan.