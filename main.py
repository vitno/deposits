######## Create Project & Application
## pip install django
## Create Django project => django-admin startproject visits_project
## Move to visit_projects => cd visits_project
## Create application => python manage.py startapp visit

## Create configuration Run/Debug (Parametrs = runserver)


class Deposit:
    def __init__(self, deposit: int, term: int, rate: float):
        self.deposit = deposit
        self.term = term
        self.rate = rate

    def interest(self):
        deposit = self.deposit
        for i in (1, self.term):
            deposit = deposit*(1+self.rate)
        interest = deposit-self.deposit
        return (interest)

deposit = Deposit(deposit=1000, term=2, rate=0.05)
interest = deposit.interest()
print(interest)