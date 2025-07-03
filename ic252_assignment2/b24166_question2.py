import random

class birthdaySimulation:
    def __init__(self, days=365, testcases=1000):
        self.days = days
        self.testcases = testcases
    def runSimulation(self):
        totalpeople = 0
        for _ in range(self.testcases):
            people = 0
            birthdays = set()
            while len(birthdays)<self.days:
                birthday = random.randint(1, self.days)
                birthdays.add(birthday)
                people+=1
            totalpeople += people
        return totalpeople/self.testcases

x = birthdaySimulation(366)
average_people = x.runSimulation()
print(average_people)

