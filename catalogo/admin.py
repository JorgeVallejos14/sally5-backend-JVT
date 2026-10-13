from django.contrib import admin
from .models import Editorial, Libro

admin.site.site_header = "Administracion de la Libreria"
admin.site.site_title = "Libreria de Acorn"
admin.site.index_title = "Gestion del catalogo"


@admin.register(Editorial)
class EditorialAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'pais', 'fundada', 'activa', 'total_libros')
    list_filter = ('activa', 'pais')
    search_fields = ('nombre', 'pais')

    @admin.display(description='Libros')
    def total_libros(self, obj):
        return obj.libros.count()


@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'editorial', 'genero', 'paginas',
                    'precio_formateado', 'disponible')
    list_filter = ('genero', 'editorial', 'disponible')
    search_fields = ('titulo', 'autor')
    list_editable = ('disponible',)
    list_select_related = ('editorial',)
    actions = ['marcar_disponible', 'marcar_agotado']

    @admin.display(description='Precio', ordering='precio')
    def precio_formateado(self, obj):
        return obj.precio_clp

    @admin.action(description="Marcar como disponibles")
    def marcar_disponible(self, request, queryset):
        n = queryset.update(disponible=True)
        self.message_user(request, f"{n} libros marcados como disponibles")

    @admin.action(description="Marcar como agotados")
    def marcar_agotado(self, request, queryset):
        n = queryset.update(disponible=False)
        self.message_user(request, f"{n} libros marcados como agotados")