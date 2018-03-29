blanc = 0
noir = 1
def blanchirPrexixeChangerDernier(nbJetons,couleurPrefixe):
   if nbJetons > 0:
      if couleurPrefixe == blanc:
         blanchirPrexixeChangerDernier(nbJetons-1,blanc)
      else:
         blanchirPrexixeChangerDernier(nbJetons-2,noir)
      print(nbJetons)
      blanchirPrexixeChangerDernier(nbJetons-1,blanc)
nbJetons = int(input())
blanchirPrexixeChangerDernier(nbJetons,noir)