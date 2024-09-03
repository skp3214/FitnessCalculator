class FitnessCalculations:
    def __init__(self, entries):
        self.entries = entries

    def calculate_bmi(self):
        weight = float(self.entries[0].get())
        height = float(self.entries[1].get())
        bmi = weight / (height ** 2)
        return 'Low' if bmi < 15 else 'Medium' if bmi < 20 else 'High'

    def blood_pressure(self):
        bpl = int(self.entries[2].get())
        bph = int(self.entries[3].get())
        return 'Normal' if bpl < 120 and bph < 80 else 'High'

    def pulse_rate(self):
        pulse = int(self.entries[4].get())
        return 'Low' if pulse < 72 else 'Medium' if pulse < 90 else 'High'

    def rbc(self):
        rbc = float(self.entries[5].get())
        return 'Low' if rbc < 4.32 else 'Medium' if rbc < 5.72 else 'High'

    def wbc_k(self):
        wbc = float(self.entries[6].get())
        return 'Low' if wbc < 3 else 'Medium' if wbc < 10 else 'High'

    def platelet(self):
        platelets = float(self.entries[7].get())
        return 'Low' if platelets < 150 else 'Medium' if platelets < 450 else 'High'

    def haemo(self):
        haemoglobin = float(self.entries[8].get())
        return 'Low' if haemoglobin < 13 else 'Medium' if haemoglobin < 16 else 'High'

    def urine_monitor(self):
        urine = float(self.entries[9].get())
        return 'Low' if urine < 4 else 'Medium' if urine < 8.5 else 'High'

    def get_cholesterol(self):
        cholesterol = float(self.entries[10].get())
        return 'Low (Good)' if cholesterol < 200 else 'Medium' if cholesterol < 239 else 'High'
