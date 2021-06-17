from tkinter import *
from elements import *
# this and purple rain and physics sims
round_num = 4
root = Tk()
root.title('Gases | Pressure | Volume')
root.geometry('700x500')
root['bg'] = 'white'

def find_moles_vol():
    vol, press, temp, pressV = volume.get(), pressure.get(), temperature.get(), pressure_v.get()
    print(vol, press, temp, pressV)
    mol = (float(press) * float(vol) ) / ((float(temp) + float(tempV.get())) * float(pressV))
    print(mol)
    labol['text'] = 'Moles : {:e}'.format(mol)
    return mol
def find_moles(mass, atomicM):
    moles = round(mass / atomicM, round_num)
    return moles

def find_volume(mol):
    press = float(pressure.get())
    temp = float(temperature.get())
    tempv = tempV.get()
    pressv = pressure_v.get()
    v = round((mol * pressv * (temp + tempv) ) / press, round_num)
    labol['text'] = 'Moles : {}\nVolume : {}L'.format(mol,v)
    return v

def submit():
    global atomic_list
    atomic_list = []
    user_compound = compound.get()
    user_compound = user_compound.strip() + ' '
    numbers = []
    number = ''
    letter = ''
    letters = []
    for x in user_compound:
        try:
            int(x)
            number += str(x)
            if letter != '':
                letters.append(letter)
            letter = ''
        except:
            letter += x
            if number != '':
                numbers.append(number)
            number = ''
    compound_dictionary = dict(zip(letters, numbers))
    for element in compound_dictionary:
        atomic_mass = elements[element] * int(compound_dictionary[element])
        atomic_list.append(atomic_mass)
    # print(find_volume(find_moles(float(mass.get()), sum(atomic_list))))
    submit2()
def submit2():
    vol = volume.get()
    comp = compound.get()
    mas = mass.get()
    temp = temperature.get()
    press = pressure.get()
    mol = mole.get()
    if vol.lower() == 'x' and comp != '' and mas != '' and temp != '' and press != '':
        print('s')
        find_volume(find_moles(float(mass.get()),sum(atomic_list)))
    elif mol.lower() == 'x' and vol != '' and press != '' and temp != '':
        find_moles_vol()
compoundL = Label(root, text='Compound')
compoundL.grid(row=1, column=1,pady=(15,5))

compound = Entry(root, width=20)
compound.grid(row=2, column=1, padx=20)

moleL = Label(root,text='Moles')
moleL.grid(row=3,column=1,pady=(15,5))

mole = Entry(root,width=20)
mole.grid(row=4,column=1)

volumeL = Label(root,text='Volume (L)')
volumeL.grid(row=5, column=1,pady=(15,5))

volume = Entry(root,width=20)
volume.grid(row=6, column=1)

massL = Label(root, text='Mass (g)')
massL.grid(row=7, column=1,pady=(15,5))

mass = Entry(root, width=20)
mass.grid(row=8, column=1, padx=20)

tempL = Label(root, text='Temperature')
tempL.grid(row=9, column=1,pady=(15,5))

temperature = Entry(root, width=20)
temperature.grid(row=10, column=1, padx=20)

tempV = DoubleVar()
tempV.set(0)

tempframe = Frame(root)
tempframe.grid(row=11,column=1,sticky='nsew',padx=30)

kelvin = Radiobutton(tempframe, variable=tempV, value=0, text='K')
kelvin.pack(fill="none", expand=True, side='left') # anchor='w'to align // side='left',anchor='w'

celsius = Radiobutton(tempframe, variable=tempV, value=273.15, text='C') # indicatoron=False for button
celsius.pack(fill="none", expand=True,side='left')

pressure = Entry(root, width=20)
pressure.grid(row=13, column=1, padx=20)

pressure_v = DoubleVar()
pressure_v.set(0.0821)

pressureframe = Frame(root)
pressureframe.grid(row=14,column=1)

pressure_atm = Radiobutton(pressureframe, variable=pressure_v, text='atm', value=0.0821)
pressure_atm.pack(fill="none", expand=True,side='left')

pressure_Kpascal = Radiobutton(pressureframe, variable=pressure_v, text='Kpa', value=8.314)
pressure_Kpascal.pack(fill="none", expand=True,side='left')

pressureL = Label(root, text='Pressure')
pressureL.grid(row=12, column=1,pady=(15,5)) # padx and pady use tuples for top/bottom and left/right


labol = Label(root,font='50')
labol.grid(row=7,column=2,columnspan=2)

submit_button = Button(root, padx=40, pady=20, command=submit,text='Submit')
submit_button.grid(row=15, column=2, columnspan=2)

root.mainloop()
