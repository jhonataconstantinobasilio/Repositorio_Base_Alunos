palavra = 'gabriel'
contador =0

for item in palavra:
   
   if item in 'aeiou':
    print(item,'é vogal',contador)
    
    contador=contador+1
    print(contador)
   else:
      print(item,'é consoante')   
