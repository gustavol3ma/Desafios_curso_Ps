produtos ={
    'feijão' : 2 , 
    'arroz'  : 5  ,
    'macarrão' : 3 ,
}
maior_preço = ''
if produtos.get('feijão') > produtos.get ('arroz'):
    maior_preço = 'Feijão'
elif produtos.get('feijão') > produtos.get('macarrão'):
    maior_preço = 'Feijão'
else:
    maior_preço = 'Macarrão'

print('O produto com maior preço é o',maior_preço)