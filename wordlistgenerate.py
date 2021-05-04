from itertools import permutations

def listToString(s):
    str1 = ""  
    for ele in s: 
        str1 += ele  
    return str1

hedefverileri = []

a = int(input("kaç tane veri eklenecek: "))
maxLengthList = a

while len(hedefverileri) < maxLengthList:
    veri = (input("veri ekle: "))
    hedefverileri.append(veri)

perm = permutations(hedefverileri)

for i in list(perm): 
    duzyazi = listToString(i)
    dosya = open("wordlist.txt","a")
    dosya.write(duzyazi + "\n")
    print(duzyazi + "\n")
    dosya.close()

"""                                        # 1 den 1000 e kadar olan sayıları wordlist e ekleme kısmı.
for i in range(1,999+2):
    i = str(i)
    dosya = open("wordlist.txt","a")
    dosya.write(str(i+"\n"))
    print(i+"\n")
    dosya.close()
"""
