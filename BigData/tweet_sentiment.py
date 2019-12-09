chaine = "adore"
f = open("AFINN-111.txt", "r")
for line in f:
    if chaine in line:
        print line
somme  = 0
chaine = 3
for i in range(0, chaine):
    somme = somme + i
    print somme

f.close()
