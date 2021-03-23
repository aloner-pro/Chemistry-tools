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
    for k in range(18):
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


for i in range(7):
    bu_check = Button(root, text=g1[i][0], height=5, width=10)
    bu_check.place(x=5, y=80 + i * 85)
    elements_display(g1[i][1], g1[i][2], g1[i][0], g1[i][3], bu_check)

exit_bu = Button(root, text='Exit', command=root.destroy, bg='red', fg='yellow')
exit_bu.place(x=1100, y=600)
ho.create_tool_tip(exit_bu, "Closes the window")
root.mainloop()
