class Doctor:
    def __init__(self, Ratio):
        self.PatientPerMinute = Ratio
        self.CurrentPatient = None
        self.TimeRemaining = 0

    def tick(self):
        if self.CurrentPatient != None:
            self.TimeRemaining = self.TimeRemaining - 1
            if round(self.TimeRemaining) == 0:
                self.CurrentPatient = None

    def busy(self):
        if self.CurrentPatient != None:
            return True
        else:
            return False

    def StartNext(self, NewPatient):
        self.CurrentPatient = NewPatient
        self.TimeRemaining = NewPatient.get_Age() / self.PatientPerMinute * 60
