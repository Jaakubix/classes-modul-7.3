class BaseContact:
    def __init__(self,imie,nazwisko,mail,nrpryw):
        self.imie = imie
        self.nazwisko = nazwisko
        self.mail = mail
        self.nrpryw = nrpryw
    def contact(self):
        print(f"Wybieram numer +48 {self.nrpryw} i dzwonię do {self.imie} {self.nazwisko}")
    def label_length(self):
        self.length = len(imie) + len(nazwisko)
        print(self.length)
class BusinessContact(BaseContact):
    def __init__(self,nrsluz,imie,nazwisko,mail):
        super().__init__(imie,nazwisko,mail)
        self.nrsluz = nrsluz
    def contact(self):
        print(f"Wybieram numer +48{self.nrsluz} i dzwonię do {self.imie} {self.nazwisko}")
    def label_length(self):
        self.length = len(imie) + len(nazwisko)
        print(self.length)