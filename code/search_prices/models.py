from django.db import models


class Client(models.Model):
    def __str__(self):
        return f"{self.name}, {self.cpf}, {self.rg}"

    name = models.CharField("Nome", max_length=100, null=False)
    rg = models.CharField(max_length=11, null=False)
    cpf = models.CharField(max_length=11, null=False)
    email = models.EmailField(max_length=254)


class Search(models.Model):
    def __str__(self):
        return f'{self.search}, {self.site}, {self.periodicidade}'

    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    search = models.CharField(max_length=254, null=False)
    site = models.CharField(max_length=254, null=False, choices=[
        ("Kabum", "KABUM"),
    ])
    periodicidade = models.IntegerField(choices=[
        (24, "todo dia"),
        (12, "duas vezes ao dia"),
        (6, "quatro vezes ao dia"),
    ])
