from django.db import models

# Create your models here.
class Editorial(models.Model):
    nombre = models.CharField(max_length=80, unique=True)
    pais = models.CharField(max_length=60)
    fundada = models.PositiveSmallIntegerField()
    activa = models.BooleanField(default=True)


    class Meta:
        ordering = ['nombre']

    def __str__(self):
        return self.nombre


class Libro(models.Model):
    GENEROS = [
        ('aventura', 'Aventura'),
        ('historia', 'Historia'),
        ('ciencia', 'Ciencia'),
        ('estrategia', 'Estrategia'),
    ]


    editorial = models.ForeignKey(
        Editorial,
        on_delete=models.PROTECT,
        related_name='libros',
    )
    titulo = models.CharField(max_length=120)
    autor = models.CharField(max_length=80)
    genero = models.CharField(max_length=15, choices=GENEROS)
    paginas = models.PositiveSmallIntegerField()
    precio = models.PositiveIntegerField()
    disponible = models.BooleanField(default=True)
    sinopsis = models.TextField(blank=True)

    class Meta:
        ordering = ['titulo']

    def __str__(self):
        return self.titulo

    @property
    def precio_clp(self):
        return f"${self.precio:,}".replace(",",".")