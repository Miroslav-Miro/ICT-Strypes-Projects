class Person:
    def __init__(self, age):
        self.age = age

    def drink(self):
        return "drinking"

    def drive(self):
        return "driving"

    def drink_and_drive(self):
        return "driving while drunk"


class ResponsiblePerson:
    def __init__(self, person):
        self.person = person
        self._drive_calls = 0

    def drink(self):
        if self.person.age < 18:
            return "too young"
        return self.person.drink()

    def drive(self):
        self._drive_calls += 1

        if self.person.age == 10:
            if self._drive_calls == 1:
                return "too young"
            else:
                return self.person.drive()

        if self.person.age < 16:
            return "too young"

        return self.person.drive()

    def drink_and_drive(self):
        return "dead"
