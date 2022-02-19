#ΚΑΠΟΙΑ PRINT() ΣΕ ΟΛΕΣ ΤΙΣ ΕΡΓΑΣΙΕΣ ΤΑ ΕΧΩ ΒΑΛΕΙ ΣΕ ΣΧΟΛΙΟ ΓΙΑΤΙ ΜΠΟΡΕΙ ΝΑ ΜΗΝ ΕΙΝΑΙ
#ΤΟΣΟ ΑΠΑΡΑΙΤΗΤΑ ΓΙΑ ΝΑ ΤΑ ΕΜΦΑΝΙΣΩ ΚΑΙ ΔΕΝ ΗΘΕΛΑ ΝΑ ΥΠΑΡΧΟΥΝ ΠΟΛΛΑ ΣΤΗΝ ΟΘΟΝΗ ΚΑΙ ΚΟΥΡΑΖΟΥΝ
#ΟΠΟΤΕ ΑΝ ΘΕΛΕΤΕ ΜΠΟΡΕΙΤΕ ΝΑ ΤΑ ΕΚΤΕΛΕΣΕΤΕ ΑΝ ΤΟ ΚΡΙΝΕΤΕ ΑΝΑΓΚΑΙΟ


import re


file=open("keimeno1.txt", "r")


y=file.read()
print("\n","\n","Arxikh morfh keimenou:","\n","\n",y)


#ΚΡΑΤΑΜΕ ΜΟΝΟ ΓΡΑΜΜΑΤΑ ΚΑΙ ΚΕΝΟ (ΥΠΕΘΕΣΑ ΧΩΡΙΣ ΣΗΜΕΙΑ ΣΤΙΞΗΣ ΚΑΙ ΑΡΙΘΜΟΥΣ ΕΤΣΙ ΟΠΩΣ ΤΟ ΛΕΕΙ Η ΕΚΦΩΝΗΣΗ)
y="".join(y)
y=re.sub(r'[^A-Za-z ]+',"", y)
print("\n","\n","\n","\n","Morfh keimenou mono me grammata kai to keno:","\n","\n",y)


#ΛΙΣΤΑ ΜΕ ΛΕΞΕΙΣ ΚΑΙ ΤΟΝ ΧΑΡΑΚΤΗΡΑ ΚΕΝΟ
b=re.split(r'(\s+)', y)
m=len(b)


print("\n","\n","Arxikh lista 'b':","\n","\n",b,"\n","\n") 
print("Mhkos listas 'b' =",m,"\n","\n")


#ΛΙΣΤΑ ΜΕ ΤΟ ΜΗΚΟΣ ΚΑΘΕ ΛΕΞΗΣ
length=[]


for i in range(m):
    length.append(len(b[i]))


n=len(length)
print("Arxikh lista mhkous lexewn 'length':","\n","\n",length,"\n","\n",) 
print("Mhkos ths 'length':",n,"\n","\n",)       


#ΛΙΣΤΑ ΜΕ ΤΑ ΠΛΗΘΗ ΤΩΝ ΓΡΑΜΜΑΤΩΝ
#ΔΕΝ ΕΒΑΛΑ ΠΑΡΑΠΑΝΩ ΤΙΜΕΣ ΓΙΑΤΙ ΔΕΝ ΛΕΤΕ ΝΑ ΑΦΑΙΡΕΣΟΥΜΕ ΤΙΣ ΛΕΞΕΙΣ ΜΕ ΠΑΝΩ ΑΠΟ 20 ΓΡΑΜΜΑΤΑ
pl=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
z=len(pl)


#ΑΦΑΙΡΕΣΗ ΛΕΞΕΩΝ ΜΕ 20 ΓΡΑΜΜΑΤΑ ΑΠΟ ΤΗΝ ΛΙΣΤΑ 'b'
#ΚΑΙ ΑΥΞΗΣΗ ΤΟΥ ΠΛΗΘΟΥΣ ΤΩΝ ΛΕΞΕΩΝ ΜΕ ΤΑΔΕ ΓΡΑΜΜΑΤΑ
i=0
while i<n:
    k=length[i]
    if k==20:
       b.pop(i)
       #b.pop(i-1) ΑΦΑΙΡΕΣΗ ΚΑΙ ΤΟΥ ΚΕΝΟΥ ΓΙΑ ΝΑ ΜΗΝ ΥΠΑΡΧΟΥΝ 2 ΔΙΑΔΟΧΙΚΑ ΚΕΝΑ(ΔΕΝ ΗΞΕΡΑ ΑΝ ΕΙΝΑΙ ΠΕΡΙΤΤΟ)
       length.pop(i)
       #length.pop(i-1) ΑΦΑΙΡΕΣΗ ΚΕΝΟΥ ΚΑΙ ΑΠΟ ΤΗΝ ΛΙΣΤΑ 'length'
       pl[k]=pl[k]+1
    else:    
       if b[i]!=" ":
          pl[k]=pl[k]+1
       i=i+1     
    n=len(length)


#ΕΚΤΥΠΩΣΗ ΠΛΗΘΟΥΣ ΛΕΞΕΩΝ ΜΕ ΤΑΔΕ ΓΡΑΜΜΑΤΑ
#Ζ=ΜΗΚΟΣ ΛΙΣΤΑΣ ΠΛΗΘΟΥΣ
for i in range(z):
    if i==1:
       print("Plithos lexewn me 1 gramma =",pl[i])
    if i>1 and i<20:
       print("Plithos lexewn me",i,"grammata =",pl[i])
    if i==20:
       print("Plithos lexewn me 20 grammata pou afairethikan=",pl[i])


print("\n","\n","\n","\n")  
  
  
print("Nea lista 'b':","\n","\n",b,"\n") 
print("Neo mhkos listas 'b'=",len(b),"\n","\n") 
print("Nea lista 'length':","\n","\n",length,"\n") 
print("Neo mhkos listas 'length'=",len(length)) 


#print("\n","\n","\n","Keimeno sthn telikh toy morfh :","\n","\n","".join(b))