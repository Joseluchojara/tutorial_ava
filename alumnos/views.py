from django.shortcuts import render

from .models import Alumno,Genero
def index(request):
    Alumnos= Alumno.objects.all()
    context={"alumnos": Alumnos}
    return render(request,'alumnos/index.html',context)

def listadoSQL(request):
    Alumnos= Alumno.objects.raw('select * from Alumnos_Alumno')
    print(Alumnos)
    context={"alumnos": Alumnos}
    return render(request,'alumnos/listadoSQL.html', context)
