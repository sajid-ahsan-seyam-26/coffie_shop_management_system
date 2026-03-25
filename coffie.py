import tkinter as tk
from tkinter import ttk, messagebox, simpledialog

# --------------------------
# Ticket and Metro System
# --------------------------

class Ticket:
    ticket_counter = 1

    def __init__(self, passenger_name, passenger_type, train, start, end, fare):
        self.id = Ticket.ticket_counter
        Ticket.ticket_counter = Ticket.ticket_counter + 1

        self.passenger_name = passenger_name
        self.passenger_type = passenger_type
        self.train = train
        self.start = start
        self.end = end
        self.fare = fare

    def __str__(self):
        return self.passenger_name + " - " + self.train + " from " + self.start + " to " + self.end + " | " + str(self.fare) + " BDT"


class MetroSystem:
    def __init__(self):
        self.tickets = []

    def book_ticket(self, passenger_name, passenger_type, train, start, end, fare):
        ticket = Ticket(passenger_name, passenger_type, train, start, end, fare)
        self.tickets.append(ticket)
        return ticket

    def delete_ticket(self, ticket_id):
        for t in self.tickets:
            if t.id == ticket_id:
                self.tickets.remove(t)
                return True
        return False

    def search_tickets(self, keyword):
        result = []
        for t in self.tickets:
            if keyword.lower() in t.passenger_name.lower():
                result.append(t)
        return result

    def total_fare(self):
        total = 0
        for t in self.tickets:
            total = total + t.fare
        return total


# --------------------------
# GUI
# --------------------------

class MetroGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Metro Rail Management System")
        self.root.geometry("1100x650")
        self.root.configure(bg="#0f172a")

        self.system = MetroSystem()

        # Style
        style = ttk.Style()
        style.theme_use("clam")

        style.configure("Treeview",
                        background="#ffffff",
                        foreground="black",
                        rowheight=28,
                        fieldbackground="#ffffff",
                        font=("Arial", 10))

        style.configure("Treeview.Heading",
                        background="#1d4ed8",
                        foreground="white",
                        font=("Arial", 10, "bold"))

        style.map("Treeview", background=[("selected", "#93c5fd")])

        # --------------------------
        # Title
        # --------------------------
        title_frame = tk.Frame(self.root, bg="#1e3a8a", height=70)
        title_frame.pack(fill="x")

        title_label = tk.Label(
            title_frame,
            text="Metro Rail Management System",
            bg="#1e3a8a",
            fg="white",
            font=("Arial", 22, "bold")
        )
        title_label.pack(pady=15)

        # --------------------------
        # Main Container
        # --------------------------
        main_frame = tk.Frame(self.root, bg="#0f172a")
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)

        # Left panel
        left_frame = tk.Frame(main_frame, bg="#e2e8f0", bd=2, relief="ridge")
        left_frame.pack(side="left", fill="y", padx=(0, 15))

        form_title = tk.Label(
            left_frame,
            text="Passenger Information",
            bg="#e2e8f0",
            fg="#0f172a",
            font=("Arial", 14, "bold")
        )
        form_title.grid(row=0, column=0, columnspan=2, pady=15)

        # Labels and entries
        tk.Label(left_frame, text="Passenger Name", bg="#e2e8f0", font=("Arial", 11)).grid(row=1, column=0, sticky="w", padx=15, pady=8)
        self.passenger_name_entry = tk.Entry(left_frame, font=("Arial", 11), width=25)
        self.passenger_name_entry.grid(row=1, column=1, padx=15, pady=8)

        tk.Label(left_frame, text="Train Name", bg="#e2e8f0", font=("Arial", 11)).grid(row=2, column=0, sticky="w", padx=15, pady=8)
        self.train_name_entry = tk.Entry(left_frame, font=("Arial", 11), width=25)
        self.train_name_entry.grid(row=2, column=1, padx=15, pady=8)

        tk.Label(left_frame, text="Start Station", bg="#e2e8f0", font=("Arial", 11)).grid(row=3, column=0, sticky="w", padx=15, pady=8)
        self.start_station_entry = tk.Entry(left_frame, font=("Arial", 11), width=25)
        self.start_station_entry.grid(row=3, column=1, padx=15, pady=8)

        tk.Label(left_frame, text="End Station", bg="#e2e8f0", font=("Arial", 11)).grid(row=4, column=0, sticky="w", padx=15, pady=8)
        self.end_station_entry = tk.Entry(left_frame, font=("Arial", 11), width=25)
        self.end_station_entry.grid(row=4, column=1, padx=15, pady=8)

        tk.Label(left_frame, text="Fare", bg="#e2e8f0", font=("Arial", 11)).grid(row=5, column=0, sticky="w", padx=15, pady=8)
        self.fare_entry = tk.Entry(left_frame, font=("Arial", 11), width=25)
        self.fare_entry.grid(row=5, column=1, padx=15, pady=8)

        tk.Label(left_frame, text="Passenger Type", bg="#e2e8f0", font=("Arial", 11)).grid(row=6, column=0, sticky="w", padx=15, pady=8)
        self.passenger_type = ttk.Combobox(left_frame, values=["Normal", "Student"], state="readonly", width=22, font=("Arial", 11))
        self.passenger_type.current(0)
        self.passenger_type.grid(row=6, column=1, padx=15, pady=8)

        # Button frame
        button_frame = tk.Frame(left_frame, bg="#e2e8f0")
        button_frame.grid(row=7, column=0, columnspan=2, pady=20)

        tk.Button(button_frame, text="Book Ticket", width=16, bg="#2563eb", fg="white", font=("Arial", 10, "bold"),
                  command=self.book_ticket).grid(row=0, column=0, padx=5, pady=5)

        tk.Button(button_frame, text="Delete Ticket", width=16, bg="#dc2626", fg="white", font=("Arial", 10, "bold"),
                  command=self.delete_ticket).grid(row=0, column=1, padx=5, pady=5)

        tk.Button(button_frame, text="Search Ticket", width=16, bg="#059669", fg="white", font=("Arial", 10, "bold"),
                  command=self.search_ticket).grid(row=1, column=0, padx=5, pady=5)

        tk.Button(button_frame, text="Show All", width=16, bg="#7c3aed", fg="white", font=("Arial", 10, "bold"),
                  command=self.show_all_tickets).grid(row=1, column=1, padx=5, pady=5)

        tk.Button(button_frame, text="Total Fare", width=34, bg="#f59e0b", fg="black", font=("Arial", 10, "bold"),
                  command=self.show_total_fare).grid(row=2, column=0, columnspan=2, padx=5, pady=8)

        # Right panel
        right_frame = tk.Frame(main_frame, bg="#e2e8f0", bd=2, relief="ridge")
        right_frame.pack(side="right", fill="both", expand=True)

        table_title = tk.Label(
            right_frame,
            text="Booked Ticket List",
            bg="#e2e8f0",
            fg="#0f172a",
            font=("Arial", 14, "bold")
        )
        table_title.pack(pady=10)

        columns = ("ID", "Name", "Type", "Train", "Start", "End", "Fare")
        self.ticket_list = ttk.Treeview(right_frame, columns=columns, show="headings", height=18)

        for col in columns:
            self.ticket_list.heading(col, text=col)
            self.ticket_list.column(col, width=110, anchor="center")

        self.ticket_list.pack(fill="both", expand=True, padx=15, pady=10)

        scrollbar = ttk.Scrollbar(right_frame, orient="vertical", command=self.ticket_list.yview)
        self.ticket_list.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        # Bottom label
        self.total_label = tk.Label(
            self.root,
            text="Total Fare: 0 BDT",
            bg="#0f172a",
            fg="white",
            font=("Arial", 12, "bold")
        )
        self.total_label.pack(pady=8)

    def update_total_label(self):
        total = self.system.total_fare()
        self.total_label.config(text="Total Fare: " + str(total) + " BDT")

    def book_ticket(self):
        name = self.passenger_name_entry.get()
        train = self.train_name_entry.get()
        start = self.start_station_entry.get()
        end = self.end_station_entry.get()
        fare = self.fare_entry.get()
        p_type = self.passenger_type.get()

        if name == "" or train == "" or start == "" or end == "" or fare == "":
            messagebox.showerror("Error", "Please fill all fields")
            return

        if start == end:
            messagebox.showerror("Error", "Start and End station cannot be same")
            return

        try:
            fare = float(fare)
        except:
            messagebox.showerror("Error", "Fare must be a number")
            return

        if fare <= 0:
            messagebox.showerror("Error", "Fare must be greater than 0")
            return

        if p_type == "Student":
            fare = fare * 0.5

        ticket = self.system.book_ticket(name, p_type, train, start, end, fare)

        self.ticket_list.insert(
            "",
            "end",
            values=(ticket.id, ticket.passenger_name, ticket.passenger_type,
                    ticket.train, ticket.start, ticket.end, ticket.fare)
        )

        self.update_total_label()
        messagebox.showinfo("Success", "Ticket booked successfully")

        self.passenger_name_entry.delete(0, tk.END)
        self.train_name_entry.delete(0, tk.END)
        self.start_station_entry.delete(0, tk.END)
        self.end_station_entry.delete(0, tk.END)
        self.fare_entry.delete(0, tk.END)
        self.passenger_type.current(0)

    def delete_ticket(self):
        selected = self.ticket_list.selection()

        if selected:
            for sel in selected:
                ticket_id = int(self.ticket_list.item(sel)["values"][0])
                self.system.delete_ticket(ticket_id)
                self.ticket_list.delete(sel)

            self.update_total_label()
            messagebox.showinfo("Deleted", "Ticket deleted successfully")
        else:
            messagebox.showerror("Error", "Select a ticket first")

    def search_ticket(self):
        keyword = simpledialog.askstring("Search", "Enter passenger name")

        if keyword != None:
            results = self.system.search_tickets(keyword)
            self.ticket_list.delete(*self.ticket_list.get_children())

            for t in results:
                self.ticket_list.insert(
                    "",
                    "end",
                    values=(t.id, t.passenger_name, t.passenger_type,
                            t.train, t.start, t.end, t.fare)
                )

    def show_all_tickets(self):
        self.ticket_list.delete(*self.ticket_list.get_children())

        for t in self.system.tickets:
            self.ticket_list.insert(
                "",
                "end",
                values=(t.id, t.passenger_name, t.passenger_type,
                        t.train, t.start, t.end, t.fare)
            )

    def show_total_fare(self):
        total = self.system.total_fare()
        messagebox.showinfo("Total Fare", "Total fare of all tickets: " + str(total) + " BDT")


# --------------------------
# Run App
# --------------------------

root = tk.Tk()
app = MetroGUI(root)
root.mainloop()
