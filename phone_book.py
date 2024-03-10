import sqlite3

def create_contact(conn, name, cell, email):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO contacts (name, cell, email) VALUES (?, ?, ?)", (name, cell, email))
    conn.commit()
    print(f"Contact {name} added successfully.")

def display_contacts(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM contacts")
    contacts = cursor.fetchall()
    
    if not contacts:
        print("No contacts found.")
    else:
        print("Contacts:")
        for contact in contacts:
            print(f"ID: {contact[0]}, Name: {contact[1]}, Cell#: {contact[2]}, E-mail: {contact[3]}")

def update_contact(conn, contact_id, new_name, new_cell, new_email):
    cursor = conn.cursor()
    cursor.execute("UPDATE contacts SET name=?, cell=?, email=? WHERE id=?", (new_name, new_cell, new_email, contact_id))
    conn.commit()
    print(f"Contact with ID {contact_id} updated successfully.")

def delete_contact(conn, contact_id):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM contacts WHERE id=?", (contact_id,))
    conn.commit()
    print(f"Contact with ID {contact_id} deleted successfully.")

def main():
    conn = sqlite3.connect('contacts.db')
    conn.execute('''
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            cell TEXT NOT NULL,
            email TEXT
        )
    ''')

    # Insert 5 rows of data (if not already inserted)
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM contacts")
    count = cursor.fetchone()[0]

    if count == 0:
        contacts_data = [
            ("Raghavendra", "9108070437", "raghavendra@gmail.com"),
            ("Raghu B S", "8861747820", "raghu@gmail.com"),
            ("Prabu K", "8050061683", "prabhu@gmail.com"),
            ("Sunil", "6362753027", "sunil@gmail.com"),
            ("Rakesh", "8277490733", "rakesh@gmail.com"),
            ("Rohan", "6360112301", "rohan@gmail.com"),
            ("Gokul", "8618220347", "gokul@gmail.com"),
            
        ]

        for contact_data in contacts_data:
            create_contact(conn, *contact_data)

    while True:
        print("\n1. Add a new contact")
        print("2. Display all contacts")
        print("3. Update a contact")
        print("4. Delete a contact")
        print("5. Exit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == '1':
            name = input("Enter name: ")
            cell = input("Enter cell number: ")
            email = input("Enter email (optional): ")
            create_contact(conn, name, cell, email)

        elif choice == '2':
            display_contacts(conn)

        elif choice == '3':
            contact_id = input("Enter the ID of the contact to update: ")
            new_name = input("Enter new name: ")
            new_cell = input("Enter new cell number: ")
            new_email = input("Enter new email (optional): ")
            update_contact(conn, contact_id, new_name, new_cell, new_email)

        elif choice == '4':
            contact_id = input("Enter the ID of the contact to delete: ")
            delete_contact(conn, contact_id)

        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter 1, 2, 3, 4, or 5.")

    conn.close()

if __name__ == "__main__":
    main()
