decrypteur = input()
texte = input()
caractere = 0
for loop in range(len(texte)):
   caractereLu = texte[caractere]
   if caractereLu.isalpha():
      if caractereLu.isupper():
         caractereLu = decrypteur[ord(caractereLu.lower()) - ord("a")].upper()
      else:
         caractereLu = decrypteur[ord(caractereLu) - ord("a")]
   print(caractereLu, end = '')
   caractere = caractere + 1