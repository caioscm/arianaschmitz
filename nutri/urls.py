from django.urls import include, path
from nutri import views

urlpatterns = [ 
	path('', views.home, name='home'),
	path('sobre/', views.sobre, name='sobre'),
	path('contato/', views.contato, name='contato'),
	path('contato/send-message', views.send_message, name='send-message'),
	path('receitas/', views.receitas, name='receitas'),
	path('receitas/<int:receita_id>', views.receita, name='receita')
	]