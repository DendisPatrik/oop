class Person:
    def __init__(self, firstname, lastname, vek, gender, occupation):
        self.__firstname = firstname
        self.__lastname = lastname
        self.age = vek
        self.gender = gender
        self.occupation = occupation

    def pozdrav1(self):
        print(f"Ahoj 1 volam sa {self.__meno()} a mam {self.age} rokov")

    def pozdrav2(self):
        print(f"Ahoj 2 volam sa {self.__meno()} a mam {self.age} rokov")

    def pozdrav3(self):
        print(f"Ahoj 3 volam sa {self.__meno()} a mam {self.age} rokov")

    def __meno(self):
        return self.__firstname + " " + self.__lastname

    def zamestnanie(self):
        print(f"Ahoj volam sa {self.__name} a byvam v {self.occupation}")

    def zostarni(self, pocetrokov):
        self.age = self.age + pocetrokov

patrik = Person("Patrik", "Dendis", 30, "muz", "Programator")
# print(patrik.__name)
print(patrik.meno())











# patrik.pozdrav()
# # print(patrik.age)
# # patrik.zostarni(5)
# # print(patrik.age)


# print(patrik.age)
#
# lucia = Person("Lucia", 25, "zena", "Studentka")
# lucia.zamestnanie()