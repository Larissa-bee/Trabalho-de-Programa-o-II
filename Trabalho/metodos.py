
import tkinter as tk
from funçoes import somar, subtrair, multiplicar, dividir, raiz_quadrada 

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora")
        master.geometry("250x250")

        # Criado para inserir textos

        self.entry = tk.Entry(master, width=20)
        self.entry.grid(row=0, column=0, columnspan=4)

        # Aqui é onde cria os botões
        
        buttons = [

            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            tk.Button(master, text=button, width=5, command=lambda button=button: self.click_button(button)).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        # Aqui o botão de limparr
        #clear função de limpar

        tk.Button(master, text="C", width=5, command=self.clear).grid(row=row_val, column=0, columnspan=4)

    def click_button(self, button):
        if button == '=':
            try:
                result = eval(self.entry.get())
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, result)
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Erro")
        else:
            self.entry.insert(tk.END, button)

    def clear(self):
        self.entry.delete(0, tk.END)

#Chamando a função
if __name__=='__main__':
    root = tk.Tk()
    my_calculator = Calculator(root)
    root.mainloop()