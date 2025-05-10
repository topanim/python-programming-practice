import tkinter as tk
from tkinter import ttk

class WorkshopRegistrationForm:
    def __init__(self, master):
        self.master = master
        master.title("Workshop Registration")
        master.geometry("600x600")
        master.resizable(False, False)

        # Header frame
        header_frame = tk.Frame(master, bg="#d3e7d5", height=30)
        header_frame.pack(fill=tk.X, pady=(0, 10))

        # Link label
        link_label = tk.Label(master, text="Register now while seats are available!", fg="blue", cursor="hand2")
        link_label.pack(anchor=tk.W, padx=10)

        # Main frame for two columns
        main_frame = tk.Frame(master)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        main_frame.grid_columnconfigure(0, weight=1)
        main_frame.grid_columnconfigure(1, weight=1)

        # Left frame (Contact Info)
        left_frame = tk.Frame(main_frame)
        left_frame.grid(row=0, column=0, padx=10, pady=5, sticky="nsew")
        left_frame.grid_columnconfigure(2, weight=1) # Make entry column expandable

        # Right frame (Lunch & Payment)
        right_frame = tk.Frame(main_frame)
        right_frame.grid(row=0, column=1, padx=10, pady=5, sticky="nsew")
        right_frame.grid_columnconfigure(1, weight=1) # Make entry/combobox column expandable

        self.entries = {} # Store entry widgets by key
        self.comboboxes = {} # Store combobox widgets by key

        # --- Left Column Widgets ---
        self._add_label_entry(left_frame, "First Name", 0, required=True)
        self._add_label_entry(left_frame, "Last Name", 1, required=True)
        self._add_label_entry(left_frame, "Company/Institution", 2, required=True)

        # Address (Text widget)
        tk.Label(left_frame, text="Address").grid(row=3, column=0, sticky="w", pady=(5, 0))
        tk.Label(left_frame, text="*", fg="red").grid(row=3, column=1, sticky="nw", pady=(5, 0))
        self.address_text = tk.Text(left_frame, height=5, width=30)
        self.address_text.grid(row=3, column=2, columnspan=2, sticky="we", padx=5, pady=(5, 10))

        self._add_label_entry(left_frame, "City", 4)
        self._add_label_combobox(left_frame, "State / Province / Region", 5, ["-Select-", "State1", "State2"])
        self._add_label_combobox(left_frame, "Country", 6, ["-Select-", "Country1", "Country2"])
        self._add_label_entry(left_frame, "Email", 7, required=True)
        self._add_label_entry(left_frame, "Phone Number", 8, required=True)

        # --- Right Column Widgets ---
        tk.Label(right_frame, text="Lunch").grid(row=0, column=0, sticky="w", pady=(0, 10))
        tk.Label(right_frame, text="Meal Preference").grid(row=1, column=0, sticky="w")
        self.meal_pref_combobox = ttk.Combobox(right_frame, values=["Vegetarian", "Non-Vegetarian"], state="readonly", width=20)
        self.meal_pref_combobox.grid(row=1, column=1, sticky="w", padx=5)
        self.meal_pref_combobox.set("Vegetarian")

        tk.Label(right_frame, text="Payment Details").grid(row=2, column=0, sticky="w", pady=(15, 5))
        tk.Label(right_frame, text="Payment Mode").grid(row=3, column=0, sticky="w")

        self.cash_var, self.cheque_var, self.demand_draft_var = tk.BooleanVar(), tk.BooleanVar(), tk.BooleanVar()
        tk.Checkbutton(right_frame, text="Cash", variable=self.cash_var).grid(row=3, column=1, sticky="w", padx=5)
        tk.Checkbutton(right_frame, text="Cheque", variable=self.cheque_var).grid(row=4, column=1, sticky="w", padx=5)
        tk.Checkbutton(right_frame, text="Demand Draft", variable=self.demand_draft_var).grid(row=5, column=1, sticky="w", padx=5, pady=(0, 10))

        self._add_label_entry(right_frame, "DD/Cheque No.", 6)
        self._add_label_entry(right_frame, "Drawn On (Bank Name)", 7)
        self._add_label_entry(right_frame, "Payable at", 8)

        # --- Footer Buttons ---
        footer_frame = tk.Frame(master)
        footer_frame.pack(pady=10)
        tk.Button(footer_frame, text="Submit", command=self.submit_data, bg="#a5d6a7").pack(side=tk.LEFT, padx=10)
        tk.Button(footer_frame, text="Reset", command=self.reset_form, bg="#a5d6a7").pack(side=tk.LEFT, padx=10)

    # --- Helper Methods ---
    def _add_label_entry(self, parent_frame, text, row, required=False):
        tk.Label(parent_frame, text=text).grid(row=row, column=0, sticky="w", pady=2)
        col_offset = 0
        if required:
            tk.Label(parent_frame, text="*", fg="red").grid(row=row, column=1, sticky="nw", pady=2)
            col_offset = 1
        entry = tk.Entry(parent_frame, width=30)
        entry.grid(row=row, column=1 + col_offset, columnspan=2 - col_offset, sticky="we", padx=5, pady=2)
        self.entries[text.lower().replace(" ", "_").replace("/", "_").replace("(", "").replace(")", "").replace(".", "")] = entry

    def _add_label_combobox(self, parent_frame, text, row, values):
        tk.Label(parent_frame, text=text).grid(row=row, column=0, sticky="w", pady=2)
        combo = ttk.Combobox(parent_frame, values=values, state="readonly", width=20)
        combo.grid(row=row, column=2, sticky="w", padx=5, pady=2)
        combo.set(values[0] if values else "")
        self.comboboxes[text.lower().replace(" ", "_").replace("/", "_")] = combo

    # --- Action Methods ---
    def submit_data(self):
        print("Submit нажата")

    def reset_form(self):
        print("Reset нажата")
        for entry in self.entries.values(): entry.delete(0, tk.END)
        self.address_text.delete("1.0", tk.END)
        self.meal_pref_combobox.set(self.meal_pref_combobox['values'][0] if self.meal_pref_combobox['values'] else "")
        for combo in self.comboboxes.values(): combo.set(combo['values'][0] if combo['values'] else "")
        self.cash_var.set(False); self.cheque_var.set(False); self.demand_draft_var.set(False)

# --- Run Application ---
if __name__ == "__main__":
    root = tk.Tk()
    app = WorkshopRegistrationForm(root)
    root.mainloop()