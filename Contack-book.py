import tkinter as tk
from tkinter import messagebox

# Sample contact storage (in memory)
contacts = {}

# Functions to handle contact operations
def add_contact():
    name = entry_name.get()
    phone = entry_phone.get()
    email = entry_email.get()
    address = entry_address.get()

    if name and phone:
        contacts[name] = {'Phone': phone, 'Email': email, 'Address': address}
        messagebox.showinfo("Success", "Contact added successfully!")
        clear_entries()
        refresh_contact_list()
    else:
        messagebox.showerror("Error", "Name and Phone are required fields!")

def view_contact_details(event):
    selected_contact = listbox_contacts.get(listbox_contacts.curselection())
    details = contacts[selected_contact]
    messagebox.showinfo(selected_contact, f"Phone: {details['Phone']}\nEmail: {details['Email']}\nAddress: {details['Address']}")

def search_contact():
    search_term = entry_search.get()
    for name, details in contacts.items():
        if search_term.lower() in name.lower() or search_term in details['Phone']:
            listbox_contacts.delete(0, tk.END)
            listbox_contacts.insert(tk.END, name)
            return
    messagebox.showinfo("Search Result", "No contact found!")

def update_contact():
    selected_contact = listbox_contacts.get(listbox_contacts.curselection())
    contacts[selected_contact] = {
        'Phone': entry_phone.get(),
        'Email': entry_email.get(),
        'Address': entry_address.get()
    }
    messagebox.showinfo("Success", "Contact updated successfully!")
    clear_entries()
    refresh_contact_list()

def delete_contact():
    selected_contact = listbox_contacts.get(listbox_contacts.curselection())
    if messagebox.askyesno("Delete Contact", f"Are you sure you want to delete {selected_contact}?"):
        del contacts[selected_contact]
        refresh_contact_list()

def refresh_contact_list():
    listbox_contacts.delete(0, tk.END)
    for name in contacts.keys():
        listbox_contacts.insert(tk.END, name)

def clear_entries():
    entry_name.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_address.delete(0, tk.END)

# GUI Setup
window = tk.Tk()
window.title("Contact Book")
window.geometry("500x400")

# Contact form
tk.Label(window, text="Name:").grid(row=0, column=0, sticky=tk.W, padx=10, pady=5)
entry_name = tk.Entry(window)
entry_name.grid(row=0, column=1, padx=10, pady=5)

tk.Label(window, text="Phone:").grid(row=1, column=0, sticky=tk.W, padx=10, pady=5)
entry_phone = tk.Entry(window)
entry_phone.grid(row=1, column=1, padx=10, pady=5)

tk.Label(window, text="Email:").grid(row=2, column=0, sticky=tk.W, padx=10, pady=5)
entry_email = tk.Entry(window)
entry_email.grid(row=2, column=1, padx=10, pady=5)

tk.Label(window, text="Address:").grid(row=3, column=0, sticky=tk.W, padx=10, pady=5)
entry_address = tk.Entry(window)
entry_address.grid(row=3, column=1, padx=10, pady=5)

tk.Button(window, text="Add Contact", command=add_contact).grid(row=4, column=0, columnspan=2, pady=10)

# Contact list
tk.Label(window, text="Contacts:").grid(row=5, column=0, sticky=tk.W, padx=10, pady=5)
listbox_contacts = tk.Listbox(window)
listbox_contacts.grid(row=6, column=0, columnspan=2, padx=10, pady=5)
listbox_contacts.bind('<<ListboxSelect>>', view_contact_details)

# Search and operations
tk.Label(window, text="Search:").grid(row=7, column=0, sticky=tk.W, padx=10, pady=5)
entry_search = tk.Entry(window)
entry_search.grid(row=7, column=1, padx=10, pady=5)
tk.Button(window, text="Search", command=search_contact).grid(row=7, column=2, padx=10, pady=5)

tk.Button(window, text="Update Contact", command=update_contact).grid(row=8, column=0, columnspan=1, padx=10, pady=5)
tk.Button(window, text="Delete Contact", command=delete_contact).grid(row=8, column=1, columnspan=1, padx=10, pady=5)

# Start the GUI loop
window.mainloop()
