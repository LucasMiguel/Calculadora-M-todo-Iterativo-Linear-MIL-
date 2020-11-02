#!/usr/bin/python3
from tkinter import * #Biblioteca de interface gráfica
from tkinter import messagebox
from sympy import * #Biblioteca de operações matemáticas


varX = 0 ##vai ser a variavel que irá receber os valores das iterações
x = symbols('x') #isso vai determinar o x como um simbolo para que conseguirmos fazer as derivadas
class Application:
    sinal = 0 ##variavel que faz a verificação, para não adicionar o sinal duas vezes
    dotContr = 0 ##controla se um algarismo já tem um ponto
    equation = "" ## variavel onde ficará a função que será calculada
    varX0 = "" ## variavel que guardará o x inicial
    varNumInte = "" ## variável que guardará o numero de iterações
    varErro  = "" ## variavel que guardará o erro
    algarism = "" ##variavel que guarda o algarismo digitado
    def __init__(self, master=None):
        self.fontBtn = ("Arial, 20")
        
        # Containers -------------------------------------------------------------------------------------------------------------------------------
        self.containerImputs = Frame(master, highlightbackground="black", highlightcolor="black", highlightthickness=1, width=100, height=100, bd= 10)
        self.containerImputs.pack(fill=X)
        self.containerDisplay = Frame(master, bg="gray", highlightbackground="black", highlightcolor="black", highlightthickness=1, width=100, height=100, bd= 10)
        self.containerDisplay.pack(fill=X)
        self.containerBtns = Frame(master, highlightbackground="black", highlightcolor="black", highlightthickness=1, width=100, height=100, bd= 10, padx=30)
        self.containerBtns.pack(fill=X)
        self.containerInterations = Frame(master)
        self.containerInterations.pack(fill=X)
        # =====================================================================================================================
        ##campos X0
        self.labelX0 = Label(self.containerImputs, text="Xo:")
        self.labelX0.grid(row=0, column=0)
        self.fieldX0 = Entry(self.containerImputs)        
        self.fieldX0["width"] = 10
        self.fieldX0.grid(row=0, column=1)
        ##campos nº interações
        self.labelItera = Label(self.containerImputs, text="Nº Iterações:")
        self.labelItera.grid(row=0, column=2)
        self.fieldItera = Entry(self.containerImputs)
        self.fieldItera["width"] = 10
        self.fieldItera.grid(row=0, column=3)
        ##Margem de erro
        self.labelMargError = Label(self.containerImputs, text="Margem Erro:")
        self.labelMargError.grid(row=0, column=4)
        self.fieldMargError = Entry(self.containerImputs)
        self.fieldMargError["width"] = 10
        self.fieldMargError.grid(row=0, column=5)
        ##BtnConverg Botão que inicia as iterações
        self.btnConver = Button(self.containerImputs, bg="#FFFF00")
        self.btnConver["text"] = "Convergência"
        self.btnConver["width"] = 10
        self.btnConver.bind("<Button-1>", self.ActionConvergence)
        self.btnConver.grid(row=0, column=6, padx=10, pady=2)
        ##BtnInter Botão que inicia as iterações
        self.btnInter = Button(self.containerImputs, bg="#3CB371")
        self.btnInter["text"] = "Ini. Interações"
        self.btnInter["width"] = 10        
        self.btnInter.bind("<Button-1>", self.ActionBtnIterations)
        self.btnInter.grid(row=0, column=7, padx=10, pady=2)

        ##BtnHelp Botao de ajuda para
        self.btnHelp = Button(self.containerImputs, bg="#4682B4")
        self.btnHelp["text"] = "Info"
        self.btnHelp["width"] = 3
        self.btnHelp.bind("<Button-1>", self.ActionBtnHelp)
        self.btnHelp.grid(row=0, column=8, padx=20, pady=2)

        ##Display-----------------------------============================================================================================
        #Display onde vai ficar as equações
        self.display = Label(self.containerDisplay, text="", anchor='w')
        self.display["font"] = ("Verdana", "20", "bold")
        self.display["width"] = 60
        self.display["height"] = 2
        self.display.pack(fill=X)
        #Display onde vai ficar os resultados das equações
        self.displayResult = Label(self.containerDisplay, text="", anchor='e')
        self.displayResult["font"] = ("Verdana", "15", "bold")
        self.displayResult["width"] = 60
        self.displayResult["height"] = 2
        self.displayResult.pack(fill=X)

        ##Botões ---------- Aqui eu estou instanciando os botões, fazendo eles aparecerem na tela=========================================
            ##Btn7
        self.btn7 = Button(self.containerBtns, bg="#778899")
        self.btn7["text"] = "7"
        self.btn7["font"] = self.fontBtn
        self.btn7["width"] = 3
        self.btn7.bind("<Button-1>", self.AddBtn7)
        self.btn7.grid(row=0,column=0)
            ##Btn8
        self.btn8 = Button(self.containerBtns, bg="#778899")
        self.btn8["text"] = "8"
        self.btn8["font"] = self.fontBtn
        self.btn8["width"] = 3
        self.btn8.bind("<Button-1>", self.AddBtn8)
        self.btn8.grid(row=0,column=1)
            ##Btn9
        self.btn9 = Button(self.containerBtns, bg="#778899")
        self.btn9["text"] = "9"
        self.btn9["width"] = 3
        self.btn9.bind("<Button-1>", self.AddBtn9)
        self.btn9["font"] = self.fontBtn
        self.btn9.grid(row=0,column=2)
            ##Btn4
        self.btn4 = Button(self.containerBtns, bg="#778899")
        self.btn4["text"] = "4"
        self.btn4["font"] = self.fontBtn
        self.btn4["width"] = 3
        self.btn4.bind("<Button-1>", self.AddBtn4)
        self.btn4.grid(row=1,column=0)
            ##Btn5
        self.btn5 = Button(self.containerBtns, bg="#778899")
        self.btn5["text"] = "5"
        self.btn5["font"] = self.fontBtn
        self.btn5["width"] = 3
        self.btn5.bind("<Button-1>", self.AddBtn5)
        self.btn5.grid(row=1,column=1)
            ##Btn6
        self.btn6 = Button(self.containerBtns, bg="#778899")
        self.btn6["text"] = "6"
        self.btn6["font"] = self.fontBtn
        self.btn6["width"] = 3
        self.btn6.bind("<Button-1>", self.AddBtn6)
        self.btn6.grid(row=1,column=2)
            ##Btn1
        self.btn1 = Button(self.containerBtns, bg="#778899")
        self.btn1["text"] = "1"
        self.btn1["font"] = self.fontBtn
        self.btn1["width"] = 3
        self.btn1.bind("<Button-1>", self.AddBtn1)
        self.btn1.grid(row=2,column=0)
            ##Btn2
        self.btn2 = Button(self.containerBtns, bg="#778899")
        self.btn2["text"] = "2"
        self.btn2["font"] = self.fontBtn
        self.btn2["width"] = 3
        self.btn2.bind("<Button-1>", self.AddBtn2)
        self.btn2.grid(row=2,column=1)
            ##Btn3
        self.btn3 = Button(self.containerBtns, bg="#778899")
        self.btn3["text"] = "3"
        self.btn3["font"] = self.fontBtn
        self.btn3["width"] = 3
        self.btn3.bind("<Button-1>", self.AddBtn3)
        self.btn3.grid(row=2,column=2)
            ##Btn0
        self.btn0 = Button(self.containerBtns, bg="#778899")
        self.btn0["text"] = "0"
        self.btn0["font"] = self.fontBtn
        self.btn0["width"] = 3
        self.btn0.bind("<Button-1>", self.AddBtn0)
        self.btn0.grid(row=3,column=1)
            ##BtnDot
        self.btnDot = Button(self.containerBtns, bg="#B0C4DE")
        self.btnDot["text"] = "."
        self.btnDot["font"] = self.fontBtn
        self.btnDot["width"] = 3
        self.btnDot.bind("<Button-1>", self.AddBtnDot)
        self.btnDot.grid(row=3,column=0)
            ##BtnX
        self.btnX = Button(self.containerBtns, bg="#B0C4DE")
        self.btnX["text"] = "x"
        self.btnX["font"] = self.fontBtn
        self.btnX["width"] = 3
        self.btnX.bind("<Button-1>", self.AddBtnX)
        self.btnX.grid(row=3,column=2)
            ##BtnPlus
        self.btnPlus = Button(self.containerBtns, bg="#B0C4DE")
        self.btnPlus["text"] = "+"
        self.btnPlus["font"] = self.fontBtn
        self.btnPlus["width"] = 3
        self.btnPlus.bind("<Button-1>", self.AddBtnPlus)
        self.btnPlus.grid(row=0,column=3)
            ##BtnSub
        self.btnSub = Button(self.containerBtns, bg="#B0C4DE")
        self.btnSub["text"] = "-"
        self.btnSub["font"] = self.fontBtn
        self.btnSub["width"] = 3
        self.btnSub.bind("<Button-1>", self.AddBtnSub)
        self.btnSub.grid(row=1,column=3)
            ##BtnMult
        self.btnMult = Button(self.containerBtns, bg="#B0C4DE")
        self.btnMult["text"] = "*"
        self.btnMult["font"] = self.fontBtn
        self.btnMult["width"] = 3
        self.btnMult.bind("<Button-1>", self.AddBtnMult)
        self.btnMult.grid(row=2,column=3)
            ##BtnDiv
        self.btnDiv = Button(self.containerBtns, bg="#B0C4DE")
        self.btnDiv["text"] = "/"
        self.btnDiv["font"] = self.fontBtn
        self.btnDiv["width"] = 3
        self.btnDiv.bind("<Button-1>", self.AddBtnDiv)
        self.btnDiv.grid(row=3,column=3)
            ##BtnParLeft
        self.btnParLeft = Button(self.containerBtns, bg="#A9A9A9")
        self.btnParLeft["text"] = "("
        self.btnParLeft["font"] = self.fontBtn
        self.btnParLeft["width"] = 5
        self.btnParLeft.bind("<Button-1>", self.AddBtnParLeft)
        self.btnParLeft.grid(row=0,column=4)
            ##BtnParRight
        self.btnParRight = Button(self.containerBtns, bg="#A9A9A9")
        self.btnParRight["text"] = ")"
        self.btnParRight["font"] = self.fontBtn
        self.btnParRight["width"] = 5
        self.btnParRight.bind("<Button-1>", self.AddBtnParRight)
        self.btnParRight.grid(row=0, column=5)
            ##BtnSin
        self.btnSin = Button(self.containerBtns, bg="#A9A9A9")
        self.btnSin["text"] = "sin"
        self.btnSin["font"] = self.fontBtn
        self.btnSin["width"] = 5
        self.btnSin.bind("<Button-1>", self.AddBtnSin)
        self.btnSin.grid(row=1, column=4)
            ##BtnCos
        self.btnCos = Button(self.containerBtns, bg="#A9A9A9")
        self.btnCos["text"] = "cos"
        self.btnCos["font"] = self.fontBtn
        self.btnCos["width"] = 5
        self.btnCos.bind("<Button-1>", self.AddBtnCos)
        self.btnCos.grid(row=2, column=4)
            ##BtnTan
        self.btnTan = Button(self.containerBtns, bg="#A9A9A9")
        self.btnTan["text"] = "Tan"
        self.btnTan["font"] = self.fontBtn
        self.btnTan["width"] = 5
        self.btnTan.bind("<Button-1>", self.AddBtnTan)
        self.btnTan.grid(row=1, column=5)
            ##BtnXEX botão x elevado a X
        self.btnXEX = Button(self.containerBtns, bg="#A9A9A9")
        self.btnXEX["text"] = "X^x"
        self.btnXEX["font"] = self.fontBtn
        self.btnXEX["width"] = 5
        self.btnXEX.bind("<Button-1>", self.AddBtnXeX)
        self.btnXEX.grid(row=2, column=5)
            ##BtnSqrt = Botão de raiz quadrada
        self.btnSqrt = Button(self.containerBtns, bg="#A9A9A9")
        self.btnSqrt["text"] = "Sqrt"
        self.btnSqrt["font"] = self.fontBtn
        self.btnSqrt["width"] = 4
        self.btnSqrt.bind("<Button-1>", self.AddBtnSqrt)
        self.btnSqrt.grid(row=3,column=6)
            ##BtnAC
        self.btnAC = Button(self.containerBtns, bg="#FF8C00")
        self.btnAC["text"] = "AC"
        self.btnAC["font"] = self.fontBtn
        self.btnAC["width"] = 4
        self.btnAC.bind("<Button-1>", self.ClearDisplay)
        self.btnAC.grid(row=0,column=6)
            ##BtnLog
        self.btnLog = Button(self.containerBtns, bg="#A9A9A9")
        self.btnLog["text"] = "log"
        self.btnLog["font"] = self.fontBtn
        self.btnLog["width"] = 5
        self.btnLog.bind("<Button-1>", self.AddBtnLog)
        self.btnLog.grid(row=3,column=5)
            ##BtnEuler
        self.btnEuler = Button(self.containerBtns, bg="#A9A9A9")
        self.btnEuler["text"] = "e"
        self.btnEuler["font"] = self.fontBtn
        self.btnEuler["width"] = 4
        self.btnEuler.bind("<Button-1>", self.AddBtnEuler)
        self.btnEuler.grid(row=2,column=6)
            ##BtnDelete
        self.btnDelete = Button(self.containerBtns, bg="#FF8C00")
        self.btnDelete["text"] = "DEL"
        self.btnDelete["font"] = self.fontBtn
        self.btnDelete["width"] = 4
        self.btnDelete.bind("<Button-1>", self.ActionBtnDelete)
        self.btnDelete.grid(row=1, column=6)
            ##BtnEqual
        self.btnEqual = Button(self.containerBtns, bg="#006400")
        self.btnEqual["text"] = "="
        self.btnEqual["font"] = self.fontBtn
        self.btnEqual["width"] = 5
        self.btnEqual.bind("<Button-1>", self.ActionBtnEqual)
        self.btnEqual.grid(row=3,column=4)

        # --------------- FIM DOS BOTÕES -----------------------------------------------------------------------------------------------

        ##Display das Iterações ========================================================================================================
        self.labelIrations = Label(self.containerInterations, text="Iterações", anchor='center')
        self.labelIrations["font"] = ("Verdana", 15, "bold", "underline")
        self.labelIrations["pady"] = 5
        self.labelIrations.pack()
        self.scrollbar = Scrollbar(self.containerInterations)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.listbox = Listbox(self.containerInterations, yscrollcommand=self.scrollbar.set, font=("Verdana", 10))

    ##Funções============ Essas são as funções que adicionam os valores na variavel equation que é global, para isso cada função está
    # chamando a função addDisplay, que colocará o valor na tela e na variavel equation
    def AddBtn1(self, event):
        self.algarism += "1"
        self.AddDisplay("1")
        self.sinal = 0
    def AddBtn2(self, event):
        self.algarism += "2"
        self.AddDisplay("2")
        self.sinal = 0
    def AddBtn3(self, event):
        self.algarism += "3"
        self.AddDisplay("3")
        self.sinal = 0
    def AddBtn4(self, event):
        self.algarism += "4"
        self.AddDisplay("4")
        self.sinal = 0
    def AddBtn5(self, event):
        self.algarism += "5"
        self.AddDisplay("5")
        self.sinal = 0
    def AddBtn6(self, event):
        self.algarism += "6"
        self.AddDisplay("6")
        self.sinal = 0
    def AddBtn7(self, event):
        self.algarism += "7"
        self.AddDisplay("7")
        self.sinal = 0
    def AddBtn8(self, event):
        self.algarism += "8"
        self.AddDisplay("8")
        self.sinal = 0
    def AddBtn9(self, event):
        self.algarism += "9"
        self.AddDisplay("9")
        self.sinal = 0
    def AddBtn0(self, event):
        self.algarism += "0"
        self.AddDisplay("0")
        self.sinal = 0
    def AddBtnX(self, event):
        self.algarism += "x"
        self.AddDisplay("x")
        self.sinal = 0
    def AddBtnDot(self, event):
        if self.dotContr == 0:
            self.algarism += "."
            self.AddDisplay(".")
            self.dotContr = 1
    def AddBtnPlus(self, event):
        if self.sinal == 0:
            self.equation += self.algarism + "+"
            self.AddDisplay("+")
            self.sinal = 1
            self.dotContr = 0
            self.algarism = ""
    def AddBtnSub(self, event):
        if self.sinal == 0:
            self.equation += self.algarism + "-"
            self.AddDisplay("-")
            self.sinal = 1
            self.dotContr = 0
            self.algarism = ""
    def AddBtnMult(self, event):
        if self.sinal == 0:
            self.equation += self.algarism + "*"
            self.AddDisplay("*")
            self.sinal = 1
            self.dotContr = 0
            self.algarism = ""
    def AddBtnDiv(self, event):
        if self.sinal == 0:
            self.equation += self.algarism + "/"
            self.AddDisplay("/")
            self.sinal = 1
            self.dotContr = 0
            self.algarism = ""
    def AddBtnParLeft(self, event):
        self.algarism += "("
        self.AddDisplay("(")
    def AddBtnParRight(self, event):
        self.AddDisplay(")")
        self.equation += self.algarism + ")"
        self.sinal = 0
        self.dotContr = 0
        self.algarism = ""
    def AddBtnSin(self, event):
        self.algarism += "sin("
        self.AddDisplay("sin(")
    def AddBtnCos(self, event):
        self.algarism += "cos("
        self.AddDisplay("cos(")
    def AddBtnTan(self, event):
        self.algarism += "tan("
        self.AddDisplay("tan(")
    def AddBtnXeX(self, event):
        self.algarism += "**"
        self.AddDisplay("^")
    def AddBtnSqrt(self, event):
        self.algarism = "sqrt("
        self.AddDisplay("sqrt(")
    def AddBtnEuler(self, event):
        self.algarism += "e"
        self.AddDisplay("e")
    def AddBtnLog(self, event):
        self.algarism = "log10("
        self.AddDisplay("log(")
    ##Função que limpa o display e a variavel equation
    def ClearDisplay(self, event):
        self.display["text"] = ""
        self.equation = ""
        self.algarism = ""
        self.sinal = 0
        self.dotContr = 0
        self.display["text"] = ""
        self.displayResult['text'] = ""
        self.listbox.delete(0,END)
        self.listbox.pack(fill=BOTH)
        self.scrollbar.config(command=self.listbox.yview)
    
    ## Função que resolve a equação == é so um teste por enquanto
    def ActionBtnEqual(self, event):
        self.equation += self.algarism
        self.algarism = ""
        # print(self.equation)
        self.displayResult['fg'] = "blue"
        if self.fieldX0.get() != "":
            varX = float(self.fieldX0.get().replace(',', '.'))
            equationTemp = self.equation.replace('x', 'varX')
            self.displayResult["text"]= eval(equationTemp)
        else:
            self.displayResult["text"] = str(eval(self.equation))
    def ActionBtnHelp(self, event):
        msg = "Equipe:\n\n - Lucas Miguel\n - Ailton Soares\n - Diego Ramon\n - Gabriel\n - Lucas Almeida\n - Rafael Brito\n - Warley Junio"
        messagebox.showinfo("Sobre", msg)

    ## Função que Adicionar ao display os valores a variável equation=====================================================================================
    def AddDisplay(self, cont):
        self.display["text"] += cont
        # print("equacao:" + self.equation)
        # print("Algarismo: " + self.algarism)
    def ActionBtnDelete(self, event):
        self.equation += self.algarism
        self.algarism = ""
        if self.equation != "":
            # print("antes: " + self.equation)
            self.equation = self.equation[:-1]
            # print("Depois" + self.equation)
            self.display["text"] = self.equation
    #Função que testa se os campos e a equação existe e chama a função de calculo de convergência==========================================================
    def ActionConvergence(self, event):
        self.equation += self.algarism
        self.algarism = ""
        if self.fieldX0.get() == "":
            messagebox.showerror("Error", "Sem valor de Xo")
        elif self.equation == "":
            messagebox.showerror("Error", "Nenhuma equação")
        elif self.equation.find('x') == -1:
            messagebox.showerror("Error", "Equação sem variável")
        else:
            self.RunConvergence()

    # Função que calcula a convergencia da função===========================================================================================================
    def RunConvergence(self):
        self.varX0 = str(self.fieldX0.get())
        if self.varX0.find(',') != -1:
            self.varX0 = self.varX0.replace(',', '.')
        derivative = diff(self.equation, x).subs(x, float(self.varX0))
        # print("Equação: " + self.equation)
        # print("derivada: " + str(derivative))
        if derivative < 0:
            derivative *= -1
        if derivative < 1:
            self.displayResult['fg'] = "green"
        else:
            self.displayResult['fg'] = "red"

        derivative = float(derivative)
        self.displayResult['text'] = str(format(derivative, '.3f'))


    #Função que dispara o botão de interações================================================================================================================
    def ActionBtnIterations(self, event):
        global varx
        self.varNumInte = self.fieldItera.get()
        if self.fieldX0.get().find(','):
            self.varX0 = self.fieldX0.get().replace(',', '.')
        if self.varNumInte != "":
            if self.fieldItera.get().find(',') or self.fieldItera.get().find('.'):
                self.varNumInte = self.fieldItera.get()
                self.varNumInte = int(self.varNumInte)
            else:
                self.varNumInte = int(self.fieldItera.get())
        else:
            self.varNumInte = 0
        if self.fieldMargError.get() != "":
            self.varErro = float(self.fieldMargError.get().replace(',', '.'))
        else:
            self.varErro = 0
        self.equation += self.algarism
        self.algarism = ""
        if self.varX0 != 0 and self.equation != "" or self.varNumInte != 0 or self.varErro != 0:
            # print(varX)
            # print(self.varX0)
            # print(self.varNumInte)
            # print(self.varErro)
            # print(self.equation)
            self.RunIterations()
        else:
            messagebox.showerror("Error", "Falta Valores")

    #Função que gera as itereções=========================================================================================================
    def RunIterations(self):
        global varX
        varX = float(self.varX0)
        varAnt = 0
        varErroCheck = 0
        # print(varX)
        self.listbox.delete(0, END)
        equationTemp = self.equation.replace('x', 'varX')
        if self.varNumInte != 0:
            for i in range(int(self.varNumInte)):
                varAnt = varX
                varX = eval(equationTemp)
                # print("Iteração" + str(i) + " :" + str(varX))
                # self.contIntera = Label(self.containerInterations, text="Iteração " + str(i+1) + ": " + str(varX)).grid(row=i+1,column=0)
                self.listbox.insert(END, str("Iteração " + str(i+1) + " : F(" + str(format(varAnt,'.3f')) + ") = " + str(equationTemp).replace("varX", str(format(varAnt, '.3f'))) + " = " + str(format(varX, '.3f'))))
                if self.varErro != 0:
                    varErroCheck = varX - varAnt
                    if varErroCheck < 0:
                        varErroCheck *= -1
                    if varErroCheck <= self.varErro:
                        break
        else:
            while(true):
                i = 0
                varAnt = varX
                varX = eval(equationTemp)
                # print("Iteração" + str(i) + " :" + str(varX))
                # self.contIntera = Label(self.containerInterations, text="Iteração " + str(i+1) + ": " + str(varX)).grid(row=i+1,column=0)
                self.listbox.insert(END, str(
                    "Iteração " + str(i + 1) + " : F(" + str(format(varAnt, '.3f')) + ") = " + str(equationTemp).replace(
                        "varX", str(format(varAnt, '.3f'))) + " = " + str(format(varX, '.3f'))))
                if self.varErro != 0:
                    varErroCheck = varX - varAnt
                    if varErroCheck < 0:
                        varErroCheck *= -1
                    if varErroCheck <= self.varErro:
                        break
                i += 1
        self.listbox.pack(fill=BOTH)
        self.scrollbar.config(command=self.listbox.yview)

root = Tk()
root.geometry("750x700")
root.title("Calculadora MIL")
Application(root)
root.mainloop()
