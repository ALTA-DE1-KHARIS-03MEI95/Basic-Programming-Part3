def bil():

  bilangan = int(input("Input: "))

  faktor = []
  for i in range(1, bilangan+1):
    if bilangan % i == 0:
      faktor.append(i)
  
  for f in reversed(faktor):
    print(f)
bil()