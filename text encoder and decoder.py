lista=str('aàáãbcdeéfghiíjklmnoóôõpqrstuúvwxyzABCDE')
texto=(input(str('Digite seu texto: ')))
textcod=[]
l=len(texto)
op=input('Digite 1 para codificar, ou 2 para decodificar: ')
while op!='1' and op!='2':
    print('Opção inválida.')
    op=input('Digite 1 para codificar, ou 2 para decodificar: ')
if op=='1':
    texto=texto.lower()
    mc=int(input('Você pode escolher entre 5 modos de codificação.  IMPORTANTE: para decodificar o texto posteriormente, você deverá informar qual foi o modo de codificação selecionado. Digite um número entre 1 e 5 para fazer sua opção: '))
    while mc not in (1,2,3,4,5):
        print('Opção inválida.')
        mc=int(input('Você pode escolher entre 5 modos de codificação.  IMPORTANTE: para decodificar o texto posteriormente, você deverá informar qual foi o modo de codificação selecionado. Digite um número entre 1 e 5 para fazer sua opção: '))
    for i in range(0,l):
        if texto[i]==' ':
            textcod.append('F')
        if texto[i] not in(lista) and texto[i]!=' ':
            textcod.append(texto[i])
        for c in range(0,39):
            if texto[i]==lista[c]:
                textcod.append(lista[c+mc])
            
    print(f'Esse é seu texto codificado:  ')
    for letra in range(0,l):
        print(textcod[letra], end='') 
if op=='2':
    mc=int(input('Para decodificar corretamente seu texto, informe o modo de codificação utilizado: '))
    while mc not in (1,2,3,4,5):
        print('Opção inválida.')
        mc=int(input('Para decodificar corretamente seu texto, informe o modo de codificação utilizado: '))
    for i in range(0,l):
        if texto[i]=='F':
            textcod.append(' ')
        if texto[i] not in(lista) and texto[i]!='F':
            textcod.append(texto[i])
        for c in range(0,40):
            if texto[i]==lista[c]:
                textcod.append(lista[c-mc])
    print(f'Esse é seu texto decodificado:  ')
    for letra in range(0,l):
        print(textcod[letra], end='')        

