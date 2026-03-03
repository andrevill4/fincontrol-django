from django.db import models

class Categoria(models.Model):
    nome=models.CharField(max_length=50)

    def __str__(self):
        return self.nome
    
class Transacao(models.Model):

    TIPO_CHOICES = (
        ('R', 'Receita'),
        ('D', 'Despesa'),
    )

    descricao = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    tipo = models.CharField(max_length=1, choices=TIPO_CHOICES)
    data = models.DateField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.descricao
