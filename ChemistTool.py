# program to display periodic table and more
from tkinter import *
import package.hovering as ho

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


bu_check = Button(root, text='Check')
bu_check.pack()
elements_display('Hydrogen', 1, 'H', 1.007, bu_check)
root.mainloop()
