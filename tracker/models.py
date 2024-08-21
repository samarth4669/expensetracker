from django.db import models

# Create your models here.

class CurrentBalance(models.Model):
    Balance=models.FloatField(default=0)
class Expensehistory(models.Model):
    Balance=models.ForeignKey(CurrentBalance,on_delete=models.CASCADE)
    amount=models.FloatField()
    description=models.TextField()
    expense_type=models.CharField(choices=(('credit','credit'),('debit','debit')),max_length=50)
    created_at=models.DateTimeField(auto_now_add=True)

