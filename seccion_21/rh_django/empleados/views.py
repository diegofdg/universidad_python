from rest_framework import generics
from .models import Empleado
from .serializers import EmpleadoSerializer

class EmpleadoListCreateAPIView(generics.ListCreateAPIView):
    queryset = Empleado.objects.all().order_by('idEmpleado')
    serializer_class = EmpleadoSerializer

class EmpleadoRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer
    # lookup_field = 'pk'  # implícito; pk mapea al campo PK del modelo (idEmpleado)
