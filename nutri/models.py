from django.db import models


class ReceitasManager(models.Manager):

	def search(self, query):
		return self.get_queryset().filter(models.Q(name__icontains=query) | models.Q(description__icontains=query))

class Receitas(models.Model):

	name = models.CharField('Nome', null=True, max_length=100)
	slug = models.SlugField('Palavra-chave', null=True)
	disclaimer = models.TextField('Resumo', default='Receita prática e nutritiva.')
	ingredientes = models.TextField('Ingredientes', null=True, blank=True)
	modo_preparo = models.TextField('Modo de Preparo', null=True)

	image = models.ImageField(upload_to='fotos/%d/%m/%y', null=True, verbose_name='imagem', blank=True)

	created_at = models.DateTimeField('Criado em', auto_now_add=True, null=True)

	update_at = models.DateTimeField('Atualizado em', auto_now=True, null=True)

	objects = ReceitasManager()

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "Receita"
		verbose_name_plural = "Receitas"
		ordering = ['update_at']

class Mensagens(models.Model):
	nome = models.CharField(max_length=200)
	email = models.EmailField()
	mensagem = models.TextField()
	data_envio = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.email