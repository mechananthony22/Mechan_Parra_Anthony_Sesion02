from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
import uuid
from .models import Articulo, GrupoArticulo, LineaArticulo, ListaPrecio
from .forms import ArticuloForm, ListaPrecioForm


@login_required
def home(request):
    """Vista para el Dashboard principal"""
    total_encomiendas = Articulo.objects.count()
    total_clientes = 0
    en_ruta = Articulo.objects.filter(stock__lt=10).count()
    context = {
        'total_encomiendas': total_encomiendas,
        'total_clientes': total_clientes,
        'en_ruta': en_ruta,
        'envios_hoy': 0,
    }
    return render(request, 'core/index.html', context)


@login_required
def encomiendas_list(request):
    """Vista para listar encomiendas"""
    encomiendas_list = Articulo.objects.all()
    q = request.GET.get('q')
    if q:
        encomiendas_list = encomiendas_list.filter(descripcion__icontains=q)
    paginator = Paginator(encomiendas_list, 15)
    page_number = request.GET.get('page')
    encomiendas = paginator.get_page(page_number)
    context = {
        'encomiendas': encomiendas,
    }
    return render(request, 'encomiendas/list.html', context)


@login_required
def encomienda_detail(request, articulo_id):
    """Vista para ver el detalle de una encomienda"""
    encomienda = get_object_or_404(Articulo, articulo_id=articulo_id)
    context = {
        'encomienda': encomienda,
    }
    return render(request, 'encomiendas/detail.html', context)


@login_required
def encomienda_create(request):
    """Vista para crear una nueva encomienda"""
    if request.method == 'POST':
        form = ArticuloForm(request.POST)
        precio_form = ListaPrecioForm(request.POST)
        if form.is_valid() and precio_form.is_valid():
            encomienda = form.save(commit=False)
            encomienda.articulo_id = uuid.uuid4()
            encomienda.save()
            lista_precio = precio_form.save(commit=False)
            lista_precio.articulo = encomienda
            lista_precio.save()
            messages.success(request, 'Encomienda creada correctamente.')
            return redirect('encomienda_detail', articulo_id=encomienda.articulo_id)
    else:
        form = ArticuloForm()
        precio_form = ListaPrecioForm()
    context = {
        'form': form,
        'precio_form': precio_form,
    }
    return render(request, 'encomiendas/form.html', context)


@login_required
def encomienda_edit(request, articulo_id):
    """Vista para editar una encomienda existente"""
    encomienda = get_object_or_404(Articulo, articulo_id=articulo_id)
    lista_precio = get_object_or_404(ListaPrecio, articulo=encomienda)
    if request.method == 'POST':
        form = ArticuloForm(request.POST, instance=encomienda)
        precio_form = ListaPrecioForm(request.POST, instance=lista_precio)
        if form.is_valid() and precio_form.is_valid():
            form.save()
            precio_form.save()
            messages.success(request, 'Encomienda actualizada correctamente.')
            return redirect('encomienda_detail', articulo_id=encomienda.articulo_id)
    else:
        form = ArticuloForm(instance=encomienda)
        precio_form = ListaPrecioForm(instance=lista_precio)
    context = {
        'form': form,
        'precio_form': precio_form,
    }
    return render(request, 'encomiendas/form.html', context)


@login_required
def encomienda_delete(request, articulo_id):
    """Vista para eliminar una encomienda"""
    encomienda = get_object_or_404(Articulo, articulo_id=articulo_id)
    if request.method == 'POST':
        encomienda.delete()
        messages.success(request, 'Encomienda eliminada correctamente.')
        return redirect('encomiendas_list')
    context = {
        'encomienda': encomienda,
    }
    return render(request, 'encomiendas/delete.html', context)


@login_required
def grupos_list(request):
    """Vista para listar grupos y líneas"""
    grupos = GrupoArticulo.objects.filter(estado=1)
    lineas = LineaArticulo.objects.filter(estado=1)
    context = {
        'grupos': grupos,
        'lineas': lineas,
    }
    return render(request, 'grupos/list.html', context)


@login_required
def grupo_detail(request, grupo_id):
    """Vista para ver detalle de un grupo"""
    grupo = get_object_or_404(GrupoArticulo, grupo_id=grupo_id)
    context = {
        'grupo': grupo,
    }
    return render(request, 'grupos/detail.html', context)


@login_required
def get_lineas_por_grupo(request, grupo_id):
    """API para obtener líneas según el grupo seleccionado"""
    lineas = LineaArticulo.objects.filter(grupo=grupo_id, estado=1)
    data = [{'id': str(linea.linea_id), 'nombre': linea.nombre_linea} for linea in lineas]
    return JsonResponse(data, safe=False)
