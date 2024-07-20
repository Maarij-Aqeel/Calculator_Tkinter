import tkinter as tk
from PIL import Image,ImageTk



def Starter_Code():
    window = tk.Tk()
    window.configure(bg="#000000")
    window.geometry("750x820")
    window.resizable(False, False)
    window.title("Calculator")
    photo=Image.open("undo.png")
    resize=photo.resize((70,70))
    photo=ImageTk.PhotoImage(resize)

    widgets(window,photo)
    window.mainloop()

def calculate(no):
    try:
        return eval(no.replace('x', '*').replace('%', '//100'))
    except ZeroDivisionError:
        return "Error"
    except:
        return "Invalid Input"

def Calculations(label, no, Answer, operator):
    global prev, prev_ans

    if operator == "AC":
        prev = ""
        prev_ans = 0
    elif operator == "undo":
        prev = prev[:-1]
    else:
        if operator in ['+', '-', 'x', '/', '%']:
            prev += operator
        else:
            prev += no

        # Calculate the result if there are at least two values and an operator
        if any(op in prev for op in ['+', '-', 'x', '/', '%']) and prev[-1] not in ['+', '-', 'x', '/', '%']:
            prev_ans = calculate(prev)

    if operator=='=':
        prev=str(prev_ans)
    label.configure(text=prev)
    Answer.configure(text=str(prev_ans))



def widgets(window,photo):
    #Creating the buttons/Labels
    
    Result = tk.Label(window, text="0", bg="black", width=12, fg="white", font=("Meiryo UI", 17))
    pressing = tk.Label(window, text="", bg="black", width=12, height=1, fg="white", font=("Meiryo UI", 17))
    Clear_all = tk.Button(window, text="AC", bg="#fd5800", width=4, height=2, border=3, fg="white",command= lambda: Calculations(pressing,"",Result,"AC") ,font=("Meiryo UI", 10, "bold"))
    modulus = tk.Button(window, text="%", bg="#292929", width=4, height=2, border=3, fg="white",command= lambda: Calculations(pressing,"",Result,"%"), font=("Meiryo UI", 10, "bold"))
    divide = tk.Button(window, text="/", bg="#292929", width=4, height=2, border=3, fg="white",command= lambda: Calculations(pressing,"",Result,'/'), font=("Meiryo UI", 10, "bold"))
    multiply = tk.Button(window, text="x", bg="#292929", width=4, height=2, border=3, fg="white",command= lambda: Calculations(pressing,"",Result,'x'), font=("Meiryo UI", 10, "bold"))
    plus=tk.Button(window, text="+", bg="#292929", width=4, height=2, border=3, fg="white",command= lambda: Calculations(pressing,"",Result,"+"), font=("Meiryo UI", 10, "bold"))
    minus=tk.Button(window, text="-", bg="#292929", width=4, height=2, border=3, fg="white",command= lambda: Calculations(pressing,"",Result,"-"), font=("Meiryo UI", 10, "bold"))
    seven=tk.Button(window, text="7", bg="#292929", width=4, height=2, border=3, fg="white", command=(lambda: Calculations(pressing,"7",Result,"")),font=("Meiryo UI", 10, "bold"))
    eight=tk.Button(window, text="8", bg="#292929", width=4, height=2, border=3, fg="white", command=(lambda: Calculations(pressing,"8",Result,"")),font=("Meiryo UI", 10, "bold"))
    nine=tk.Button(window, text="9", bg="#292929", width=4, height=2, border=3, fg="white", command=(lambda: Calculations(pressing,"9",Result,"")),font=("Meiryo UI", 10, "bold"))
    four=tk.Button(window, text="4", bg="#292929", width=4, height=2, border=3, fg="white", command=(lambda: Calculations(pressing,"4",Result,"")),font=("Meiryo UI", 10, "bold"))
    five=tk.Button(window, text="5", bg="#292929", width=4, height=2, border=3, fg="white", command=(lambda: Calculations(pressing,"5",Result,"")),font=("Meiryo UI", 10, "bold"))
    six=tk.Button(window, text="6", bg="#292929", width=4, height=2, border=3, fg="white", command=(lambda: Calculations(pressing,"6",Result,"")),font=("Meiryo UI", 10, "bold"))
    one=tk.Button(window, text="1", bg="#292929", width=4, height=2, border=3, fg="white", command=(lambda: Calculations(pressing,"1",Result,"")),font=("Meiryo UI", 10, "bold"))
    two=tk.Button(window, text="2", bg="#292929", width=4, height=2, border=3, fg="white", command=(lambda: Calculations(pressing,"2",Result,"")),font=("Meiryo UI", 10, "bold"))
    three=tk.Button(window, text="3", bg="#292929", width=4, height=2, border=3, fg="white", command=(lambda: Calculations(pressing,"3",Result,"")),font=("Meiryo UI", 10, "bold"))
    zero=tk.Button(window, text="0", bg="#292929", width=4, height=2, border=3, fg="white", command=(lambda: Calculations(pressing,"0",Result,"")),font=("Meiryo UI", 10, "bold"))
    dot=tk.Button(window, text=".", bg="#292929", width=4, height=2, border=3, fg="white", command=(lambda: Calculations(pressing,".",Result,"")),font=("Meiryo UI", 10, "bold"))
    undo=tk.Button(window,image=photo, width=4, height=80,bg="#292929",borderwidth=0,command=lambda: Calculations(pressing,"",Result,"undo"))
    equal=tk.Button(window, text="=", bg="#292929", width=4, height=4, border=3, fg="white", command=lambda: Calculations(pressing,"",Result,"=") ,font=("Meiryo UI", 10, "bold"))

    
    #Placing on screen
    Result.grid(row=0, column=0, columnspan=4)
    pressing.grid(row=1, column=0, columnspan=4)
    Clear_all.grid(row=2, column=0, sticky="ew", padx=10)
    modulus.grid(row=2, column=1,sticky="ew", padx=10)
    divide.grid(row=2, column=2,sticky="ew", padx=10)
    multiply.grid(row=2, column=3,sticky="ew", padx=10)
    minus.grid(row=3, column=3, pady=15,sticky="nsew", padx=10)
    plus.grid(row=4, column=3, pady=15,sticky="nsew", padx=10)
    seven.grid(row=3,column=0,padx=10,pady=15,sticky="nsew")
    eight.grid(row=3,column=1,padx=10,pady=15,sticky="nsew")
    nine.grid(row=3,column=2,padx=10,pady=15,sticky="nsew")
    four.grid(row=4,column=0,padx=10,pady=15,sticky="nsew")
    five.grid(row=4,column=1,padx=10,pady=15,sticky="nsew")
    six.grid(row=4,column=2,padx=10,pady=15,sticky="nsew")
    one.grid(row=5,column=0,padx=10,pady=15,sticky="nsew")
    two.grid(row=5,column=1,padx=10,pady=15,sticky="nsew")
    three.grid(row=5,column=2,padx=10,pady=15,sticky="nsew")
    zero.grid(row=6,column=0,padx=10,pady=15,sticky="nsew")
    dot.grid(row=6,column=1,padx=10,pady=15,sticky="nsew")
    undo.grid(row=6,column=2,padx=10,pady=15,sticky="nsew")
    equal.grid(row=5,column=3,padx=10,pady=15,sticky="nsew",rowspan=2)

    for i in range(4):
        window.grid_columnconfigure(i, weight=1)
    for i in range(3):
        window.grid_rowconfigure(i, weight=1)

prev=""
prev_ans=0
Starter_Code()
