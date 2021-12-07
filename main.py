import random
from pythonds.basic.queue import Queue
from patient import Patient
from doctor import Doctor

def NewPatient():
    if random.randrange(1, 361) == 360:
        return True
    else:
        return False

def Simulation(WorkTime, PatientPerMinute):
    ClinicDoctor = Doctor(PatientPerMinute)
    WaitingHall = Queue()
    WaitingTime = []

    for CurrentSecond in range(WorkTime):
        if NewPatient():
            patient = Patient(CurrentSecond)
            WaitingHall.enqueue(patient)

        if ((not ClinicDoctor.busy()) and (not WaitingHall.isEmpty())):
            NextPatient = WaitingHall.dequeue()
            WaitingTime.append(NextPatient.Wait_Time(CurrentSecond))
            ClinicDoctor.StartNext(NextPatient)

        ClinicDoctor.tick()

    AverageWait = (sum(WaitingTime) / len(WaitingTime)) / 60
    print("Average time = ", "{:.2f}".format(AverageWait),"Min\t\t\t\t",WaitingHall.size(),"Patients remaining")

for i in range(10):
    Simulation(14400, 5)
