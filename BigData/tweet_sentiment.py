#chaine = ["adore", "admire"]
chaine = "admire"
chaine = "love"
f = open("AFINN-111.txt", "r")
for line in f:
    if chaine in line > 3:
            print line
somme  = 0
chaine = 4
for i in range(0, chaine):
    somme = somme + i
    print somme

f.close()
