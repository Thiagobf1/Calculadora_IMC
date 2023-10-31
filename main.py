altura = float(input('Qual sua altura em cm: '))
peso = float(input('Qual seu peso em kg: '))

IMC = peso / (altura/100)**2

if IMC < 18.5: 
  print(f'Seu IMC é de {IMC}, e é classificado como Magreza')
  
elif IMC >= 18.5 and IMC <= 24.9:
  print(f'Seu IMC é de {IMC}, e é classificado como Normal')
  
elif IMC >= 25 and IMC <= 29.9:
  print(f'Seu IMC é de {IMC}, e é classificado como Sobrepeso')
  
elif IMC >= 30 and IMC <= 39.9:
  print(f'Seu IMC é de {IMC}, e é classificado como Obesidade')
  
if IMC >= 40.0:
  print(f'Seu IMC é de {IMC}, e é classificado como Obesidade Grave')