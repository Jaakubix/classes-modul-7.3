from faker import Faker
fake_data = Faker()
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
def create_contacts():
    x = int(input("Podaj rodzaj wizytowki 1-BaseContact  2-BusinessContact: "))
    y = int(input("Podaj ilosc danych, ktore maja zostac wygenerowane"))
    for _ in range(y):
        if x == 1:
            BaseContact.imie = fake_data.first_name()
            BaseContact.nazwisko = fake_data.last_name()
            BaseContact.mail = fake_data.safe_email()
            BaseContact.nrpryw = fake_data.phone_number()
        else:
            BaseContact.imie = fake_data.first_name()
            BaseContact.nazwisko = fake_data.last_name()
            BaseContact.mail = fake_data.safe_email()
            BusinessContact.nrsluz = fake_data.phone_number()