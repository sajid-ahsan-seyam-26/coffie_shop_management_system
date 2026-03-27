import tkinter as tk
from tkinter import messagebox, simpledialog


class Ticket:
    ticket_counter = 1

    def __init__(self, name, p_type, train, start, end, fare):
        self.id = Ticket.ticket_counter
        Ticket.ticket_counter += 1

        self.name = name
        self.p_type = p_type
        self.train = train
        self.start = start
        self.end = end
        self.fare = fare

    def __str__(self):
        return f"{self.id} | {self.name} | {self.p_type} | {self.train} | {self.start}->{self.end} | {self.fare} BDT"


class MetroSystem:
    def __init__(self):
        self.tickets = []

    def book_ticket(self, *args):
        t = Ticket(*args)
        self.tickets.append(t)
        return t

    def delete_ticket(self, ticket_id):
        for t in self.tickets:
            if t.id == ticket_id:
                self.tickets.remove(t)
                return True
        return False

    def search(self, keyword):
        return [t for t in self.tickets if keyword.lower() in t.name.lower()]

    def total_fare(self):
        return sum(t.fare for t in self.tickets)



class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Metro System")

        self.system = MetroSystem()

        # Inputs
        tk.Label(root, text="Name").grid(row=0, column=0)
        self.name = tk.Entry(root)
        self.name.grid(row=0, column=1)

        tk.Label(root, text="Train").grid(row=1, column=0)
        self.train = tk.Entry(root)
        self.train.grid(row=1, column=1)

        tk.Label(root, text="Start").grid(row=2, column=0)
        self.start = tk.Entry(root)
        self.start.grid(row=2, column=1)

        tk.Label(root, text="End").grid(row=3, column=0)
        self.end = tk.Entry(root)
        self.end.grid(row=3, column=1)

        tk.Label(root, text="Fare").grid(row=4, column=0)
        self.fare = tk.Entry(root)
        self.fare.grid(row=4, column=1)

        # Dropdown (instead of ttk Combobox)
        self.p_type = tk.StringVar(value="Normal")
        tk.OptionMenu(root, self.p_type, "Normal", "Student").grid(row=5, column=1)

        # Buttons
        tk.Button(root, text="Book", command=self.book).grid(row=6, column=0)
        tk.Button(root, text="Delete", command=self.delete).grid(row=6, column=1)
        tk.Button(root, text="Search", command=self.search).grid(row=7, column=0)
        tk.Button(root, text="Show All", command=self.show_all).grid(row=7, column=1)
        tk.Button(root, text="Total Fare", command=self.total).grid(row=8, column=0, columnspan=2)

        # Listbox instead of Treeview
        self.listbox = tk.Listbox(root, width=80, height=15)
        self.listbox.grid(row=9, column=0, columnspan=2)

        scrollbar = tk.Scrollbar(root)
        scrollbar.grid(row=9, column=2, sticky="ns")

        self.listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.listbox.yview)

    def book(self):
        name = self.name.get()
        train = self.train.get()
        start = self.start.get()
        end = self.end.get()
        fare = self.fare.get()
        p_type = self.p_type.get()

        if not name or not train or not start or not end or not fare:
            messagebox.showerror("Error", "Fill all fields")
            return

        if start == end:
            messagebox.showerror("Error", "Start & End same")
            return

        try:
            fare = float(fare)
        except:
            messagebox.showerror("Error", "Fare must be number")
            return

        if p_type == "Student":
            fare *= 0.5

        t = self.system.book_ticket(name, p_type, train, start, end, fare)
        self.listbox.insert(tk.END, str(t))

    def delete(self):
        selected = self.listbox.curselection()
        if not selected:
            messagebox.showerror("Error", "Select item")
            return

        index = selected[0]
        text = self.listbox.get(index)
        ticket_id = int(text.split("|")[0].strip())

        self.system.delete_ticket(ticket_id)
        self.listbox.delete(index)

    def search(self):
        key = simpledialog.askstring("Search", "Enter name")
        if key:
            self.listbox.delete(0, tk.END)
            for t in self.system.search(key):
                self.listbox.insert(tk.END, str(t))

    def show_all(self):
        self.listbox.delete(0, tk.END)
        for t in self.system.tickets:
            self.listbox.insert(tk.END, str(t))

    def total(self):
        total = self.system.total_fare()
        messagebox.showinfo("Total", f"{total} BDT")



root = tk.Tk()
App(root)
root.mainloop()
