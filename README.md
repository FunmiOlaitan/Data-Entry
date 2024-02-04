# Data Entry: Rock Climbing Club Membership Details

## Overview
This program is designed to manage and store membership details for a Rock Climbing Club. Users can input their personal information, and the program will display the details for confirmation. If confirmed, the information is stored; otherwise, it allows for a new input. The project also includes extensions such as allowing entry of multiple memberships, storing details in a file, retrieving details from a file, and searching for stored users.

## Getting Started
To run the program, execute the provided Python script `data_entry.py`. The program will guide you through entering membership details and provide options for confirmation, storage, and retrieval.

```bash
python data_entry.py
```

## Features

### 1. Get Membership Details
- Users are prompted to input their name, age, contact number, and email.

### 2. Display Details
- The entered membership details are displayed with appropriate headings for confirmation.

### 3. Save Membership
- Confirmed membership details are saved to a file named `membership_details.json`.

### 4. Load from File
- The program loads existing membership details from the `membership_details.json` file if available.

### 5. Search for Members
- Users can search for a member by entering their name or email. The program will display the member's details if found.

### 6. Multiple Memberships
- The program allows users to enter details for multiple memberships.

## Command Line Interface

### Example Usage
1. Enter membership details as prompted.
2. Confirm details when prompted.
3. Repeat for additional memberships or exit.
4. Search for a member by entering their name or email.

## Code Structure
The main functionalities are organised in the `data_entry.py` file. Key functions include:
- `get_membership_details`: Capture user input for membership details.
- `display_details`: Display entered details for confirmation.
- `save_membership`: Save confirmed memberships to the `membership_details.json` file.
- `load_from_file`: Load existing memberships from the `membership_details.json` file.
- `search_member`: Search for a member based on name or email in stored memberships.
- `main`: Main function to execute the program.

## Requirements
- Python 3.x

## Extensions
1. Allow entry of more than one membership.
2. Store membership details to a file.
3. Retrieve details from a file.
4. Allow searching for stored users.

## Contributions
Contributions and feedback are welcome. Feel free to open an issue or submit a pull request.
