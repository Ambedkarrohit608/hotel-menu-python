for i in range(0,5):
    print("*",end="     ")
print("\n||....WELCOME....|| ")

print("||1. Room services||")

print("||2. Food services|| ")
for i in range(0,5):
    print("*",end="     ")
x=int(input("\n enter your choice..."))
if x==1:
    print("Room services")
    print("1.Ac Rooms ")
    print("2. Non Ac Rooms")
    y=int(input("enter your choice"))
    if y==1:
        print("||Ac Rooms||")
        print("1.Single person.....Rs 1000")
        print("2.Double person.....Rs  1500")
        print("3. Family...........Rs  4000")
        print("4.Birthday party....Rs 1200")
        while(True):
            x=int(input("enter your choice...."))
            if x==1:
                print("FOR SINGLE PERSON..........")
                qt=int(input("enter your qt for room......."))
                rt=qt*1000
                print("TOTAL BALANCE IS...Rs",rt)
            elif x==2:
                print(" FOR DOUBLE PERSON....")
                qt=int(input("enter your qt for room...."))
                rt=qt*1500
                print("TOTAL BALANCE IS..Rs",rt)
            elif x==3:
                print(" FOR FAMILY....")        
                qt=int(input("enter your qt for room....."))
                rt=qt*4000
                print("TOTAL BALANCE IS....Rs",rt)
            elif x==4:
                print("FOR BIRTHDAY PARTY..... ") 
                qt=int(input("enter your qt for room ......."))
                rt=qt*1200
                print("TOTAL BAlANCE IS......Rs",rt)  
            else:
                print("your choice is wrong please enter right choice.........")     
    elif y==2:
        print("Rooms for Non Ac...")
        print("1.SINGLE PERSON.....Rs.800")
        print("2.DOUBLE PERSON......Rs 1000")
        print("3.FAMILY.............Rs 1500") 
        print("4.BIRTHDAY PARTY......Rs 1000")
        while (True):
            x=int(input("enter your choice...."))
            if x==1:
                print("SINGLE PERSON ")
                qt=int(input("enter your qt for room...... "))
                rt=qt*800
                print("TOTAL BALANCE IS......Rs",rt)
            elif x==2:
                print("DOUBLE PERSON....")
                qt=int(input("enter your qt for room.."))
                rt=qt*1000
                print(" TOTAL BALANCE IS ..Rs",rt)
            elif x==3:
                print("FAMILY....")
                qt=int(input("enter your qt for room...."))
                rt=qt*1500
                print("TOTAL BALANCE IS...Rs",rt)
            elif x==4:
                print("BIRTHDAY PARTY ...")
                qt=int(input("enter your qt for room.."))
                rt=qt*1000
                print("TOTAL BALANCE IS.Rs",rt)
            else:
                print("your choice is wrong pleace enter right choice.......")    
elif x==2:
    print("FOOD SERVICE")
    print("1.BREAKFAST...")
    print("2.LUNCH.......") 
    print("3.DINNER......")
    while(True):
        y=int(input("enter your choice...."))
        if y==1:
            print("BREAKFAST......")
            print("1.TEA.......Rs 50")
            print("2.COFFEE....Rs 70") 
            print("3.DOSA......Rs 40") 
            print("4.MAGGI.....Rs 60") 
            x=int(input("enter your choice.."))
            if x==1:
                print("TEA")
                qt=int(input("enter your quantity for tea...."))
                rt=qt*50
                print("TOTAL BALANCE ONLY TEA...Rs",rt)
            elif x==2:
                print("COFFEE")
                qt=int(input("enter your quantity for coffee....."))
                rt=qt*70
                print("TOTAL BALANCE COFFEE ONLY..Rs",rt)
            elif x==3:
                print("DOSA....")
                qt=int(input("enter your quantity for dosa......"))
                rt=qt*40
                print("TOTAL BALANCE DOSA ONLY..Rs",rt)
            elif x==4:
                print("MAGGI")
                qt=int(input("enter your quantity for maggi......")) 
                rt=qt*60
                print("TOTAL BALANCE MAGGI ONLY...Rs",rt)
            else:
                print("your choice is wrong pleace enter right choice.......")    

        elif y==2:
            print("LUNCH")
            print("1.NAND ROTI  + MATER PANIR....Rs 120/plate")
            print("2. DAL CHAWAL ................Rs 50/plate") 
            print("3.CHOLE BHATURE...............Rs 30/plate")
            print("4. VEG BIRYANI................Rs 50/plate")
            while(True):
                x=int(input("enter your choice....."))
                if x==1:
                    print("NAND ROTI + MATER PANIR")
                    qt=int(input("enter your quantity for nand roti+ mater panir........."))
                    rt=qt*120
                    print("TOTAL BALANCE NAND ROTI+ MATER PANIR ONLY...Rs",rt)
                elif x==2:
                    print("DAL CHAWAL")
                    qt=int(input("enter your quantity for dal chawal........"))
                    rt=qt*50
                    print("TOTAL BALANCE DAL CHAWAL ONLY ..Rs",rt)
                elif x==3:
                    print("CHOLE BHATURE") 
                    qt=int(input("enter your quantity for chole bhature......"))
                    rt=qt*30
                    print("TOTAL BALANCE CHOLE BHATURE ONLY...Rs",rt)
                elif x==4:
                    print("VEG BIRYANI") 
                    qt=int(input("enter your quantity for veg biryani......."))
                    rt=qt*50
                    print("TOTAL BALANCE VEG BIRYANI ONLY....Rs",rt)  
                else:
                    print("your choice is wrong pleace enter right choice.................")        
        elif y==3:
            print("DINNER......")
            print("1.AALU PANATHE................Rs 50/plate")
            print("2.AALU GOBHI + SADA ROTI .....Rs 70/plate")
            print("3.MATER PANEER + NAND ROTI....Rs 140/plate")
            print("4.CHOLE + NAND ROTI...........Rs  90/plate")
            while(True):
                x=int(input("enter your choice......"))
                if x==1:
                    print("|| AALU PANATHE.......||")
                    qt=int(input("enter your quantity for aalu panathe........")) 
                
                    rt=qt*50
                    print("TOTAL BALANCE...Rs",rt)
                elif x==2:
                    print("|| AALU GOBHI+ SADA ROTI||")
                    qt=int(input("enter your quantity for aalu gobhi + sada roti........"))
                    rt=qt*70
                    print("TOTAL BALNCE....Rs",rt)
                elif x==3:
                    print("|| MATER PANEER +NAND ROTI||")
                    qt=int(input("enter your quantity for mater paneer + nand roti...."))
                    rt=qt*140
                    print("TOTAL BALANCE.....Rs",rt)
                elif x==4:
                    print("|| CHOLE +NAND ROTI ||")
                    qt=int(input("enter your quantity for chole +nand roti......."))
                    rt=qt*90
                    print("TOTAL BALANCE.....Rs",rt)
                else:
                    print("your choice is wrong pleace enter right choice.............. ")               

                          
 
    
        

