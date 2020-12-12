import tkinter
from tkinter import *
from tkinter import messagebox

val = ""
A = 0
operator = ""

def main():

    

    # ======================Functions======================#
    # Clear button
    def btn_clear_clicked():
        global A, operator, val
        val, operator = "", ""
        A = 0
        data.set(val)

    # buttons
    def btn_0_isClicked():
        global val
        val += "0"
        data.set(val)

    def btn_1_isClicked():
        global val
        val += "1"
        data.set(val)

    def btn_2_isClicked():
        global val
        val += "2"
        data.set(val)

    def btn_3_isClicked():
        global val
        val += "3"
        data.set(val)

    def btn_3_isClicked():
        global val
        val += "3"
        data.set(val)

    def btn_4_isClicked():
        global val
        val += "4"
        data.set(val)

    def btn_5_isClicked():
        global val
        val += "5"
        data.set(val)

    def btn_6_isClicked():
        global val
        val += "6"
        data.set(val)

    def btn_7_isClicked():
        global val
        val += "7"
        data.set(val)

    def btn_8_isClicked():
        global val
        val += "8"
        data.set(val)

    def btn_9_isClicked():
        global val
        val += "9"
        data.set(val)

    # Operators
    def btn_plus_cicked():
        global val, A, operator
        A = int(val)
        operator = "+"
        val += "+"
        data.set(val)

    def btn_minus_cicked():
        global val, A, operator
        A = int(val)
        operator = "-"
        val += "-"
        data.set(val)

    def btn_multi_cicked():
        global val, A, operator
        A = int(val)
        operator = "*"
        val += "*"
        data.set(val)

    def btn_div_cicked():
        global val, A, operator
        A = int(val)
        operator = "/"
        val += "/"
        data.set(val)

    # Equal button clicked
    def equal():
        global val, A, operator
        val2 = val
        if operator == "+":
            x = int((val2.split("+")[1]))
            c = A + x
            data.set(c)
            val = str(c)
        elif operator == "-":
            x = int((val2.split("-")[1]))
            c = A - x
            data.set(c)
            val = str(c)
        elif operator == "*":
            x = int((val2.split("*")[1]))
            c = A * x
            data.set(c)
            val = str(c)
        elif operator == "/":
            x = int((val2.split("/")[1]))
            if x == 0:
                messagebox.showerror("Error", "Division by 0 not allow")
                A = ""
                val = ""
                data.set(val)
            else:
                c = int(A / x)
                data.set(c)
                val = str(c)

    # =======================Functions Ends=====================#

    root = tkinter.Tk()
    root.geometry("400x550+700+300")
    root.resizable(0, 0)
    root.title("Calculator")
    data = StringVar()

    # Screen
    screen = Label(
        root,
        anchor="se",
        font=("Verdana", 20),
        bg="#fff",
        fg="#000",
        textvariable=data,
    )
    screen.pack(expand=True, fill="both", )

    # Button row
    btnrow1 = Frame(root, bg="", )
    btnrow1.pack(expand=True, fill="both", )
    btnrow2 = Frame(root, bg="", )
    btnrow2.pack(expand=True, fill="both", )
    btnrow3 = Frame(root, bg="", )
    btnrow3.pack(expand=True, fill="both", )
    btnrow4 = Frame(root, bg="", )
    btnrow4.pack(expand=True, fill="both", )

    # buttons row 1
    btn7 = Button(btnrow1, text="7", font=("Verdana", 22), relief=GROOVE, border=0, command=btn_7_isClicked, )
    btn7.pack(side=LEFT, expand=True, fill="both")
    btn8 = Button(btnrow1, text="8", font=("Verdana", 22), relief=GROOVE, border=0, command=btn_8_isClicked, )
    btn8.pack(side=LEFT, expand=True, fill="both")
    btn9 = Button(btnrow1, text="9", font=("Verdana", 22), relief=GROOVE, border=0, command=btn_9_isClicked, )
    btn9.pack(side=LEFT, expand=True, fill="both")
    btnPlus = Button(btnrow1, text="+", font=("Verdana",), relief=GROOVE, border=0, command=btn_plus_cicked, )
    btnPlus.pack(side=LEFT, expand=True, fill="both")

    # buttons row 2
    btn4 = Button(btnrow2, text="4", font=("Verdana", 22), relief=GROOVE, border=0, command=btn_4_isClicked, )
    btn4.pack(side=LEFT, expand=True, fill="both")
    btn5 = Button(btnrow2, text="5", font=("Verdana", 22), relief=GROOVE, border=0, command=btn_5_isClicked, )
    btn5.pack(side=LEFT, expand=True, fill="both")
    btn6 = Button(btnrow2, text="6", font=("Verdana", 22), relief=GROOVE, border=0, command=btn_6_isClicked, )
    btn6.pack(side=LEFT, expand=True, fill="both")
    btnMinus = Button(btnrow2, text="-", font=("Verdana",), relief=GROOVE, border=0, command=btn_minus_cicked, )
    btnMinus.pack(side=LEFT, expand=True, fill="both")

    # buttons row 3
    btn1 = Button(btnrow3, text="1", font=("Verdana", 22), relief=GROOVE, border=0, command=btn_1_isClicked, )
    btn1.pack(side=LEFT, expand=True, fill="both")
    btn2 = Button(btnrow3, text="2", font=("Verdana", 22), relief=GROOVE, border=0, command=btn_2_isClicked, )
    btn2.pack(side=LEFT, expand=True, fill="both")
    btn3 = Button(btnrow3, text="3", font=("Verdana", 22), relief=GROOVE, border=0, command=btn_3_isClicked, )
    btn3.pack(side=LEFT, expand=True, fill="both")
    btnMulti = Button(btnrow3, text="*", font=("Verdana",), relief=GROOVE, border=0, command=btn_multi_cicked, )
    btnMulti.pack(side=LEFT, expand=True, fill="both")

    # buttons row 4
    btnClear = Button(btnrow4, text="C", font=("Verdana", 22), relief=GROOVE, border=0, command=btn_clear_clicked, )
    btnClear.pack(side=LEFT, expand=True, fill="both")
    btn0 = Button(btnrow4, text="0", font=("Verdana", 22), relief=GROOVE, border=0, command=btn_0_isClicked, )
    btn0.pack(side=LEFT, expand=True, fill="both")
    btnEqual = Button(btnrow4, text="=", font=("Verdana", 22), relief=GROOVE, border=0, command=equal, )
    btnEqual.pack(side=LEFT, expand=True, fill="both")
    btnDiv = Button(btnrow4, text="/", font=("Verdana",), relief=GROOVE, border=0, command=btn_div_cicked, )
    btnDiv.pack(side=LEFT, expand=True, fill="both")
    root.mainloop()


if __name__ == '__main__':
    main()
