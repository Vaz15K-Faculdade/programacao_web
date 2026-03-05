from django.db import models


# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length=50, unique=True, blank=False)
    descricao = models.TextField(max_length=150, blank=False)
    imagem = models.ImageField(upload_to="fotos/categoria", blank=True)
    slug = models.SlugField(max_length=90, unique=True)

    def __str__(self):
        return self.nome
