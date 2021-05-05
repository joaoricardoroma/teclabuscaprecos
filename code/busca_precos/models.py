from django.db import models

class Client(models.Model):
    def __str__(self):
        return f"{self.name}, {self.cpf}, {self.rg}"

    name = models.CharField("Nome", max_length=100, null=False)
    rg = models.CharField(max_length=11, null=False)
    cpf = models.CharField(max_length=11, null=False)
    email = models.EmailField(max_length=254)
