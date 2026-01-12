from django.db import models

class Empleado(models.Model):
    idEmpleado = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)        # requerido
    departamento = models.CharField(max_length=100)  # requerido
    sueldo = models.DecimalField(max_digits=10, decimal_places=2)  # > 0

    class Meta:
        db_table = 'empleado'  # nombre exacto de la tabla

    def __str__(self):
        return f'{self.idEmpleado} - {self.nombre} ({self.departamento})'