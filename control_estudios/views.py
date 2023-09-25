from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from control_estudios.forms import CursoFormulario
from control_estudios.models import Curso, Estudiante

# Vistas de cursos
def listar_cursos(request):
    contexto = {
        "cursos": Curso.objects.all(),
    }
    return render(request, 'control_estudios/lista_cursos.html', contexto)

def crear_curso(request):
    if request.method == "POST":
        formulario = CursoFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            nombre = data['nombre']
            comision = data['comision']

            curso = Curso(nombre=nombre, comision=comision)
            curso.save()

            return redirect('lista_cursos')
    
    else:  # GET
        formulario = CursoFormulario()

    return render(
        request=request,
        template_name='control_estudios/formulario_curso.html',
        context={'formulario': formulario}
    )

def buscar_cursos(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        cursos = Curso.objects.filter(comision__contains=busqueda)
        contexto = {
            "cursos": cursos,
        }
        return render(request, 'control_estudios/lista_cursos.html', contexto)

def eliminar_curso(request, id):
    curso = Curso.objects.get(id=id)
    if request.method == "POST":
        curso.delete()
        return redirect('lista_cursos')

def editar_curso(request, id):
    curso = Curso.objects.get(id=id)
    if request.method == "POST":
        formulario = CursoFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            curso.nombre = data['nombre']
            curso.comision = data['comision']
            curso.save()
            return redirect('lista_cursos')
    else:  # GET
        inicial = {
            'nombre': curso.nombre,
            'comision': curso.comision,
        }
        formulario = CursoFormulario(initial=inicial)
    return render(
        request=request,
        template_name='control_estudios/formulario_curso.html',
        context={'formulario': formulario},
    )

# Vistas de Estudiantes
class EstudianteListView(ListView):
    model = Estudiante
    template_name = 'control_estudios/lista_estudiantes.html'

class EstudianteCreateView(CreateView):
    model = Estudiante
    fields = ('apellido', 'nombre', 'email', 'dni')
    success_url = reverse_lazy('lista_estudiantes')
    template_name = 'control_estudios/estudiante_forms.html'  

class EstudianteDetailView(DetailView):
    model = Estudiante
    success_url = reverse_lazy('lista_estudiantes')

class EstudianteUpdateView(UpdateView):
    model = Estudiante
    fields = ('apellido', 'nombre', 'email', 'dni')
    success_url = reverse_lazy('lista_estudiantes')

class EstudianteDeleteView(DeleteView):
    model = Estudiante
    success_url = reverse_lazy('lista_estudiantes')
