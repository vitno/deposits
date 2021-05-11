from django.shortcuts import render, redirect
from django.views.generic import ListView, View, FormView, DetailView
from deposits_app.models import DepositModel
from deposits_app.forms import DepositForm
from django.urls import reverse_lazy


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


class DepositListView(ListView):

    model = DepositModel
    template_name = 'deposit_list.html'

class DepositDetailView(DetailView):

    model = DepositModel
    template_name = 'deposit_detail.html'

class CreateDeposit(View):

    def get(self, request):

        return render(
            template_name='make_deposit.html',
            request=request,
        )

    def post(self, request):

        deposit = int(request.POST['deposit'])
        term = int(request.POST['term'])
        rate = float(request.POST['rate'])
        new_deposit = Deposit(deposit=deposit, term=term, rate=rate)
        interest = new_deposit.interest()

        dep = DepositModel(
            deposit=deposit,
            term=term,
            rate=rate,
            interest=interest
        )
        dep.save()

        return redirect(reverse_lazy('deposits-list'))
