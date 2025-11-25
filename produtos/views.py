from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Produto, Carrinho, ItemCarrinho

# LISTA DE PRODUTOS
@login_required
def lista_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'produtos/lista_produtos.html', {'produtos': produtos})

# ADICIONAR PRODUTO (CRUD Create)
@login_required
def criar_produto(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        preco = request.POST.get('preco')
        descricao = request.POST.get('descricao')

        Produto.objects.create(nome=nome, preco=preco, descricao=descricao)
        return redirect('lista_produtos')

    return render(request, 'produtos/criar_produto.html')

# REMOVER PRODUTO (CRUD Delete)
@login_required
def deletar_produto(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    produto.delete()
    return redirect('lista_produtos')


# ============================
# 🛒 CARRINHO
# ============================

@login_required
def adicionar_ao_carrinho(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)

    # cria carrinho se não existir
    carrinho, criado = Carrinho.objects.get_or_create(usuario=request.user)

    item, criado = ItemCarrinho.objects.get_or_create(
        carrinho=carrinho,
        produto=produto
    )

    if not criado:
        item.quantidade += 1
        item.save()

    return redirect('lista_produtos')

@login_required
def remover_do_carrinho(request, item_id):
    item = get_object_or_404(ItemCarrinho, id=item_id)
    item.delete()
    return redirect('ver_carrinho')

@login_required
def remover_do_carrinho_unid(request, item_id):
    item = get_object_or_404(ItemCarrinho, id=item_id)
    if item.quantidade > 1:
        item.quantidade -= 1
        item.save()
    else:
        item.delete()
    return redirect('ver_carrinho')

@login_required
def ver_carrinho(request):
    carrinho, _ = Carrinho.objects.get_or_create(usuario=request.user)
    itens = ItemCarrinho.objects.filter(carrinho=carrinho)
    return render(request, 'produtos/carrinho.html', {'itens': itens})
