from tkinter import *
from tkinter import messagebox
from Functions.calculations import FitnessCalculations
from constants.constants import *

class FitnessCalculator:
    def __init__(self):
        self.calculator = Tk()
        self.calculator.title('Fitness Calculator')
        self.calculator.resizable(0, 0)
        self.calculator.configure(bg='#FDF0D5')
        window_width = 700  
        window_height = 820  
        screen_width = self.calculator.winfo_screenwidth()
        screen_height = self.calculator.winfo_screenheight()
        x = (screen_width - window_width) // 2
        y = (screen_height - window_height) // 2
        self.calculator.geometry(f'{window_width}x{window_height}+{x}+{y}')
        self.create_widgets()
        self.calculator.mainloop()

    def create_widgets(self):
        Label(self.calculator, text=APP_TITLE, bg='#780000', fg='white', width=30, font=('Helvetica', 16)).grid(row=0, column=0, columnspan=4, pady=10)
        self.create_user_info_section()
        self.create_gender_section()
        self.entries = self.create_entry_fields()
        self.create_report_labels()
        self.create_result_labels()
        Button(self.calculator, text="Show Report", relief='ridge', bg='#003049', fg='white', bd=2, command=self.show_results).grid(row=14, column=3, padx=10, pady=20)

    def create_user_info_section(self):
        Label(self.calculator, text='Name:',bg='#003049',fg='white', width=10).grid(row=1, column=0, padx=10, pady=5, sticky=W)
        self.name = StringVar()
        Entry(self.calculator, width=25, relief='ridge', bd=2, textvariable=self.name).grid(row=1, column=1, pady=5, sticky=W)
        Label(self.calculator, text='Age:',bg='#003049', fg='white', width=10).grid(row=1, column=2, padx=10, pady=5, sticky=W)
        self.age = IntVar()
        Entry(self.calculator, width=15, relief='ridge', bd=2, textvariable=self.age).grid(row=1, column=3,padx=10, pady=5, sticky=W)

    def create_gender_section(self):
        Label(self.calculator, text='Gender:',bg='#003049',fg='white').grid(row=2, column=0, padx=10, pady=5, sticky=W)
        self.gender = IntVar()
        Radiobutton(self.calculator, text='Male', bg='#FDF0D5', variable=self.gender, value=1).grid(row=2, column=1, sticky=W)
        Radiobutton(self.calculator, text='Female', bg='#FDF0D5', variable=self.gender, value=2).grid(row=2, column=2, sticky=W)

    def create_entry_fields(self):
        entries = []
        for r, field in enumerate(FIELDS, start=3):
            Label(self.calculator, text=field + ':', width=30, bg='#780000', fg='white').grid(row=r, column=0, padx=10, pady=5, sticky=W)
            entry = Entry(self.calculator, justify='center', width=30, relief='ridge', bd=2)
            entry.grid(row=r, column=1, pady=5, sticky=W)
            entries.append(entry)
        return entries

    def create_report_labels(self):
        Label(self.calculator, text='Report Of', width=30, bg='#003049', fg='white').grid(row=14, column=0, padx=10, pady=10, sticky=W)

    def create_result_labels(self):
        self.bmi_calculated = StringVar()
        self.bp_calc = StringVar()
        self.pulse_calulated = StringVar()
        self.cholestrol_calculated = StringVar()
        self.wbc_final = StringVar()
        self.rbc_final = StringVar()
        self.platelets_final = StringVar()
        self.uric_acid = StringVar()
        self.haemoglobin_calc = StringVar()

        results_vars = [
            self.bmi_calculated, self.bp_calc, self.pulse_calulated,
            self.rbc_final, self.wbc_final, self.platelets_final,
            self.haemoglobin_calc, self.uric_acid, self.cholestrol_calculated
        ]

        for r, (label_text, result_var) in enumerate(zip(RESULT_LABELS, results_vars), start=15):
            Label(self.calculator, text=label_text, width=30, bg='#780000', fg='white').grid(row=r, column=0, padx=10, pady=5, sticky=W)
            Label(self.calculator, textvariable=result_var, width=30, bg='#003049', fg='white').grid(row=r, column=1, padx=10, pady=5, sticky=W)

    def show_results(self):
        if any(not entry.get() for entry in self.entries) or not self.name.get() or not self.age.get():
            messagebox.showwarning("Input Error", "Please enter all the required details.")
            return
        fitness_calc = FitnessCalculations(self.entries)
        self.bmi_calculated.set(fitness_calc.calculate_bmi())
        self.bp_calc.set(fitness_calc.blood_pressure())
        self.pulse_calulated.set(fitness_calc.pulse_rate())
        self.rbc_final.set(fitness_calc.rbc())
        self.wbc_final.set(fitness_calc.wbc_k())
        self.platelets_final.set(fitness_calc.platelet())
        self.haemoglobin_calc.set(fitness_calc.haemo())
        self.uric_acid.set(fitness_calc.urine_monitor())
        self.cholestrol_calculated.set(fitness_calc.get_cholesterol())
