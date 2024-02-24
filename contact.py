import tkinter as tk
from tkinter import messagebox

class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactManager:
    def __init__(self):
        self.contacts = []
        
    def add_contact(self, contact):
        self.contacts.append(contact)
    
    def delete_contact(self, contact):
        self.contacts.remove(contact)
    
    def search_contact(self, keyword):
        results = []
        for contact in self.contacts:
            if keyword.lower() in contact.name.lower() or keyword in contact.phone:
                results.append(contact)
        return results

class ContactApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Contact Manager")
        
        self.contact_manager = ContactManager()
        
        self.name_label = tk.Label(master, text="Name:")
        self.name_label.grid(row=0, column=0, padx=10, pady=5)
        self.name_entry = tk.Entry(master)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)

        self.phone_label = tk.Label(master, text="Phone:")
        self.phone_label.grid(row=1, column=0, padx=10, pady=5)
        self.phone_entry = tk.Entry(master)
        self.phone_entry.grid(row=1, column=1, padx=10, pady=5)

        self.email_label = tk.Label(master, text="Email:")
        self.email_label.grid(row=2, column=0, padx=10, pady=5)
        self.email_entry = tk.Entry(master)
        self.email_entry.grid(row=2, column=1, padx=10, pady=5)

        self.address_label = tk.Label(master, text="Address:")
        self.address_label.grid(row=3, column=0, padx=10, pady=5)
        self.address_entry = tk.Entry(master)
        self.address_entry.grid(row=3, column=1, padx=10, pady=5)

        self.add_button = tk.Button(master, text="Add Contact", command=self.add_contact)
        self.add_button.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

        self.search_entry = tk.Entry(master)
        self.search_entry.grid(row=5, column=0, padx=10, pady=5)
        self.search_button = tk.Button(master, text="Search", command=self.search_contact)
        self.search_button.grid(row=5, column=1, padx=10, pady=5)

        self.contact_listbox = tk.Listbox(master, width=40, height=10)
        self.contact_listbox.grid(row=6, column=0, columnspan=2, padx=10, pady=5)

        self.view_button = tk.Button(master, text="View All Contacts", command=self.view_contacts)
        self.view_button.grid(row=7, column=0, columnspan=2, padx=10, pady=5)

        self.delete_button = tk.Button(master, text="Delete Contact", command=self.delete_contact)
        self.delete_button.grid(row=8, column=0, padx=10, pady=5)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()
        if name and phone:
            contact = Contact(name, phone, email, address)
            self.contact_manager.add_contact(contact)
            messagebox.showinfo("Success", "Contact added successfully.")
            self.clear_entries()
        else:
            messagebox.showwarning("Warning", "Name and phone number are required.")

    def search_contact(self):
        keyword = self.search_entry.get()
        if keyword:
            results = self.contact_manager.search_contact(keyword)
            self.display_contacts(results)
        else:
            messagebox.showwarning("Warning", "Please enter a search keyword.")

    def view_contacts(self):
        self.display_contacts(self.contact_manager.contacts)

    def display_contacts(self, contacts):
        self.contact_listbox.delete(0, tk.END)
        for contact in contacts:
            self.contact_listbox.insert(tk.END, f"{contact.name} - {contact.phone}")

    def delete_contact(self):
        selected_index = self.contact_listbox.curselection()
        if selected_index:
            contact = self.contact_manager.contacts[selected_index[0]]
            self.contact_manager.delete_contact(contact)
            self.view_contacts()
            messagebox.showinfo("Success", "Contact deleted successfully.")
        else:
            messagebox.showwarning("Warning", "Please select a contact to delete.")

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactApp(root)
    root.mainloop()