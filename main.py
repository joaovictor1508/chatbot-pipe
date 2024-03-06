# -*- coding: utf-8 -*-
import tkinter as tk
from PIL import ImageTk, Image
import nltk
from chatbot import ChatBot
import time

nltk.download('punkt')
nltk.download('wordnet')

myChatBot = ChatBot()
myChatBot.loadModel()
#myChatBot.createModel()


def limpar_conversa():
  caixa_texto.config(state=tk.NORMAL)
  caixa_texto.delete(1.0, tk.END)
  caixa_texto.config(state=tk.DISABLED)


def enviar_mensagem(event=None):
  mensagem = caixa_entrada.get()
  exibir_mensagem_usuario(mensagem)
  resposta, _ = myChatBot.chatbot_response(mensagem)
  exibir_resposta_chatbot(resposta)
  caixa_entrada.delete(0, tk.END)


def exibir_mensagem_usuario(mensagem):
  caixa_texto.config(state=tk.NORMAL)
  caixa_texto.insert(tk.END, "Você: " + mensagem + "\n", "usuario")
  caixa_texto.config(state=tk.DISABLED)
  caixa_texto.yview(tk.END)
  caixa_entrada.delete(0, tk.END)


def exibir_resposta_chatbot(resposta):
  caixa_texto.config(state=tk.NORMAL)
  caixa_texto.insert(tk.END, "Chatbot: ", "chatbot")
  caixa_texto.config(state=tk.DISABLED)
  caixa_texto.yview(tk.END)
  janela.update()

  for palavra in resposta.split():
    caixa_texto.config(state=tk.NORMAL)
    caixa_texto.insert(tk.END, palavra + " ", "chatbot")
    caixa_texto.config(state=tk.DISABLED)
    caixa_texto.yview(tk.END)
    janela.update()
    time.sleep(0.1)

  caixa_texto.config(state=tk.NORMAL)
  caixa_texto.insert(tk.END, "\n", "chatbot")
  caixa_texto.config(state=tk.DISABLED)
  caixa_texto.yview(tk.END)


janela = tk.Tk()
janela.title("ChatBot")
janela.geometry("631x360")

# Adicionar imagem de background
imagem_de_background = Image.open("chatbot.png")
imagem_de_background = ImageTk.PhotoImage(imagem_de_background)
canvas = tk.Canvas(janela, width=631, height=360)
canvas.create_image(0, 0, anchor=tk.NW, image=imagem_de_background)
canvas.place(x=0, y=0)

# Caixa de texto - Exibir mensagens
caixa_texto = tk.Text(janela, height=19, width=37, wrap=tk.WORD)
caixa_texto.place(x=310, y=10)
caixa_texto.tag_config("usuario", foreground="blue")
caixa_texto.tag_config("chatbot", foreground="red")

# Caixa de Entrada
caixa_entrada = tk.Entry(janela, width=20)
caixa_entrada.place(x=310, y=325)
caixa_entrada.bind("<Return>", enviar_mensagem)

# Botão Enter
botao_enter = tk.Button(janela, text="Enter", command=enviar_mensagem)
botao_enter.place(x=483, y=320)

# Botão Limpar
botao_limpar = tk.Button(janela, text="Limpar", command=limpar_conversa)
botao_limpar.place(x=550, y=320)

janela.tk.call('encoding', 'system', 'utf-8')
caixa_entrada.focus()
janela.mainloop()
