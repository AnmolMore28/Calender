import calendar
import tkinter as tk
from tkinter import ttk

class CalendarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Stylish Calendar App")
        
        self.year_var = tk.StringVar()
        self.month_var = tk.StringVar()
        
        self.create_widgets()

        # Festival data for specific dates
        self.date_festivals = {
            (2023, 12, 25): ['Christmas'],
            (2023, 4, 2): ['Good Friday']
            # Add more dates and festivals as needed
        }

    def create_widgets(self):
        # Year Entry
        year_label = ttk.Label(self.root, text="Enter Year:")
        year_label.grid(row=0, column=0, pady=10)
        year_entry = ttk.Entry(self.root, textvariable=self.year_var)
        year_entry.grid(row=0, column=1, pady=10)

        # Month Entry
        month_label = ttk.Label(self.root, text="Enter Month:")
        month_label.grid(row=0, column=2, pady=10)
        month_entry = ttk.Entry(self.root, textvariable=self.month_var)
        month_entry.grid(row=0, column=3, pady=10)

        # Show Calendar Button
        show_button = ttk.Button(self.root, text="Show Calendar", command=self.show_calendar)
        show_button.grid(row=0, column=4, pady=10)

        # Calendar Widget
        style = ttk.Style()
        style.configure("Treeview", background="#e1e1e1", fieldbackground="#e1e1e1", foreground="black", font=('Arial', 12))
        style.configure("Treeview.Heading", font=('Arial', 14))  # Increase heading font size
        style.configure("Treeview", rowheight=30)  # Increase Y-axis height

        self.cal = ttk.Treeview(self.root, columns=('Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'), show='headings', height=6)
        for col in ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']:
            self.cal.heading(col, text=col)
        self.cal.grid(row=1, column=0, columnspan=5, padx=10, pady=10)

    def show_calendar(self):
        try:
            year = int(self.year_var.get())
            month = int(self.month_var.get())
        except ValueError:
            return

        cal_data = calendar.monthcalendar(year, month)
        for i, week in enumerate(cal_data):
            week_str = [str(day) if day != 0 else '' for day in week]

            # Append festivals to the end of each week
            for j, day in enumerate(week_str):
                date = (year, month, day)
                if date in self.date_festivals:
                    week_str[j] += '\n' + '\n'.join(self.date_festivals[date])

            self.cal.insert('', i, values=week_str)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalendarApp(root)
    root.mainloop()


