from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=20)

    class Meta:
        db_table = "users"

class Accounts(models.Model):
    bank_name=models.CharField(max_length=50)
    account_no=models.IntegerField()
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="user_accounts")

    def __str__(self):
        d={"bank_name":self.bank_name,"account_no":self.account_no}
        print(d)
        return f'{d}'
