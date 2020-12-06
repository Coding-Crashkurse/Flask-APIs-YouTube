class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hallo, mein name ist {self.name}")


person1 = Person(name="Markus")
person1.greet()


class Kunde(Person):
    def __init__(self, name, money):
        super().__init__(name)
        self.money = money

    def einzahlen(self, summe):
        self.money = self.money + summe

    def abheben(self, summe):
        if summe > self.money:
            print(f"Du willst {summe}, hast aber nur noch {self.money} auf dem Konto")
        else:
            self.money = self.money - summe


markus = Kunde("Markus", 2000)
markus.abheben(1500)
markus.abheben(300)
markus.abheben(500)
markus.einzahlen(1000)
