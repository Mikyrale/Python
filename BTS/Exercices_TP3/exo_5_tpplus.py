medecin = ((1, 'Chambernux', 'Daniela'), (2, 'Colombux', 'Laetitia'))
patients = ((1, 'Cratux', 'Leo'), (2, 'Machintrux', 'Thierry'))
rendez_vous = ((1,1,'2016-10-02'), (2,1,'2016-10-12'), (2,2,'2016-10-15'))
dates = ('2016-10-01', '2016-10-02', '2016-10-03', '2016-10-04', '2016-10-05', '2016-10-06', '2016-10-07', '2016-10-08', '2016-10-09', '2016-10-10', '2016-10-11', '2016-10-12', '2016-10-13', '2016-10-14', '2016-10-15')

for medecins in medecin :
    print("\t"*2, medecins[1], medecins[2],end='')
print("\n","-"*140,sep='')

for date in dates: 
    print(date, end=("\t"*2))

    for nb_rdv in range (len(rendez_vous)):
        if date in rendez_vous[nb_rdv][2]:

            for nb_medecin in range(len(medecin)):
                if rendez_vous[nb_rdv][0]==medecin[nb_medecin][0]:
                    print("\t"*nb_medecin,patients[rendez_vous[nb_rdv][1]-1][2]," ",patients[rendez_vous[nb_rdv][1]-1][1],end="\t"*2,sep="")
                else:
                    print("RDV LIBRE",end="\t")
            print("\n")
            break

    if date not in rendez_vous[nb_rdv][2]:
            for i in range (len(medecin)):
                  print("RDV LIBRE",end="\t"*2)
            print("\n")


