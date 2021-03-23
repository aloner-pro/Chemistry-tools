# Program to display periodic table and more
import csv
from tkinter import *
import package.hovering as ho

with open('queried.csv', 'r') as d:
    td = list(csv.reader(d))
    data = []
    for i in td[1:]:
        if i[-3] != '':
            data.append(i)
    g1 = []
    for k in range(19):
        for j in data:
            if int(j[-3]) == k:
                g1.append(j)

root = Tk()
root.title('Periodic Table')

# Centering the window
root_h, root_w = 680, 1200
s_w = root.winfo_screenwidth()
s_h = root.winfo_screenheight()
x_co = int((s_w / 2) - (root_w / 2))
y_co = int((s_h / 2) - (root_h / 2))
root.geometry("{}x{}+{}+{}".format(root_w, root_h, x_co, y_co))


def elements_display(ele_name: str, at_no: int, ele_sym: str, at_mass: float, button_obj):
    ho.create_tool_tip(button_obj, f'Element Symbol: {ele_sym}\nElement Name: {ele_name}\nAtomic Number: {at_no}'
                                   f'\nAtomic Mass: {at_mass}')


def ele_7(ele_list, x_):
    for a in range(7):
        du = ele_list[a]
        bu_check2 = Button(root, text=du[0], height=4, width=8)
        bu_check2.place(x=x_, y=55 + a * 70)
        elements_display(du[1], du[2], du[0], du[3], bu_check2)


def ele_6(ele_list, x_):
    for a in range(6):
        du = ele_list[a]
        bu_check2 = Button(root, text=du[0], height=4, width=8)
        bu_check2.place(x=x_, y=125 + a * 70)
        elements_display(du[1], du[2], du[0], du[3], bu_check2)


def ele_4(ele_list, x_):
    for a in range(4):
        du = ele_list[a]
        bu_check2 = Button(root, text=du[0], height=4, width=8)
        bu_check2.place(x=x_, y=265 + a * 70)
        elements_display(du[1], du[2], du[0], du[3], bu_check2)


ele_7(g1[:7], 4)
ele_6(g1[7:13], 70)

for y in range(10):
    ele_4(g1[13+(4*y):17+(4*y)], 136+(66*y))

for z in range(5):
    ele_6(g1[53+(6*z):59+(6*z)], 796+(66*z))

ele_7(g1[83:90], 1126)
exit_bu = Button(root, text='Exit', command=root.destroy, bg='red', fg='yellow')
exit_bu.place(x=1100, y=600)
ho.create_tool_tip(exit_bu, "Closes the window")
root.mainloop()
