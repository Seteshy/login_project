from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_produtos, name='lista_produtos'),
    path('criar/', views.criar_produto, name='criar_produto'),
    path('deletar/<int:produto_id>/', views.deletar_produto, name='deletar_produto'),

    # CARRINHO
    path('carrinho/', views.ver_carrinho, name='ver_carrinho'),
    path('carrinho/add/<int:produto_id>/', views.adicionar_ao_carrinho, name='adicionar_ao_carrinho'),
    path('carrinho/remove/<int:item_id>/', views.remover_do_carrinho, name='remover_do_carrinho'),
    path('carrinho/remove_unid/<int:item_id>/', views.remover_do_carrinho_unid, name='remover_do_carrinho_unid'),
]
