from django.db import models


class BlogPost(models.Model):
    titulo = models.CharField(max_length=200)
    assuntos = models.CharField(max_length=200)
    texto_postagem = models.TextField()
    data_postagem = models.DateTimeField('Criada em', auto_now_add=True, null=True)
    data_modificacao = models.DateTimeField('Atualizada em', auto_now=True, null=True)
    publicada = models.BooleanField(default=False)
    destaque = models.BooleanField(default=False)
    image = models.ImageField(upload_to='blog-images/%d/%m/%Y', null=True, blank=True)

    def __str__(self):
        return self.titulo
