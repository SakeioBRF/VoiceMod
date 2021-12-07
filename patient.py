import random

class Patient:
    def __init__(self, time):
        self.TimeStamp = time
        self.Age = random.randrange(20, 61)

    def get_Stamp(self):
        return self.Time_Stamp

    def get_Age(self):
        return self.Age

    def Wait_Time(self, CurrentTime):
        return CurrentTime - self.TimeStamp
