#ΚΑΠΟΙΑ PRINT() ΣΕ ΟΛΕΣ ΤΙΣ ΕΡΓΑΣΙΕΣ ΤΑ ΕΧΩ ΒΑΛΕΙ ΣΕ ΣΧΟΛΙΟ ΓΙΑΤΙ ΜΠΟΡΕΙ ΝΑ ΜΗΝ ΕΙΝΑΙ
#ΤΟΣΟ ΑΠΑΡΑΙΤΗΤΑ ΓΙΑ ΝΑ ΤΑ ΕΜΦΑΝΙΣΩ ΚΑΙ ΔΕΝ ΗΘΕΛΑ ΝΑ ΥΠΑΡΧΟΥΝ ΠΟΛΛΑ ΣΤΗΝ ΟΘΟΝΗ ΚΑΙ ΚΟΥΡΑΖΟΥΝ
#ΟΠΟΤΕ ΑΝ ΘΕΛΕΤΕ ΜΠΟΡΕΙΤΕ ΝΑ ΤΑ ΕΚΤΕΛΕΣΕΤΕ ΑΝ ΤΟ ΚΡΙΝΕΤΕ ΑΝΑΓΚΑΙΟ


file=open("keimeno2.txt", "r")


a=file.read()
print("\n","\n","Arxikh morfh keimenou:","\n","\n",a)


#ΛΙΣΤΑ 'b' ΜΕ ΚΑΘΕ ΧΑΡΑΚΤΗΡΑ ΞΕΧΩΡΙΣΤΑ
b=list(a)
print("\n","\n","Lista 'b' me kathe xaraktira jexwrista:","\n","\n",b)


#ΛΙΣΤΑ 'c' ΜΕ ΚΑΘΕ ΧΑΡΑΚΤΗΡΑ ΣΕ ΔΥΑΔΙΚΗ ΜΟΡΦΗ ΜΗΚΟΥΣ 7
c=[]
x=len(b)


#MΕΤΑΤΡΟΠΗ ΚΑΘΕ ΧΑΡΑΚΤΗΡΑ ΣΤΟΝ ΔΕΚΑΔΙΚΟ ΑΡΙΘΜΟ ΠΟΥ ΤΟΥΣ ΑΝΤΙΣΤΙΧΕΙ ΣΤΟ ASCII
for i in range (x):
    c.append(ord(b[i]))
 
 
#ΜΕΤΑΤΡΟΠΗ ΚΑΘΕ ΑΡΙΘΜΟΥ ΣΤΗΝ ΔΥΑΔΙΚΗ ΤΟΥ ΜΟΡΦΗ
for i in range (x):
    c[i]=bin(c[i])[2:]


#ΣΥΜΠΛΗΡΩΣΗ ΤΟΥ 0 ΣΤΗΝ ΑΡΧΗ ΟΠΟΥ ΕΙΝΑΙ ΑΝΑΓΚΑΙΟ ΓΙΑ ΝΑ ΕΙΝΑΙ ΜΗΚΟΣ 7 ΧΩΡΙΣ ΝΑ ΜΕΤΑΒΛΗΘΕΙ Η ΑΡΧΙΚΗ ΤΙΜΗ 
for i in range(x):
    if len(c[i])==1:
       c[i]='000000'+c[i]
    if len(c[i])==2:
       c[i]='00000'+c[i]  
    if len(c[i])==3:
       c[i]='0000'+c[i]
    if len(c[i])==4:
       c[i]='000'+c[i]
    if len(c[i])==5:
       c[i]='00'+c[i]
    if len(c[i])==6:
       c[i]='0'+c[i]    

 
print("\n","\n","Lista 'c' me kathe xaraktira se dyadikh morfh mhkous 7:","\n","\n",c)


akolouthia0=0 #Akolouthia 0 mexri na emfanistei to 1
akolouthia1=0 #Akolouthia 1 mexri na emfanistei to 0
max0=0 #Megalyterh akolouthia 0
max1=0 #Megalyterh akolouthia 1

#ΜΕΤΑΤΡΟΠΗ ΣΕ STRING
e="".join(c)
y=len(e)


print("\n","\n","Apeikonish 'e' kathe dyadikhs timhs enwmenh:","\n","\n",e,"\n","\n")
print("Mhkos 'e' =",y,"\n","\n")


#ΕΥΡΕΣΗ ΜΕΓΑΛΥΤΕΡΗΣ ΑΚΟΛΟΥΘΙΑΣ 0
for i in range (y):
    if e[i]=="0":
       akolouthia0=akolouthia0+1
       #print("twrinh akolouthia0 = ",akolouthia0)
    else:       
       if akolouthia0>max0:
          max0=akolouthia0
          #print("twrino max0 = ",max0)
       akolouthia0=0      


#ΕΥΡΕΣΗ ΜΕΓΑΛΥΤΕΡΗΣ ΑΚΟΛΟΥΘΙΑΣ 1
for i in range (y):
    if e[i]=="1":
       akolouthia1=akolouthia1+1
       #print("twrinh akolouthia1 = ",akolouthia1)
    else:       
       if akolouthia1>max1:
          max1=akolouthia1
          #print("twrino max1 = ",max1)
       akolouthia1=0      


print("\n","\n","\n")
print("Megalyterh akolouthia 0 =",max0)
print("Megalyterh akolouthia 1 =",max1)