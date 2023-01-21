import sys
try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk
try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

# import _support
def vp_start_gui():
    """Starting point when module is the main routine."""
    global val, w, root
    root = tk.Tk()
    top = Toplevel1(root)
    # _support.init(root, top)
    root.mainloop()


w = None


def create_Toplevel1(rt, *args, **kwargs):
    """Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' ."""
    global w, w_win, root
    # rt = root
    root = rt
    w = tk.Toplevel(root)
    top = Toplevel1(w)
    # _support.init(w, top, *args, **kwargs)
    return (w, top)


def destroy_Toplevel1():
    global w
    w.destroy()
    w = None


class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'
        font9 = "-family {Century Gothic} -size 14 -weight bold"
        btn_font = "-family {Century Gothic} -size 10 -weight bold"
        top.geometry("600x450+650+150")
        top.minsize(176, 1)
        top.maxsize(1924, 1050)
        top.resizable(0, 0)
        top.title("EyeNose Mouse FYP")
        top.configure(background="#d9d9d9")

        self.Label1 = tk.Label(top)
        # self.Label1.place(relx=0.2, rely=0.0, height=71, width=357)
        self.Label1.place(relx=0.2, rely=0.0, height=50, width=357)
        self.Label1.configure(background="#000040")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font9)
        self.Label1.configure(foreground="#ffffff")
        self.Label1.configure(text='''EyeNose Mouse Dashboard''')

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0, rely=0.83, height=80, width=600)
        self.Label2.configure(background="#000040")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font=font9)
        self.Label2.configure(foreground="#ffffff")
        self.Label2.configure(text='''By:\nKashif Ali\nMaryam Habib''')


        """NoseMouse button code"""
        self.Button1_2 = tk.Button(top)
        self.Button1_2.place(relx=0.325, rely=0.267, height=42, width=208)
        self.Button1_2.configure(font=btn_font)
        self.Button1_2.configure(activebackground="#ececec")
        self.Button1_2.configure(activeforeground="#000000")
        self.Button1_2.configure(background="#0979f7")
        self.Button1_2.configure(command=NoseMouse)
        self.Button1_2.configure(disabledforeground="#a3a3a3")
        self.Button1_2.configure(foreground="#ffffff")
        self.Button1_2.configure(highlightbackground="#d9d9d9")
        self.Button1_2.configure(highlightcolor="black")
        self.Button1_2.configure(pady="0")
        self.Button1_2.configure(text='''Nose Mouse''')


        """Keyboard button code"""
        self.Button1_4 = tk.Button(top)
        self.Button1_4.place(relx=0.325, rely=0.4, height=42, width=208)
        self.Button1_4.configure(font=btn_font)
        self.Button1_4.configure(activebackground="#ececec")
        self.Button1_4.configure(activeforeground="#000000")
        self.Button1_4.configure(background="#0979f7")
        self.Button1_4.configure(command=Keyboard)
        self.Button1_4.configure(disabledforeground="#a3a3a3")
        self.Button1_4.configure(foreground="#ffffff")
        self.Button1_4.configure(highlightbackground="#d9d9d9")
        self.Button1_4.configure(highlightcolor="black")
        self.Button1_4.configure(pady="0")
        self.Button1_4.configure(text='''Virtual Keyboard''')

        """Combine Keyboard button code"""
        # self.Button1_5 = tk.Button(top)
        # self.Button1_5.place(relx=0.120, rely=0.4, height=42, width=208)
        # self.Button1_5.configure(font=btn_font)
        # self.Button1_5.configure(activebackground="#ececec")
        # self.Button1_5.configure(activeforeground="#000000")
        # self.Button1_5.configure(background="#0979f7")
        # self.Button1_5.configure(command=combineKeyboard)
        # self.Button1_5.configure(disabledforeground="#a3a3a3")
        # self.Button1_5.configure(foreground="#ffffff")
        # self.Button1_5.configure(highlightbackground="#d9d9d9")
        # self.Button1_5.configure(highlightcolor="black")
        # self.Button1_5.configure(pady="0")
        # self.Button1_5.configure(text='''Combine Virtual Keyboard''')


        # """EyeMouse button code"""
        # self.Button1_3 = tk.Button(top)
        # self.Button1_3.place(relx=0.550, rely=0.4, height=42, width=208)
        # self.Button1_3.configure(font=btn_font)
        # self.Button1_3.configure(activebackground="#ececec")
        # self.Button1_3.configure(activeforeground="#000000")
        # self.Button1_3.configure(background="#0979f7")
        # self.Button1_3.configure(command=EyeMouse)
        # self.Button1_3.configure(disabledforeground="#a3a3a3")
        # self.Button1_3.configure(foreground="#ffffff")
        # self.Button1_3.configure(foreground="#ffffff")
        # self.Button1_3.configure(highlightbackground="#d9d9d9")
        # self.Button1_3.configure(highlightcolor="black")
        # self.Button1_3.configure(pady="0")
        # self.Button1_3.configure(text='''Eye Mouse''')


        """Exit button code"""
        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.325, rely=0.55, height=42, width=208)
        self.Button1.configure(font=btn_font)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#0979f7")
        self.Button1.configure(command=quit)
        self.Button1.configure(cursor="fleur")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#ffffff")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Exit''')


def EyeMouse():
    root.attributes('-alpha', 0)
    import EyeMouse
    root.attributes('-alpha', 255)

def NoseMouse():
    root.attributes('-alpha', 0)
    import NoseMouse
    root.attributes('-alpha', 255)


def Keyboard():
    root.attributes('-alpha', 0)
    import Keyboard_module
    root.attributes('-alpha', 255)

def combineKeyboard():
    root.attributes('-alpha', 0)
    import full_keyboard
    root.attributes('-alpha', 255)
def quiteApp():
    sys.exit(0)


if __name__ == '__main__':
    vp_start_gui()
