chaine = "adore"
f = open("AFINN-111.txt", "r")
for line in f:
    if chaine in line:
        print line

f.close()
