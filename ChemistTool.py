# program to display periodic table and more
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
desk = Tk()
desk.title("Welcome to Chemist's Tools")
desk.geometry('350x300')
desk.wm_iconbitmap('logos\\cal3.ico')
lb = Label(desk, text="Chemist's\nTools", font=('Britannic Bold', 30))
lb.grid(column=0, row=0)
selected = IntVar()
rad1 = ttk.Radiobutton(desk, text='Periodic Table', value=1, variable=selected)
rad2 = ttk.Radiobutton(desk, text='Chemistry\nCalculator', value=2, variable=selected)
rad1.grid(column=0, row=1)
rad2.grid(column=0, row=2)


def to_know(event=None):
    if selected.get() == 1:
        window = Tk()        
        window.title('Periodic Table')
        window.geometry('1350x750')
        window.wm_iconbitmap('logos\\logo1.ico')
        lbl = Label(window, text="Click on\n Element \n to know \ninfo about it", font=('Britannic Bold', 10))
        lbl.grid(column=0, row=0)
        l1 = Label(window, text='Gas\nElements', font=('Britannic Bold', 10))
        l1.grid(column=1, row=0)
        l2 = Label(window, text='Liquid\nElements', fg='green', font=('Britannic Bold', 10))
        l2.grid(column=2, row=0)

        # First Group
        def click():
            messagebox.showinfo('Element Information','H\nHydrogen\nAtomic No. is 1\nMass No. is 1.0074')
        btn1=Button(window,text='H\nHydrogen',bg='light green',fg='black',width=10,height=5,font=('Britannic Bold',10),command=click)
        btn1.grid(column=0,row=1)
        def click1():
            messagebox.showinfo('Element Information','Li\nLithum\nAtomic No. is 3\nMass No. is 6.941')
        btn1=Button(window,text='Li\nLithum',bg='light blue',fg='blue',width=10,height=5,command=click1)
        btn1.grid(column=0,row=2)
        def click2():
            messagebox.showinfo('Element Information','Na\nSodium\nAtomic No. is 11\nMass No. is 22.9')
        btn1=Button(window,text='Na\nSodium',bg='light blue',fg='blue',width=10,height=5,command=click2)
        btn1.grid(column=0,row=3)
        def click3():
            messagebox.showinfo('Element Information','K\nPotassium\nAtomic No. is 19\nMass No. is 39.09')
        btn1=Button(window,text='K\nPotassium',bg='light blue',fg='blue',width=10,height=5,command=click3)
        btn1.grid(column=0,row=4)
        def click7():
            messagebox.showinfo('Element Information','Rb\nRubidium\nAtomic No. is 37\nMass No. is 85.4678')
        btn1=Button(window,text='Rb\nRubidium',bg='light blue',fg='blue',width=10,height=5,command=click7)
        btn1.grid(column=0,row=5)
        def click9():
            messagebox.showinfo('Element Information','Cs\nCaesium\nAtomic No. is 55\nMass No. is 132.905')
        btn1=Button(window,text='Cs\nCaesium',bg='light blue',fg='blue',width=10,height=5,command=click9)
        btn1.grid(column=0,row=6)
        def click11():
            messagebox.showinfo('Element Information','Fr\nFrancium \nAtomic No. is 87\nMass No. is 223')
        btn1=Button(window,text='Fr\nFrancium',bg='light blue',fg='blue',width=10,height=5,command=click11)
        btn1.grid(column=0,row=7)

        #Second Group
        def click4():
            messagebox.showinfo('Element Information','Be\nBeryllium\nAtomic No. is 4\nMass No. is 9.012')
        btn1=Button(window,text='Be\nBeryllium',bg='light blue',fg='blue',width=10,height=5,command=click4)
        btn1.grid(column=1,row=2)
        def click5():
            messagebox.showinfo('Element Information','Mg\nMagnesium \nAtomic No. is 12\nMass No. is 24.3050')
        btn1=Button(window,text='Mg\nMagnesium',bg='light blue',fg='blue',width=10,height=5,command=click5)
        btn1.grid(column=1,row=3)
        def click6():
            messagebox.showinfo('Element Information','Ca\nCalcium \nAtomic No. is 20\nMass No. is 40.078')
        btn1=Button(window,text='Ca\nCalcium',bg='light blue',fg='blue',width=10,height=5,command=click6)
        btn1.grid(column=1,row=4)
        def click8():
            messagebox.showinfo('Element Information','Sr\nStrontium\nAtomic No. is 38\nMass No. is 87.62')
        btn1=Button(window,text='Sr\nStrontium',bg='light blue',fg='blue',width=10,height=5,command=click8)
        btn1.grid(column=1,row=5)
        def click10():
            messagebox.showinfo('Element Information','Ba\nBarium\nAtomic No. is 56\nMass No. is 137.327')
        btn1=Button(window,text='Ba\nBarium',bg='light blue',fg='blue',width=10,height=5,command=click10)
        btn1.grid(column=1,row=6)
        def click12():
            messagebox.showinfo('Element Information','Ra\nRadium \nAtomic No. is 88\nMass No. is 226')
        btn1=Button(window,text='Ra\nRadium',bg='light blue',fg='blue',width=10,height=5,command=click12)
        btn1.grid(column=1,row=7)

        #Third Group
        def click13():
            messagebox.showinfo('Element Information','Sc\nScandium\nAtomic No. is 21\nMass No. is 44.95')
        btn1=Button(window,text='Sc\nScandium',bg='pink',fg='red',width=10,height=5,command=click13)
        btn1.grid(column=2,row=4)
        def click14():
            messagebox.showinfo('Element Information','Y\nYttrium\nAtomic No. is 39\nMass No. is 88.9')
        btn1=Button(window,text='Y\nYttrium',bg='pink',fg='red',width=10,height=5,command=click14)
        btn1.grid(column=2,row=5)

        #Fourth Group
        def click15():
            messagebox.showinfo('Element Information','Ti\nTitanium \nAtomic No. is 22\nMass No. is 47.86')
        btn1=Button(window,text='Ti\nTitanium',bg='pink',fg='red',width=10,height=5,command=click15)
        btn1.grid(column=3,row=4)
        def click16():
            messagebox.showinfo('Element Information','Zr\nZirconium \nAtomic No. is 40\nMass No. is 91.22')
        btn1=Button(window,text='Zr\nZirconium',bg='pink',fg='red',width=10,height=5,command=click16)
        btn1.grid(column=3,row=5)
        def click17():
            messagebox.showinfo('Element Information','Hf\nHafnium\nAtomic No. is 72\nMass No. is 178.49')
        btn1=Button(window,text='Hf\nHafnium',bg='pink',fg='red',width=10,height=5,command=click17)
        btn1.grid(column=3,row=6)
        def click18():
            messagebox.showinfo('Element Information','Rb\nRutherfordium\nAtomic No. is 104\nMass No. is 261')
        btn1=Button(window,text='Rb\nRutherfordium',bg='pink',fg='red',width=10,height=5,command=click18)
        btn1.grid(column=3,row=7)


        #Fifth Group
        def click19():
            messagebox.showinfo('Element Information','V\nVanadium\nAtomic No. is 23\nMass No. is 50.94')
        btn1=Button(window,text='V\nVanadium',bg='pink',fg='red',width=10,height=5,command=click19)
        btn1.grid(column=4,row=4)
        def click20():
            messagebox.showinfo('Element Information','Nb\nNiobium\nAtomic No. is 41\nMass No. is 92.9')
        btn1=Button(window,text='Nb\nNiobium',bg='pink',fg='red',width=10,height=5,command=click20)
        btn1.grid(column=4,row=5)
        def click21():
            messagebox.showinfo('Element Information','Ta\nTantalum \nAtomic No. is 73\nMass No. is 180.94')
        btn1=Button(window,text='Ta\nTantalum',bg='pink',fg='red',width=10,height=5,command=click21)
        btn1.grid(column=4,row=6)
        def click22():
            messagebox.showinfo('Element Information','Ra\nRadium \nAtomic No. is 105\nMass No. is 262')
        btn1=Button(window,text='Db\nDubnium',bg='pink',fg='red',width=10,height=5,command=click22)
        btn1.grid(column=4,row=7)


        #Sixth Group
        def click23():
            messagebox.showinfo('Element Information','Cr\nChromium\nAtomic No. is 24\nMass No. is 51.99')
        btn1=Button(window,text='Cr\nChromium',bg='pink',fg='red',width=10,height=5,command=click23)
        btn1.grid(column=5,row=4)
        def click24():
            messagebox.showinfo('Element Information','Mo\nMolybdenum\nAtomic No. is 42\nMass No. is 95.96')
        btn1=Button(window,text='Mo\nMolybdenum',bg='pink',fg='red',width=10,height=5,command=click24)
        btn1.grid(column=5,row=5)
        def click25():
            messagebox.showinfo('Element Information','W\nTungsten \nAtomic No. is 74\nMass No. is 183.84')
        btn1=Button(window,text='W\nTungsten',bg='pink',fg='red',width=10,height=5,command=click25)
        btn1.grid(column=5,row=6)
        def click26():
            messagebox.showinfo('Element Information','Sg\nSeaborgium \nAtomic No. is 106\nMass No. is 266')
        btn1=Button(window,text='Sg\nSeaborgium',bg='pink',fg='red',width=10,height=5,command=click26)
        btn1.grid(column=5,row=7)


        #Seventh Group
        def click27():
            messagebox.showinfo('Element Information','Mn\nManganese\nAtomic No. is 25\nMass No. is 54.93')
        btn1=Button(window,text='Mn\nManganese',bg='pink',fg='red',width=10,height=5,command=click27)
        btn1.grid(column=6,row=4)
        def click28():
            messagebox.showinfo('Element Information','Tc\nTechnetium\nAtomic No. is 43\nMass No. is 97.90')
        btn1=Button(window,text='Tc\nTechnetium',bg='pink',fg='red',width=10,height=5,command=click28)
        btn1.grid(column=6,row=5)
        def click29():
            messagebox.showinfo('Element Information','Re\nRhenium\nAtomic No. is 75\nMass No. is 186.207')
        btn1=Button(window,text='Re\nRhenium',bg='pink',fg='red',width=10,height=5,command=click29)
        btn1.grid(column=6,row=6)
        def click30():
            messagebox.showinfo('Element Information','Bh\nBohrium \nAtomic No. is 107\nMass No. is 264')
        btn1=Button(window,text='Bh\nBohrium',bg='pink',fg='red',width=10,height=5,command=click30)
        btn1.grid(column=6,row=7)
  


        #Eigth Group
        def click31():
            messagebox.showinfo('Element Information','Fe\nIron\nAtomic No. is 26\nMass No. is 55.8')
        btn1=Button(window,text='Fe\nIron',bg='pink',fg='red',width=10,height=5,command=click31)
        btn1.grid(column=7,row=4)
        def click32():
            messagebox.showinfo('Element Information','Ru\nRuthenium\nAtomic No. is 44\nMass No. is 101.70')
        btn1=Button(window,text='Ru\nRuthenium',bg='pink',fg='red',width=10,height=5,command=click32)
        btn1.grid(column=7,row=5)
        def click33():
            messagebox.showinfo('Element Information','Os\nOsmium\nAtomic No. is 76\nMass No. is 190.23')
        btn1=Button(window,text='Os\nOsmium',bg='pink',fg='red',width=10,height=5,command=click33)
        btn1.grid(column=7,row=6)
        def click34():
            messagebox.showinfo('Element Information','Hs\nHassium \nAtomic No. is 108\nMass No. is 277')
        btn1=Button(window,text='Hs\nHassium',bg='pink',fg='red',width=10,height=5,command=click34)
        btn1.grid(column=7,row=7)
  

        #Ninth Group
        def click35():
            messagebox.showinfo('Element Information','Co\nCobalt\nAtomic No. is 27\nMass No. is 58.93')
        btn1=Button(window,text='Co\nCobalt',bg='pink',fg='red',width=10,height=5,command=click35)
        btn1.grid(column=8,row=4)
        def click36():
            messagebox.showinfo('Element Information','Ruh\nRhodium\nAtomic No. is 45\nMass No. is 102.90')
        btn1=Button(window,text='Rh\nRhodium',bg='pink',fg='red',width=10,height=5,command=click36)
        btn1.grid(column=8,row=5)
        def click37():
            messagebox.showinfo('Element Information','Ir\nIrdium\nAtomic No. is 77\nMass No. is 192.217')
        btn1=Button(window,text='Ir\nIrdium',bg='pink',fg='red',width=10,height=5,command=click37)
        btn1.grid(column=8,row=6)
        def click38():
            messagebox.showinfo('Element Information','Mt\nMeitnerium \nAtomic No. is 109\nMass No. is 268')
        btn1=Button(window,text='Mt\nMeitnerium',bg='pink',fg='red',width=10,height=5,command=click38)
        btn1.grid(column=8,row=7)
  

        #Tenth Group
        def click39():
            messagebox.showinfo('Element Information','Ni\nNickel\nAtomic No. is 28\nMass No. is 58.69')
        btn1=Button(window,text='Ni\nNickel',bg='pink',fg='red',width=10,height=5,command=click39)
        btn1.grid(column=9,row=4)
        def click40():
            messagebox.showinfo('Element Information','Pd\nPalladium\nAtomic No. is 46\nMass No. is 106.42')
        btn1=Button(window,text='Pd\nPalladium',bg='pink',fg='red',width=10,height=5,command=click40)
        btn1.grid(column=9,row=5)
        def click41():
            messagebox.showinfo('Element Information','Pt\nPlatinum\nAtomic No. is 78\nMass No. is 195.0.84')
        btn1=Button(window,text='Pt\nPlatinum',bg='pink',fg='red',width=10,height=5,command=click41)
        btn1.grid(column=9,row=6)
        def click42():
            messagebox.showinfo('Element Information','Ds\nDarmstadtium \nAtomic No. is 110\nMass No. is 271')
        btn1=Button(window,text='Ds\nDarmstadtium',bg='pink',fg='red',width=10,height=5,command=click42)
        btn1.grid(column=9,row=7)
  

        #Eleventh Group
        def click43():
            messagebox.showinfo('Element Information','Cu\nCopper\nAtomic No. is 29\nMass No. is 63.54')
        btn1=Button(window,text='Cu\nCopper',bg='pink',fg='red',width=10,height=5,command=click43)
        btn1.grid(column=9,row=4)
        def click44():
            messagebox.showinfo('Element Information','Ag\nSilver\nAtomic No. is 47\nMass No. is 107.86')
        btn1=Button(window,text='Ag\nSilver',bg='pink',fg='red',width=10,height=5,command=click44)
        btn1.grid(column=9,row=5)
        def click45():
            messagebox.showinfo('Element Information','Au\nGold\nAtomic No. is 79\nMass No. is 196.96')
        btn1=Button(window,text='Au\nGold',bg='pink',fg='red',width=10,height=5,command=click45)
        btn1.grid(column=9,row=6)
        def click46():
            messagebox.showinfo('Element Information','Rg\nRoentgenium \nAtomic No. is 111\nMass No. is 272')
        btn1=Button(window,text='Rg\nRoentgenium',bg='pink',fg='red',width=10,height=5,command=click46)
        btn1.grid(column=9,row=7)
 

        #Twelveth Group
        def click47():
            messagebox.showinfo('Element Information','Zn\nZinc\nAtomic No. is 30\nMass No. is 65.38')
        btn1=Button(window,text='Zn\nZinc',bg='pink',fg='red',width=10,height=5,command=click47)
        btn1.grid(column=10,row=4)
        def click48():
            messagebox.showinfo('Element Information','Cd\nCadmium\nAtomic No. is 48\nMass No. is 112.41')
        btn1=Button(window,text='Cd\nCadmium',bg='pink',fg='red',width=10,height=5,command=click48)
        btn1.grid(column=10,row=5)
        def click49():
            messagebox.showinfo('Element Information','Hg\nMercury\nAtomic No. is 80\nMass No. is 200.56')
        btn1=Button(window,text='Hg\nMercury',bg='pink',fg='green',width=10,height=5,font=('Britannic Bold',10),command=click49)
        btn1.grid(column=10,row=6)
        def click50():
            messagebox.showinfo('Element Information','Cn\nCopernicium \nAtomic No. is 112\nMass No. is 285')
        btn1=Button(window,text='Cn\nCopernicium',bg='pink',fg='red',width=10,height=5,command=click50)
        btn1.grid(column=10,row=7)
 

        #Thirteenth Group
        def click51():
            messagebox.showinfo('Element Information','B\nBoron\nAtomic No. is 5\nMass No. is 10.81')
        btn1=Button(window,text='B\nBoron',bg='yellow',fg='red',width=10,height=5,command=click51)
        btn1.grid(column=11,row=2)
        def click52():
            messagebox.showinfo('Element Information','Al\nAluminium\nAtomic No. is 13\nMass No. is 26.98')
        btn1=Button(window,text='Al\nAluminium',bg='yellow',fg='red',width=10,height=5,command=click52)
        btn1.grid(column=11,row=3)
        def click53():
            messagebox.showinfo('Element Information','Ga\nGallium\nAtomic No. is 31\nMass No. is 69.72')
        btn1=Button(window,text='Ga\nGallium',bg='yellow',fg='red',width=10,height=5,command=click53)
        btn1.grid(column=11,row=4)
        def click54():
            messagebox.showinfo('Element Information','In\nIndium \nAtomic No. is 49\nMass No. is 114.818')
        btn1=Button(window,text='In\nIndium',bg='yellow',fg='red',width=10,height=5,command=click54)
        btn1.grid(column=11,row=5)
        def click55():
             messagebox.showinfo('Element Information','Tl\nThallium\nAtomic No. is 81\nMass No. is 204.38')
        btn1=Button(window,text='Tl\nThallium',bg='yellow',fg='red',width=10,height=5,command=click55)
        btn1.grid(column=11,row=6)
        def click56():
            messagebox.showinfo('Element Information','Nh\nNihonium \nAtomic No. is 113\nMass No. is 284')
        btn1=Button(window,text='Nh\nNihonium',bg='yellow',fg='red',width=10,height=5,command=click56)
        btn1.grid(column=11,row=7)
 

        #Fourteenth Group
        def click57():
            messagebox.showinfo('Element Information','C\nCarbon\nAtomic No. is 6\nMass No. is 12.01')
        btn1=Button(window,text='C\nCarbon',bg='yellow',fg='red',width=10,height=5,command=click57)
        btn1.grid(column=12,row=2)
        def click58():
            messagebox.showinfo('Element Information','Si\nSilicon\nAtomic No. is 14\nMass No. is 28.08')
        btn1=Button(window,text='Si\nSilicon',bg='yellow',fg='red',width=10,height=5,command=click58)
        btn1.grid(column=12,row=3)
        def click59():
            messagebox.showinfo('Element Information','Ge\nGermanium\nAtomic No. is 32\nMass No. is 72.63')
        btn1=Button(window,text='Ge\nGermanium',bg='yellow',fg='red',width=10,height=5,command=click59)
        btn1.grid(column=12,row=4)
        def click60():
            messagebox.showinfo('Element Information','Sn\nTin \nAtomic No. is 50\nMass No. is 118.71')
        btn1=Button(window,text='Sn\nTin',bg='yellow',fg='red',width=10,height=5,command=click60)
        btn1.grid(column=12,row=5)
        def click61():
            messagebox.showinfo('Element Information','Pb\nLead\nAtomic No. is 82\nMass No. is 207.2')
        btn1=Button(window,text='Pb\nLead',bg='yellow',fg='red',width=10,height=5,command=click61)
        btn1.grid(column=12,row=6)
        def click62():
            messagebox.showinfo('Element Information','Fl\nFlerovium \nAtomic No. is 114\nMass No. is 289')
        btn1=Button(window,text='Fl\nFlerovium',bg='yellow',fg='red',width=10,height=5,command=click62)
        btn1.grid(column=12,row=7)
 

        #Fifteenth Group
        def click63():
            messagebox.showinfo('Element Information','N\nNitrogen\nAtomic No. is 7\nMass No. is 14.0')
        btn1=Button(window,text='N\nNitrogen',bg='yellow',fg='black',width=10,height=5,font=('Britannic Bold',10),command=click63)
        btn1.grid(column=13,row=2)
        def click64():
            messagebox.showinfo('Element Information','P\nPhosphorus\nAtomic No. is 15\nMass No. is 30.9')
        btn1=Button(window,text='P\nPhosphorus',bg='yellow',fg='red',width=10,height=5,command=click64)
        btn1.grid(column=13,row=3)
        def click65():
            messagebox.showinfo('Element Information','As\nArsenic\nAtomic No. is 33\nMass No. is 74.92')
        btn1=Button(window,text='As\nArsenic',bg='yellow',fg='red',width=10,height=5,command=click65)
        btn1.grid(column=13,row=4)
        def click66():
            messagebox.showinfo('Element Information','Sb\nAntimony\nAtomic No. is 51\nMass No. is 121.76')
        btn1=Button(window,text='Sb\nAntimony',bg='yellow',fg='red',width=10,height=5,command=click66)
        btn1.grid(column=13,row=5)
        def click67():
             messagebox.showinfo('Element Information','Bi\nBismuth\nAtomic No. is 83\nMass No. is 208.98')
        btn1=Button(window,text='Bi\nBismuth',bg='yellow',fg='red',width=10,height=5,command=click67)
        btn1.grid(column=13,row=6)
        def click68():
            messagebox.showinfo('Element Information','Mc\nMoscovium \nAtomic No. is 115\nMass No. is 288')
        btn1=Button(window,text='Mc\nMoscovium',bg='yellow',fg='red',width=10,height=5,command=click68)
        btn1.grid(column=13,row=7)


        #Sixteenth Group
        def click75():
            messagebox.showinfo('Element Information','O\nOxygen\nAtomic No. is 8\nMass No. is 15.99')
        btn1=Button(window,text='O\nOxygen',bg='yellow',fg='black',width=10,height=5,font=('Britannic Bold',10),command=click75)
        btn1.grid(column=15,row=2)
        def click76():
            messagebox.showinfo('Element Information','S\nSulfur\nAtomic No. is 16\nMass No. is 32.065')
        btn1=Button(window,text='S\nSulfur',bg='yellow',fg='red',width=10,height=5,command=click76)
        btn1.grid(column=15,row=3)
        def click77():
            messagebox.showinfo('Element Information','Se\nSelenium\nAtomic No. is 34\nMass No. is 78.96')
        btn1=Button(window,text='Se\nSelenium',bg='yellow',fg='red',width=10,height=5,command=click77)
        btn1.grid(column=15,row=4)
        def click78():
           messagebox.showinfo('Element Information','Te\nTellurium\nAtomic No. is 52\nMass No. is 127.60')
        btn1=Button(window,text='Te\nTellurium',bg='yellow',fg='red',width=10,height=5,command=click78)
        btn1.grid(column=15,row=5)
        def click79():
            messagebox.showinfo('Element Information','Po\nPolonium\nAtomic No. is 84\nMass No. is 208.9824')
        btn1=Button(window,text='Po\nPolonium',bg='yellow',fg='red',width=10,height=5,command=click79)
        btn1.grid(column=15,row=6)
        def click80():
            messagebox.showinfo('Element Information','Lv\nLivermorium \nAtomic No. is 116\nMass No. is 292')
        btn1=Button(window,text='Lv\nLivermorium',bg='yellow',fg='red',width=10,height=5,command=click80)
        btn1.grid(column=15,row=7)
 

        #17 grp
        def click81():
            messagebox.showinfo('Element Information','F\nFluorine\nAtomic No. is 9\nMass No. is 18.99')
        btn1=Button(window,text='F\nFluorine',bg='yellow',fg='black',width=10,height=5,font=('Britannic Bold',10),command=click81)
        btn1.grid(column=16,row=2)
        def click82():
            messagebox.showinfo('Element Information','Cl\nChlorine\nAtomic No. is 17\nMass No. is 35.45')
        btn1=Button(window,text='Cl\nChlorine',bg='yellow',fg='black',width=10,height=5,font=('Britannic Bold',10),command=click82)
        btn1.grid(column=16,row=3)
        def click83():
            messagebox.showinfo('Element Information','Br\nBromine\nAtomic No. is 35\nMass No. is 79.90')
        btn1=Button(window,text='Br\nBromine',bg='yellow',fg='green',width=10,height=5,font=('Britannic Bold',10),command=click83)
        btn1.grid(column=16,row=4)
        def click84():
            messagebox.showinfo('Element Information','I\nIodine\nAtomic No. is 53\nMass No. is 126.90')
        btn1=Button(window,text='I\nIodine',bg='yellow',fg='red',width=10,height=5,command=click84)
        btn1.grid(column=16,row=5)
        def click85():
            messagebox.showinfo('Element Information','At\nAstatine\nAtomic No. is 85\nMass No. is 209.9871')
        btn1=Button(window,text='At\nAstatine',bg='yellow',fg='red',width=10,height=5,command=click85)
        btn1.grid(column=16,row=6)
        def click86():
            messagebox.showinfo('Element Information','Ts\nTennessine \nAtomic No. is 117\nMass No. is not known at present')
        btn1=Button(window,text='Ts\nTennessine',bg='yellow',fg='red',width=10,height=5,command=click86)
        btn1.grid(column=16,row=7)
  

        #18 grp
        def click87():
            messagebox.showinfo('Element Information','He\nHelium\nAtomic No. is 2\nMass No. is 4.00')
        btn1=Button(window,text='He\nHelium',bg='yellow',fg='black',width=10,height=5,font=('Britannic Bold',10),command=click87)
        btn1.grid(column=17,row=1)
        def click88():
            messagebox.showinfo('Element Information','Ne\nNeon\nAtomic No. is 10\nMass No. is 20.17')
        btn1=Button(window,text='Ne\nNeon',bg='yellow',fg='black',width=10,height=5,font=('Britannic Bold',10),command=click88)
        btn1.grid(column=17,row=2)
        def click89():
            messagebox.showinfo('Element Information','Ar\nArgon\nAtomic No. is 18\nMass No. is 39.94')
        btn1=Button(window,text='Ar\nArgon',bg='yellow',fg='black',width=10,height=5,font=('Britannic Bold',10),command=click89)
        btn1.grid(column=17,row=3)
        def click90():
            messagebox.showinfo('Element Information','Kr\nKrypton\nAtomic No. is 36\nMass No. is 83.79')
        btn1=Button(window,text='Kr\nKrypton',bg='yellow',fg='black',width=10,height=5,font=('Britannic Bold',10),command=click90)
        btn1.grid(column=17,row=4)
        def click91():
            messagebox.showinfo('Element Information','Xe\nXenon\nAtomic No. is 54\nMass No. is 131.29')
        btn1=Button(window,text='Xe\nXenon',bg='yellow',fg='black',width=10,height=5,font=('Britannic Bold',10),command=click91)
        btn1.grid(column=17,row=5)
        def click92():
            messagebox.showinfo('Element Information','Rn\nRadon \nAtomic No. is 86\nMass No. is 222.01')
        btn1=Button(window,text='Rn\nRadon',bg='yellow',fg='black',width=10,height=5,font=('Britannic Bold',10),command=click92)
        btn1.grid(column=17,row=6)
        def click93():
            messagebox.showinfo('Element Information','Og\nOganesson \nAtomic No. is 118\nMass No. is 294')
        btn1=Button(window,text='Og\nOganesson',bg='yellow',fg='red',width=10,height=5,command=click93)
        btn1.grid(column=17,row=7)
 
        #f block
        def fblock():
            lan=Tk()
            lan.title('F-Block Elements')
            lan.geometry('1350x350')
            lan.wm_iconbitmap('logos\\logo1.ico')
            ld=Label(lan,text='F-Block\nElements',font=('Franklin Gothic Demi',15))
            ld.grid(column=0,row=0)
            # lanthenoid 
            def click1():
                 messagebox.showinfo('Element Information','La\nLanthanum\nAtomic No. is 57\nMass No. is 138.90')
            btn1=Button(lan,text='La\nLanthanum',bg='light green',fg='blue',width=11,height=5,command=click1)
            btn1.grid(column=0,row=1)
            def click2():
                messagebox.showinfo('Element Information','Ce\nCerium\nAtomic No. is 58\nMass No. is 140.15')
            btn1=Button(lan,text='Ce\nCerium',bg='light green',fg='blue',width=11,height=5,command=click2)
            btn1.grid(column=1,row=1)
            def click3():
                messagebox.showinfo('Element Information','Pr\nPraseodymium\nAtomic No. is 59\nMass No. is 140.90')
            btn1=Button(lan,text='Pr\nPraseodymium',bg='light green',fg='blue',width=11,height=5,command=click3)
            btn1.grid(column=2,row=1)
            def click4():
                messagebox.showinfo('Element Information','Nd\nNeodymium\nAtomic No. is 60\nMass No. is 83.79')
            btn1=Button(lan,text='Nd\nNeodymium',bg='light green',fg='blue',width=11,height=5,command=click4)
            btn1.grid(column=3,row=1)
            def click5():
                messagebox.showinfo('Element Information','Pm\nPromethium\nAtomic No. is 61\nMass No. is 145')
            btn1=Button(lan,text='Pm\nPromethium',bg='light green',fg='blue',width=11,height=5,command=click5)
            btn1.grid(column=4,row=1)
            def click6():
                messagebox.showinfo('Element Information','Sm\nSamarium \nAtomic No. is 62\nMass No. is 150.36')
            btn1=Button(lan,text='Sm\nSamarium',bg='light green',fg='blue',width=11,height=5,command=click6)
            btn1.grid(column=5,row=1)
            def click7():
                messagebox.showinfo('Element Information','Eu\nEuropium \nAtomic No. is 63\nMass No. is 151.96')
            btn1=Button(lan,text='Eu\nEuropium',bg='light green',fg='blue',width=11,height=5,command=click7)
            btn1.grid(column=6,row=1)
            def click8():
                 messagebox.showinfo('Element Information','Gd\nGadolinium\nAtomic No. is 64\nMass No. is 157.25')
            btn1=Button(lan,text='Gd\nGadolinium',bg='light green',fg='blue',width=11,height=5,command=click8)
            btn1.grid(column=7,row=1)
            def click9():
                messagebox.showinfo('Element Information','Tb\nTerbium\nAtomic No. is 65\nMass No. is 158.92')
            btn1=Button(lan,text='Tb\nTerbium',bg='light green',fg='blue',width=11,height=5,command=click9)
            btn1.grid(column=8,row=1)
            def click10():
                messagebox.showinfo('Element Information','Dy\nDysprosium\nAtomic No. is 66\nMass No. is 162.5')
            btn1=Button(lan,text='Dy\nDysprosium',bg='light green',fg='blue',width=11,height=5,command=click10)
            btn1.grid(column=9,row=1)
            def click11():
                messagebox.showinfo('Element Information','Ho\nHolmium\nAtomic No. is 67\nMass No. is 164.93')
            btn1=Button(lan,text='Ho\nHolmium',bg='light green',fg='blue',width=11,height=5,command=click11)
            btn1.grid(column=10,row=1)
            def click12():
                messagebox.showinfo('Element Information','Er\nErbium\nAtomic No. is 68\nMass No. is 167.25')
            btn1=Button(lan,text='Er\nErbium',bg='light green',fg='blue',width=11,height=5,command=click12)
            btn1.grid(column=11,row=1)
            def click13():
                messagebox.showinfo('Element Information','Tm\nThulium \nAtomic No. is 69\nMass No. is 168.93')
            btn1=Button(lan,text='Tm\nThulium',bg='light green',fg='blue',width=11,height=5,command=click13)
            btn1.grid(column=12,row=1)
            def click14():
                messagebox.showinfo('Element Information','Yb\nYtterbium \nAtomic No. is 70\nMass No. is 173.05')
            btn1=Button(lan,text='Yb\nYtterbium',bg='light green',fg='blue',width=11,height=5,command=click14)
            btn1.grid(column=13,row=1)
            def click15():
                messagebox.showinfo('Element Information','Lu\nLutetium \nAtomic No. is 71\nMass No. is 174.96')
            btn1=Button(lan,text='Lu\nLutetium',bg='light green',fg='blue',width=11,height=5,command=click15)
            btn1.grid(column=14,row=1)
            #actinoid
            def clicks1():
                messagebox.showinfo('Element Information','Ac\nActinium\nAtomic No. is 89\nMass No. is 227')
            btn1=Button(lan,text='Ac\nActinium',bg='light green',fg='blue',width=11,height=5,command=clicks1)
            btn1.grid(column=0,row=2)
            def clicks2():
                messagebox.showinfo('Element Information','Th\nThorium\nAtomic No. is 90\nMass No. is 232.03')
            btn1=Button(lan,text='Th\nThorium',bg='light green',fg='blue',width=11,height=5,command=clicks2)
            btn1.grid(column=1,row=2)
            def clicks3():
                messagebox.showinfo('Element Information','Pr\nProtactinium\nAtomic No. is 91\nMass No. is 231.03')
            btn1=Button(lan,text='Pr\nPraseodymium',bg='light green',fg='blue',width=11,height=5,command=clicks3)
            btn1.grid(column=2,row=2)
            def clicks4():
                 messagebox.showinfo('Element Information','U\nUranium\nAtomic No. is 92\nMass No. is 238.02')
            btn1=Button(lan,text='U\nUranium',bg='light green',fg='blue',width=11,height=5,command=clicks4)
            btn1.grid(column=3,row=2)
            def clicks5():
                messagebox.showinfo('Element Information','Np\nNeptunium\nAtomic No. is 93\nMass No. is 237')
            btn1=Button(lan,text='Np\nNeptunium',bg='light green',fg='blue',width=11,height=5,command=clicks5)
            btn1.grid(column=4,row=2)
            def clicks6():
               messagebox.showinfo('Element Information','Pu\nPlutonium\nAtomic No. is 94\nMass No. is 244')
            btn1=Button(lan,text='Pu\nPlutonium',bg='light green',fg='blue',width=11,height=5,command=clicks6)
            btn1.grid(column=5,row=2)
            def clicks7():
                messagebox.showinfo('Element Information','Am\nAmericium \nAtomic No. is 95\nMass No. is 243')
            btn1=Button(lan,text='Am\nAmericium',bg='light green',fg='blue',width=11,height=5,command=clicks7)
            btn1.grid(column=6,row=2)
            def clicks8():
                messagebox.showinfo('Element Information','Cm\nCurium\nAtomic No. is 96\nMass No. is 247')
            btn1=Button(lan,text='Cm\nCurium',bg='light green',fg='blue',width=11,height=5,command=clicks8)
            btn1.grid(column=7,row=2)
            def clicks9():
                messagebox.showinfo('Element Information','Bk\nBerkelium\nAtomic No. is 97\nMass No. is 247')
            btn1=Button(lan,text='Bk\nBerkelium',bg='light green',fg='blue',width=11,height=5,command=clicks9)
            btn1.grid(column=8,row=2)
            def clicks10():
                messagebox.showinfo('Element Information','Cf\nCalifornium\nAtomic No. is 98\nMass No. is 251')
            btn1=Button(lan,text='Cf\nCalifornium',bg='light green',fg='blue',width=11,height=5,command=clicks10)
            btn1.grid(column=9,row=2)
            def clicks11():
                messagebox.showinfo('Element Information','Es\nEinsteinium\nAtomic No. is 99\nMass No. is 252')
            btn1=Button(lan,text='Es\nEinsteinium',bg='light green',fg='blue',width=11,height=5,command=clicks11)
            btn1.grid(column=10,row=2)
            def clicks12():
                messagebox.showinfo('Element Information','Fm\nFermium\nAtomic No. is 100\nMass No. is 257')
            btn1=Button(lan,text='Fm\nFermium',bg='light green',fg='blue',width=11,height=5,command=clicks12)
            btn1.grid(column=11,row=2)
            def clicks13():
                 messagebox.showinfo('Element Information','Md\nMendelevium \nAtomic No. is 101\nMass No. is 258')
            btn1=Button(lan,text='Md\nMendelevium',bg='light green',fg='blue',width=11,height=5,command=clicks13)
            btn1.grid(column=12,row=2)
            def clicks14():
                messagebox.showinfo('Element Information','No\nNobelium \nAtomic No. is 102\nMass No. is 259')
            btn1=Button(lan,text='No\nNobelium',bg='light green',fg='blue',width=11,height=5,command=clicks14)
            btn1.grid(column=13,row=2)
            def clicks15():
                 messagebox.showinfo('Element Information','Lr\nLawrencium \nAtomic No. is 103\nMass No. is 262')
            btn1=Button(lan,text='Lr\nLawrencium',bg='light green',fg='blue',width=11,height=5,command=clicks15)
            btn1.grid(column=14,row=2)
    
            #quit lan
            kquit = Button(lan,relief='groove', text="QUIT", fg="red",command=lan.destroy)
            kquit.grid(column=14,row=3,sticky=W)
  
            lan.mainloop()
    
        fbt=Button(window,text='Lanthanoids\n57-71',bg='blue',fg='yellow',width=10,height=5,command=fblock)
        fbt.grid(column=2,row=6)
        fbt1=Button(window,text='Actinoids\n89-103',bg='blue',fg='yellow',width=10,height=5,command=fblock)
        fbt1.grid(column=2,row=7)
         
        #quit
        kquit = Button(window,relief='groove', text="QUIT", fg="red",command=window.destroy)
        kquit.grid(column=17,row=8)
 
        window.mainloop()
    elif selected.get()==2:
        win=Tk()
        win.title("Chemistry Calculator")
        win.geometry('300x220')
        win.wm_iconbitmap('logos\\chem.ico')
        tab_control = ttk.Notebook(win)
        tab1 = ttk.Frame(tab_control)
        tab2 = ttk.Frame(tab_control)
        tab_control.add(tab1, text='Moles')
        tab_control.add(tab2, text='Conc. Terms')
        tab_control.pack(expand=1, fill='both')
 

        # Tab 1 moles
        lb = Label(tab1, text="Moles Calculator",font=('Impact',20))   
        lb.grid(column=0, row=0)
        lb = Label(tab1, text="Enter given mass")
        lb.grid(column=0, row=1)
        lb1 = Label(tab1, text="Enter molar mass")
        lb1.grid(column=0, row=2)
        lb2 = Label(tab1, text="Enter entity")
        lb2.grid(column=0, row=3)
        t= Entry(tab1,width=10,bg='light blue')
        t1= Entry(tab1,width=10,bg='light green')
        t2= Entry(tab1,width=10,bg='pink')
        t2.grid(column=1,row=3)
        t.grid(column=1,row=1)
        t1.grid(column=1,row=2)
        def mol1(event=None):
            x=float(t.get())/float(t1.get())
            f='No. of moles of '+t2.get()+' is '+str(x)
            v=Label(tab1,text=f)
            v.grid(column=0,row=3)
        b = Button(tab1,text='Enter',bg='yellow',command=mol1)
        b.grid(column=0,row=4)

        #Tab 2 Conc terms
        lbl2 = Label(tab2, text= 'Concentration of Solution\nTerms Calculator',font=('Impact',20))
        lbl2.grid(column=0, row=0)
        def func(event=None):
            if cb.get()=='Mass%':
                mass= Tk()
                mass.title('Calculating Mass %')
                mass.geometry('300x250')
                lb=Label(mass,text='Mass Per cent\nCalculator',font=('Impact',20))
                lb.grid(column=0,row=0)
                lm=Label(mass,text='Enter mass of solute')
                lm.grid(column=0,row=1)
                lm=Label(mass,text='Enter mass of solution')
                lm.grid(column=0,row=2)
                t1= Entry(mass,width=10,bg='light green')
                t2= Entry(mass,width=10,bg='light blue')
                t2.grid(column=1,row=1)
                t1.grid(column=1,row=2)
                def mol(event=None):
                      x=(float(t1.get())/(float(t2.get())+float(t1.get())))*100
                      g=100-x
                      f='Mass per cent of solute is '+str(g)+' %'
                      v=Label(mass,text=f)
                      v.grid(column=0,row=3)
                b = Button(mass,text='Enter',bg='yellow',command=mol)
                b.grid(column=0,row=4)
                mass.bind('<Return>', mol)
                mass.mainloop()
            elif cb.get()=='Mole Fraction':
                mass2= Tk()
                mass2.title('Calculating Mole Fraction')
                mass2.geometry('300x250')
                lb=Label(mass2,text='Mole Fraction\nCalculator',font=('Impact',20))
                lb.grid(column=0,row=0)
                lm=Label(mass2,text='Enter moles of substance A')
                lm.grid(column=0,row=1)
                lm=Label(mass2,text='Enter moles of substance B')
                lm.grid(column=0,row=2)
                t1= Entry(mass2,width=10,bg='pink')
                t2= Entry(mass2,width=10,bg='light blue')
                t2.grid(column=1,row=1)
                t1.grid(column=1,row=2)
                def mol2(event=None):
                      x=float(t1.get())/(float(t1.get())+float(t2.get()))
                      f='Mole Fraction of substance A is '+str(x)
                      v=Label(mass2,text=f)
                      v.grid(column=0,row=3)
                b = Button(mass2,text='Enter',bg='yellow',command=mol2)
                b.grid(column=0,row=4)
                mass2.bind('<Return>', mol2)
                mass2.mainloop()
            elif cb.get()=='Molarity':
                mass3= Tk()
                mass3.title('Calculating Molarity')
                mass3.geometry('300x250')
                lb=Label(mass3,text='Molarity\nCalculator',font=('Impact',20))
                lb.grid(column=0,row=0)
                lm=Label(mass3,text='Enter moles of solute')
                lm.grid(column=0,row=1)
                lm=Label(mass3,text='Enter volume of solution in mL')
                lm.grid(column=0,row=2)
                t1= Entry(mass3,width=10,bg='pink')
                t2= Entry(mass3,width=10,bg='light green')
                t2.grid(column=1,row=1)
                t1.grid(column=1,row=2)
                def mol3(event=None):
                      x=float(t2.get())/(float(t1.get())/1000)
                      f='Molarity of solution is '+str(x)+' M'
                      v=Label(mass3,text=f)
                      v.grid(column=0,row=3)
                b = Button(mass3,text='Enter',bg='yellow',command=mol3)
                b.grid(column=0,row=4)
                mass3.bind('<Return>', mol3)
                mass3.mainloop()
            elif cb.get()=='Molality':
                mass4= Tk()
                mass4.title('Calculating Molality')
                mass4.geometry('300x250')
                lb=Label(mass4,text='Molality\nCalculator',font=('Impact',20))
                lb.grid(column=0,row=0)
                lm=Label(mass4,text='Enter moles of solute')
                lm.grid(column=0,row=1)
                lm=Label(mass4,text='Enter mass of solvent in g')
                lm.grid(column=0,row=2)
                t1= Entry(mass4,width=10,bg='pink')
                t2= Entry(mass4,width=10,bg='light blue')
                t2.grid(column=1,row=1)
                t1.grid(column=1,row=2)
                def mol4(event=None):
                      x=float(t2.get())/(float(t1.get())/1000)
                      f='Molality of solution is '+str(x)+' m'
                      v=Label(mass4,text=f)
                      v.grid(column=0,row=3)
                b = Button(mass4,text='Enter',bg='yellow',command=mol4)
                b.grid(column=0,row=4)
                mass4.bind('<Return>', mol4)
                mass4.mainloop()
                
            
            
        course=["Mass%","Mole Fraction","Molarity","Molality"]
        l1=Label(tab2,text="Choose which you want to Calculate")
        l1.grid(column=0, row=1)
        cb=ttk.Combobox(tab2,values=course,width=20)
        cb.grid(column=0, row=2)
        cb.current(0)
        b=Button(tab2,text="Enter",bg='green',fg='light green',command=func)
        b.grid(column=0, row=3)
        win.mainloop()
        
def about():
    ab  = Tk()
    ab.title('Chemistry Tools Information')
    ab.geometry('400x400')
    sub='This  is  a  software  that  has  been created using  Python\
         \nas  a  programming language.This is a small way to help\
         \n the scientific community.Through this one can enter the\
         \nexciting world of chemistry through the base of chemistry\
         \nusing periodic table and also calculate several \
         \nconcentration terms and most importantly moles.This is an\
         \neasy to use software developed especially so that even a\
         \nbeginner can use it smoothly.This would be a great help to\
         \nvarious chemistry labs in schools.This software has been\
         \ndesigned to cut short the hassles of memorizing periodic\
         \ntable and save you from several calculations.This has been\
         \ncreated in accordance to the latest IUPAC suggestions.'
    lq=Label(ab,text=sub,fg='navy',font=('Franklin Gothic Demi Cond',12))
    lq.grid(column=0,row=0)
    lq1=Label(ab,text='With regards,\nSohel Ahmed',fg='orange red',font=('Cooper Black',12))
    lq1.grid(column=0,row=1)
    lq2 = Label(ab, text='Created with 😃 & </> by 👨🏻‍💻', fg='deep pink', font=10)
    lq2.grid(column=0,row=2)
    ab.mainloop()
    
btn = Button(desk, text="Click Here",bg='light blue',fg='red',command=to_know)
btn.grid(column=0, row=3)
abt = Button(desk, text='About',bg='yellow green',fg='deep pink',command=about)
abt.grid(column=0, row=6)
quit1 = Button(desk, text="Exit",bg='orange',fg='red',command=desk.destroy)
quit1.grid(column=5, row=4)
desk.bind('<Return>', to_know)                              
desk.mainloop()


