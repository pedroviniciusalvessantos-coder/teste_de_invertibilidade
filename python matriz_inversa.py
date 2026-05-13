import tkinter as tk
from tkinter import messagebox
import numpy as np

# Função para calcular a inversa
def calcular_inversa():
    try:
        # Pegando os valores da matriz
        a = float(entrada_a.get())
        b = float(entrada_b.get())
        c = float(entrada_c.get())
        d = float(entrada_d.get())

        # Criando matriz
        matriz = np.array([[a, b],
                           [c, d]])

        # Calculando determinante
        det = np.linalg.det(matriz)

        # Limpando resultado anterior
        resultado_texto.config(state="normal")
        resultado_texto.delete(1.0, tk.END)

        # Mostrando matriz
        resultado_texto.insert(tk.END, "MATRIZ INFORMADA:\n")
        resultado_texto.insert(tk.END, f"{matriz}\n\n")

        # Mostrando determinante
        resultado_texto.insert(tk.END, f"Determinante: {det:.2f}\n\n")

        # Verificando invertibilidade
        if det != 0:
            inversa = np.linalg.inv(matriz)

            resultado_texto.insert(
                tk.END,
                "STATUS: MATRIZ INVERTÍVEL\n\n"
            )

            resultado_texto.insert(
                tk.END,
                "MATRIZ INVERSA:\n"
            )

            resultado_texto.insert(
                tk.END,
                f"[ {inversa[0][0]:.2f}   {inversa[0][1]:.2f} ]\n"
            )

            resultado_texto.insert(
                tk.END,
                f"[ {inversa[1][0]:.2f}   {inversa[1][1]:.2f} ]\n"
            )

        else:
            resultado_texto.insert(
                tk.END,
                "STATUS: MATRIZ NÃO INVERTÍVEL\n"
            )

            resultado_texto.insert(
                tk.END,
                "Motivo: determinante igual a zero."
            )

        resultado_texto.config(state="disabled")

    except:
        messagebox.showerror(
            "Erro",
            "Digite apenas números válidos."
        )

# Janela principal
janela = tk.Tk()
janela.title("Teste de Invertibilidade")
janela.geometry("700x600")
janela.configure(bg="#1e1e1e")

# Título
titulo = tk.Label(
    janela,
    text="TESTE DE INVERTIBILIDADE",
    font=("Arial", 22, "bold"),
    bg="#1e1e1e",
    fg="#00ffcc"
)

titulo.pack(pady=20)

# Frame da matriz
frame = tk.Frame(janela, bg="#1e1e1e")
frame.pack(pady=10)

# Entradas da matriz
entrada_a = tk.Entry(frame, width=8, font=("Arial", 18), justify="center")
entrada_b = tk.Entry(frame, width=8, font=("Arial", 18), justify="center")
entrada_c = tk.Entry(frame, width=8, font=("Arial", 18), justify="center")
entrada_d = tk.Entry(frame, width=8, font=("Arial", 18), justify="center")

entrada_a.grid(row=0, column=0, padx=10, pady=10)
entrada_b.grid(row=0, column=1, padx=10, pady=10)
entrada_c.grid(row=1, column=0, padx=10, pady=10)
entrada_d.grid(row=1, column=1, padx=10, pady=10)

# Botão
botao = tk.Button(
    janela,
    text="CALCULAR",
    font=("Arial", 16, "bold"),
    bg="#00ffcc",
    fg="black",
    padx=20,
    pady=10,
    command=calcular_inversa
)

botao.pack(pady=20)

# Área de resultado
resultado_texto = tk.Text(
    janela,
    height=15,
    width=60,
    font=("Consolas", 14),
    bg="#2b2b2b",
    fg="white"
)

resultado_texto.pack(pady=20)

resultado_texto.config(state="disabled")

# Rodar janela
janela.mainloop()