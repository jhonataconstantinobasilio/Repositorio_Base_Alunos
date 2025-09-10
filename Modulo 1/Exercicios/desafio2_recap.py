nome= input('qual é o seu nome' )

o_que_você_quer_fazer= input('digite o que você quer fazer')

ativivdade1='quero viajar'

ativiade2=('quero ler um livro','\n')

atividade3='volei '



atividade4=('quero descansar','\n')


if 'viajar' in o_que_você_quer_fazer  :
    print('ok, que tal viajarmos para o Rio de Jameiro ?')


elif o_que_você_quer_fazer=='quero ler um livro':
    print('ok, sugiro que voc~e leia Pequeno Principe é uma otima historia')


elif  atividade3 in o_que_você_quer_fazer :
    print('blz, você quer jogar no campo ou na quadra de futsal ?')


elif o_que_você_quer_fazer in ativivdade1:
    print('blz, sente-se no sofa para descansar')    

else:
    print('ok, você gostaria de fazer algo neste mês ?')