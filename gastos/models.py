from django.db import models

class Departamento(models.Model):
    numero = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f"Departamento {self.numero}"

class Gasto(models.Model):
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    mes = models.PositiveIntegerField()
    año = models.PositiveIntegerField()
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    pagado = models.BooleanField(default=False)
    fecha_pago = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Gasto del Departamento {self.departamento.numero} ({self.mes}/{self.año})"
