from django.shortcuts import render, get_object_or_404
from django.db.models import Q, Count, Avg
from .models import Libro, Editorial

# Create your views here.
def inicio(request):
    q = request.GET.get('q', "").strip()
    editorial_id = request.GET.get('editorial', "")

    libros = Libro.objects.select_related('editorial')

    if q:
        libros = libros.filter(Q(titulo__icontains=q) | Q(autor__icontains=q))
    if editorial_id.isdigit():
        libros = libros.filter(editorial_id=int(editorial_id))

    resumen = libros.aggregate(total=Count('id'), promedio=Avg('precio'))
    promedio = resumen['promedio'] or 0
    promedio_clp = f"${int(promedio):,}".replace(",",".")

    contexto = {
        'libros': libros,
        'editoriales': Editorial.objects.all(),
        'q': q,
        'editorial_sel': editorial_id,
        'total': resumen['total'],
        'promedio_clp': promedio_clp,
    }
    return render(request, 'catalogo/inicio.html', contexto)

def detalle(request, id):
    libro = get_object_or_404(Libro.objects.select_related('editorial'), id=id)
    return render(request, 'catalogo/detalle.html', {'libro': libro})