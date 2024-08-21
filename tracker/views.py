from django.shortcuts import render,redirect
from .models import Expensehistory,CurrentBalance
# Create your views here.

def index(request):
    if request.method=="POST":
        description=request.POST.get('description')
        amount=int(request.POST.get('amount'))
        if(amount>0):
            expense_type='credit'
        else:
             expense_type='debit'  
        currentbal,_=CurrentBalance.objects.get_or_create(id=1)
        currentbal.Balance=currentbal.Balance+amount
        currentbal.save()
        Expensehistory.objects.create(amount=amount,expense_type=expense_type,description=description,Balance=currentbal)
        return redirect("/")
    current_balance, _ = CurrentBalance.objects.get_or_create(id = 1)
    income = 0
    expense = 0  
    for history in Expensehistory.objects.all():
        if(history.expense_type=="credit"):
            income+=history.amount
        else:
            expense+=abs(history.amount)
    transactions=Expensehistory.objects.all()
    context={'transactions':transactions,'income':income,'expense':expense,'balance':current_balance.Balance}

    return render(request,"index.html",context)


def delete_transaction(request,pk):
    track_history=Expensehistory.objects.filter(pk=pk)
    current_balance, _ = CurrentBalance.objects.get_or_create(id = 1)
    if(track_history[0].expense_type=='credit'):
          current_balance.Balance-=track_history[0].amount
          current_balance.save()
    else:
        current_balance.Balance+=abs(track_history[0].amount)
        current_balance.save()    
    
    track_history[0].delete()
    return redirect("/")



