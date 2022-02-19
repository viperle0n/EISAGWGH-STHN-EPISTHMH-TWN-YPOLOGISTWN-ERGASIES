#ΚΑΠΟΙΑ PRINT() ΣΕ ΟΛΕΣ ΤΙΣ ΕΡΓΑΣΙΕΣ ΤΑ ΕΧΩ ΒΑΛΕΙ ΣΕ ΣΧΟΛΙΟ ΓΙΑΤΙ ΜΠΟΡΕΙ ΝΑ ΜΗΝ ΕΙΝΑΙ
#ΤΟΣΟ ΑΠΑΡΑΙΤΗΤΑ ΓΙΑ ΝΑ ΤΑ ΕΜΦΑΝΙΣΩ ΚΑΙ ΔΕΝ ΗΘΕΛΑ ΝΑ ΥΠΑΡΧΟΥΝ ΠΟΛΛΑ ΣΤΗΝ ΟΘΟΝΗ ΚΑΙ ΚΟΥΡΑΖΟΥΝ
#ΟΠΟΤΕ ΑΝ ΘΕΛΕΤΕ ΜΠΟΡΕΙΤΕ ΝΑ ΤΑ ΕΚΤΕΛΕΣΕΤΕ ΑΝ ΤΟ ΚΡΙΝΕΤΕ ΑΝΑΓΚΑΙΟ


import urllib.request
from urllib.request import Request, urlopen


#ΠΡΟΣΒΑΣΗ ΣΤΗΝ ΙΣΤΟΣΕΛΙΔΑ ΚΑΙ ΑΠΟΚΤΗΣΗ ΣΤΟΙΧΕΙΩΝ
url=Request("https://drand.cloudflare.com/public/latest", headers={'User-Agent': 'Mozilla/5.0'})
x=urllib.request.urlopen(url)
webpage=x.read()
print("\n","\n",webpage)


#ΜΕΤΑΤΡΟΠΗ ΚΑΘΕ ΧΑΡΑΚΤΗΡΑ ΣΤΟΝ ΑΝΤΙΣΤΟΙΧΟ ΔΕΚΑΔΙΚΟ ΑΡΙΘΜΟ ASCII ΚΑΙ ΚΑΤΑΧΩΡΗΣΗ ΣΤΗΝ ΛΙΣΤΑ 'a'
a=list(webpage)
y=len(a)
#print(a)


#ΜΕΤΑΤΡΟΠΗ ΚΑΘΕ ΔΕΚΑΔΙΚΟΥ ΑΡΙΘΜΟΥ ΣΤΟΝ ΑΝΤΙΣΤΟΙΧΟ ΧΑΡΑΚΤΗΡΑ ΚΑΙ ΚΑΤΑΧΩΡΗΣΗ ΤΟΥ ΣΤΗΝ ΛΙΣΤΑ 'b'
b=[]
for i in range (y):
    b.append(chr(a[i]))
#print(b)


#ΕΥΡΕΣΗ ΤΕΛΕΥΤΑΙΟΥ ΓΥΡΟΥ
z="".join(b[9:16])


#ΕΥΡΕΣΗ RANDOMNESS ΤΟΥ ΤΕΛΕΥΤΑΙΟΥ ΓΥΡΟΥ ΚΑΙ ΠΡΟΣΘΗΚΗ ΤΟΥ ΣΤΗΝ ΛΙΣΤΑ 'times'
times=[]
s="".join((b[31:95]))
times.append(s)


print("\n","\n","Teleftaios gyros =",z,)
print("\n","\n","Randomness teleftaiou gyrou =",times[0],"\n","\n",)


#ΑΜΕΤΑΒΛΗΤΟ LINK ΓΙΑ ΧΡΗΣΗ ΜΕΤΑΒΑΛΛΩΝΤΑΣ ΤΟΝ ΓΥΡΟ ΣΤΗΝ ΕΠΑΝΑΛΗΨΗ
monimo="https://drand.cloudflare.com/public/"

    
#ΕΥΡΕΣΗ RANDOMNESS ΤΩΝ ΤΕΛΕΥΤΑΙΩΝ 99 ΓΥΡΩΝ (ΑΦΟΥ ΕΧΟΥΜΕ ΒΡΕΙ ΗΔΗ ΤΟΥ ΤΕΛΕΥΤΑΙΟΥ)
for i in range (1,100):
    #ΜΕΤΑΤΡΟΠΗ Ζ ΣΕ ΑΚΕΡΑΙΟ ΓΙΑ ΝΑ ΜΠΟΡΕΣΟΥΜΕ ΝΑ ΑΦΕΡΑΙΣΟΥΜΕ 1 ΓΙΑ ΝΑ ΑΛΛΑΞΕΙ Ο ΓΥΡΟΣ
    gyros1=int(z)-1
    #print("Twrinos gyros=",gyros1)
    
    
    #ΜΕΤΑΤΡΟΠΗ ΤΩΡΙΝΟΥ ΓΥΡΟΥ ΣΕ STRING ΓΙΑ ΝΑ ΜΠΟΡΕΣΟΥΜΕ ΝΑ ΤΟ ΠΡΟΣΘΕΣΟΥΜΕ ΣΤΟ ΜΟΝΙΜΟ LINK
    gyros2=str(gyros1)
    
    
    #ΤΟ 'k' ΕΙΝΑΙ ΤΟ ΟΛΟΚΛΗΡΩΜΕΝΟ LINK ΤΟΥ ΓΥΡΟΥ ΠΟΥ ΘΕΛΟΥΜΕ
    k=monimo+gyros2
    
    
    #ΚΑΤΑΧΩΡΗΣΗ ΤΟΥ ΓΥΡΟΥ ΣΤΗΝ 'z'
    z=gyros2
    
    
    #ΠΡΟΣΒΑΣΗ ΣΤΗΝ ΙΣΤΟΣΕΛΙΔΑ ΤΟΥ ΤΩΡΙΝΟΥ ΓΥΡΟΥ ΚΑΙ ΑΠΟΚΤΗΣΗ ΣΤΟΙΧΕΙΩΝ
    #ΟΥΣΙΑΣΤΙΚΑ ΕΚΤΕΛΟΥΜΕ ΤΗΝ ΙΔΙΑ ΔΙΑΔΙΚΑΣΙΑ ΜΕ ΠΡΙΝ ΑΠΛΑ ΓΙΑ ΤΟΥΣ ΥΠΟΛΟΙΠΟΥΣ ΓΥΡΟΥΣ
    url=Request(k, headers={'User-Agent': 'Mozilla/5.0'})
    x=urllib.request.urlopen(url)
    webpage=x.read()
    #print(webpage)
    
    
    a=list(webpage)
    y=len(a)
    #print(a)
    
    
    b=[]
    for i in range (y):
        b.append(chr(a[i]))


   
    s="".join((b[31:95]))
    times.append(s)


print("\n","\n","Lista 'times' twn teleftaiwn 100 timwn randomness:","\n","\n",times,"\n","\n")


#ΜΕΤΑΤΡΟΠΗ ΤΗΣ ΛΙΣΤΑΣ 'times' ΣΕ ΕΝΙΑΙΟ STRING 
d="".join(times)
#print(d)


#ΚΑΤΑΧΩΡΗΣΗ ΚΑΘΕ ΧΑΡΑΚΤΗΡΑ ΞΕΧΩΡΙΣΤΑ ΣΤΗΝ ΛΙΣΤΑ 'v'
v=list(d)
print("\n","\n","Lista 'v' twn timwn randomness me kathe xaraktira jexwrista:","\n","\n",v,"\n","\n")
r=len(v)


c=[]
#MΕΤΑΤΡΟΠΗ ΚΑΘΕ ΧΑΡΑΚΤΗΡΑ ΣΤΟΝ ΔΕΚΑΔΙΚΟ ΑΡΙΘΜΟ ΠΟΥ ΤΟΥΣ ΑΝΤΙΣΤΙΧΕΙ ΣΤΟ ASCII ΚΑΙ ΕΚΧΩΡΗΣΗ ΣΤΗΝ ΛΙΣΤΑ 'c'
for i in range (r):
    c.append(ord(v[i]))
 
 
#ΜΕΤΑΤΡΟΠΗ ΚΑΘΕ ΔΕΚΑΔΙΚΟΥ ΑΡΙΘΜΟΥ ΣΤΗΝ ΔΥΑΔΙΚΗ ΤΟΥ ΜΟΡΦΗ ΚΑΙ ΕΚΧΩΡΗΣΗ ΣΤΗΝ ΛΙΣΤΑ 'c'
for i in range (r):
    c[i]=bin(c[i])[2:]


print("\n","\n","Lista 'c' apeikonisews toy kathe xarakthra se dyadikh morfh:","\n","\n",c,"\n","\n")


akolouthia0=0 #Akolouthia 0 mexri na emfanistei to 1
akolouthia1=0 #Akolouthia 1 mexri na emfanistei to 0
max0=0 #Megalyterh akolouthia 0
max1=0 #Megalyterh akolouthia 1


#ΜΕΤΑΤΡΟΠΗ ΣΕ STRING
e="".join(c)
y=len(e)


print("\n","\n","Apeikonish 'e' kathe dyadikhs timhs enwmenh:","\n","\n",e,"\n","\n")
print("Mhkos 'e'=",y)


for i in range (y):
    if e[i]=="0":
       akolouthia0=akolouthia0+1
       #print("twrinh akolouthia0 = ",akolouthia0)
    else:       
       if akolouthia0>max0:
          max0=akolouthia0
          #print("twrino max0 = ",max0)
       akolouthia0=0      


for i in range (y):
    if e[i]=="1":
       akolouthia1=akolouthia1+1
       #print("twrinh akolouthia1 = ",akolouthia1)
    else:       
       if akolouthia1>max1:
          max1=akolouthia1
          #print("twrino max1 = ",max1)
       akolouthia1=0      


print("Megalyterh akolouthia 0 =",max0)
print("Megalyterh akolouthia 1 =",max1)