import tkinter as tk
from tkinter import messagebox


menu = {
    "Espresso": 120,
    "Cappuccino": 180,
    "Latte": 200,
    "Americano": 150,
    "Mocha": 220
}


class CoffeeShop:
    def __init__(self, root):
        self.root = root
        self.root.title("Coffee Shop Management System")

        self.orders = []

        tk.Label(root, text="☕ Coffee Shop", font=("Arial", 18, "bold")).pack(pady=10)

        # Dropdown
        self.selected_item = tk.StringVar(value="Espresso")
        tk.OptionMenu(root, self.selected_item, *menu.keys()).pack()

        # Quantity
        tk.Label(root, text="Quantity").pack()
        self.qty = tk.Entry(root)
        self.qty.pack()

        # Buttons
        tk.Button(root, text="Add Order", command=self.add_order).pack(pady=5)
        tk.Button(root, text="Remove Selected", command=self.remove_order).pack(pady=5)
        tk.Button(root, text="Total Bill", command=self.total_bill).pack(pady=5)

        # Listbox
        self.listbox = tk.Listbox(root, width=50, height=10)
        self.listbox.pack(pady=10)

    def add_order(self):
        item = self.selected_item.get()
        qty = self.qty.get()

        if not qty:
            messagebox.showerror("Error", "Enter quantity")
            return

        try:
            qty = int(qty)
        except:
            messagebox.showerror("Error", "Invalid number")
            return

        price = menu[item] * qty
        order_text = f"{item} x{qty} = {price} BDT"

        self.orders.append(price)
        self.listbox.insert(tk.END, order_text)

        self.qty.delete(0, tk.END)

    def remove_order(self):
        selected = self.listbox.curselection()
        if not selected:
            messagebox.showerror("Error", "Select item")
            return

        index = selected[0]
        self.listbox.delete(index)
        self.orders.pop(index)

    def total_bill(self):
        total = sum(self.orders)
        messagebox.showinfo("Total Bill", f"Total: {total} BDT")



root = tk.Tk()
app = CoffeeShop(root)
root.mainloop()
