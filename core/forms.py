from django import forms
from .models import Articulo, ListaPrecio, GrupoArticulo, LineaArticulo
from config.choices import EstadoEntidades


class ArticuloForm(forms.ModelForm):
    """Formulario para el modelo Articulo"""
    class Meta:
        model = Articulo
        fields = ['codigo_articulo', 'codigo_barras', 'descripcion', 'presentacion',
                  'grupo', 'linea', 'stock']
        widgets = {
            'codigo_articulo': forms.TextInput(attrs={'class': 'form-control'}),
            'codigo_barras': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'presentacion': forms.TextInput(attrs={'class': 'form-control'}),
            'grupo': forms.Select(attrs={'class': 'form-select'}),
            'linea': forms.Select(attrs={'class': 'form-select'}),
            'stock': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['grupo'].queryset = GrupoArticulo.objects.filter(estado=EstadoEntidades.ACTIVO)
        self.fields['linea'].queryset = LineaArticulo.objects.filter(estado=EstadoEntidades.ACTIVO)
        if not self.instance._state.adding and self.instance.grupo_id:
            self.fields['linea'].queryset = LineaArticulo.objects.filter(
                grupo_id=self.instance.grupo_id,
                estado=EstadoEntidades.ACTIVO
            )


class ListaPrecioForm(forms.ModelForm):
    """Formulario para el modelo ListaPrecio"""
    class Meta:
        model = ListaPrecio
        fields = ['precio_1', 'precio_2', 'precio_3', 'precio_4',
                  'precio_compra', 'precio_costo']
        widgets = {
            'precio_1': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'min': '0'}),
            'precio_2': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'min': '0'}),
            'precio_3': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'min': '0'}),
            'precio_4': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'min': '0'}),
            'precio_compra': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'min': '0'}),
            'precio_costo': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'min': '0'}),
        }
