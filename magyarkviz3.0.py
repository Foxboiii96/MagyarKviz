print('Üdvözöllek a magyar kvízemben!')
# Ebből az inputból indulnak ki a válaszok
val = input('Készen állsz a játékra? (igen/nem)')
# Ebbe gyűjti a pontokat
pont = 0
# A kérdések száma
ossz_k = 6
        
if val.lower() == "igen":
    val = input("1. Ki volt Magyarország első királya?")
    if val.lower() == "i. istván" or "istván":
        pont += 1 
        print("Helyes!")
    else:
        print("A helyes válasz i. istván lett volna.")
        
    val = input("2. Ki volt I. Magyar Köztársasag első Miniszterelnöke?")
    if val.lower() == "antall józsef":
        pont += 1 
        print("Helyes!")
    else:
        print("A helyes válasz antall józsef lett volna.")
                
    val = input ("3. Ki volt a király nélküli Magyar Királyság kormányzója?")
    if val.lower() == "horthy miklós":
        pont += 1 
        print("Helyes!")
    else:
        print("A helyes válasz horthy miklós lett volna.")
            
    val = input ("4. Ki volt a legvidámabb barakk titkára?")
    if val.lower() == "kádár jános":
        pont += 1
        print ("Helyes!")
    else:
        print("A helyes válasz kádár jános lett volna.")
                
    val = input ("5. Ki volt Madagaszkár királya?")
    if val.lower() == "benyovszky móric" or "móric":
        pont += 1
        print("Helyes!")
    else:
        print("A helyes válasz benyovszky móric lett volna.")
                
    val = input ("6. Hány magyar önjelölt uralkodó volt 1400 előtt?")
    if val.lower() == 12:
        pont += 1
        print("Helyes!")
    else:
        print("A helyes válasz 12 lett volna.")
            
    szazalek = (pont/ossz_k) * 100
            
    print("Köszönöm hogy játszottál a játékommal! A helyes válaszaidnak a száma")
    print(str(pont) + " helyes válasz")
    print("És ennyi százalékot értél el")
    print(str(szazalek) + "%") 
        

print("Viszlát!")