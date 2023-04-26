import customtkinter as ctk 
from tkinter import *
from PIL import Image
janela = ctk.CTk()

janela.title("Rasterização")
janela.geometry("700x500")
janela.maxsize(width=700,height=700)
janela.minsize(width=500,height=500)
janela.resizable(width=False,height=False)
janela._set_appearance_mode("dark")

def novaTela():
    novaJanela = ctk.CTkToplevel(janela, fg_color="teal")
    novaJanela.geometry("200x200")

#btn = ctk.CTkButton(janela,text="Abrir nova janela",command=novaTela).place(x=200,y=200)

# frame1= ctk.CTkFrame(master=janela,width=200,height=430,fg_color="#FE2D00",bg_color="transparent",border_width=10,border_color="teal",corner_radius=30).place(x=10,y=60)
# frame2= ctk.CTkFrame(janela,width=200,height=430,fg_color="green").place(x=220,y=60)
# frame3 = ctk.CTkFrame(janela,width=200,height=430,fg_color="white").place(x=430,y=60)

# tabview = ctk.CTkTabview(janela,width=400,segmented_button_fg_color="red",segmented_button_selected_color="Green",segmented_button_unselected_color="blue",corner_radius=20)
# tabview.pack()
# tabview.add("Nomes")
# tabview.add("Idades")


# elemento = ctk.CTkLabel(tabview.tab("Nomes"),text="Mateus")
# elemento.pack()
# elemento = ctk.CTkLabel(tabview.tab("Idades"),text="21 anos")
# elemento.pack()

# scrollavel = ctk.CTkScrollbar(janela,width=10,button_color="red").place(x=690)

# textbox = ctk.CTkTextbox(janela,width=300,height=300,scrollbar_button_hover_color="red",scrollbar_button_color="green",border_color="red",border_width=1,corner_radius=15,border_spacing=20,fg_color="teal")
# textbox.pack()

# textbox.insert("0.0", "Título do seu texto\n\n" + "Olá, estou programando em Python com CustomTKinter\n\n"*20)

# def abrirDialog():
#     messagebox.showerror(title='Erro',message=f"Testando")
#     #dialog = ctk.CTkInputDialog(title="Caixa de dialogo",text="Digite o seu celular")
#     #print("Número: "+dialog.get_input())

# btn = ctk.CTkButton(janela, text="Abrir dialog",command=abrirDialog)
# btn.pack()

# ctk.CTkLabel(janela,text="Escolha o seu mês de nascimento: ",font=("arial bold",14)).pack()
# mes_var = ctk.StringVar(value="Selecione o mes")
# def mesEscolhido(escolha):
#     print(f"O seu mês de nascimento é {escolha}")

# mes = ctk.CTkOptionMenu(janela, values=["Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Outros"],command=mesEscolhido)
# mes.pack(pady=10)
# mes.set("Selecione o mes")

# mes = ctk.CTkOptionMenu(janela, values=["Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Outros"],command=mesEscolhido,variable=mes_var)
# mes.pack(pady=10)

ctk.CTkLabel(janela,text="Rasterização",font=("arial bold", 20)).pack(pady=20,padx=5)

# ctk.CTkLabel(janela, text="Este texto estático é de uma label").pack()

#text_var = ctk.StringVar(value=input("Digite o seu nome completo: "))

# def enviar():
#     t = entry.get()
#     lab.configure(text=str(t))
#     pass

# lab = ctk.CTkLabel(janela,text="",width=200,height=25,text_color="red",font=("arial bold", 16),fg_color="#005")
# lab.pack(pady=10)

# entry = ctk.CTkEntry(janela,width=200)
# entry.pack()

# ctk.CTkButton(janela,text="Enviar", width=200, command= enviar).pack(pady=10)

# entry = ctk.CTkEntry(janela,width=300,placeholder_text="Digite o seu nome completo",placeholder_text_color="green",fg_color="transparent",text_color="teal",font=("arial bold",16),border_width=2,border_color="#fff",state="normal",corner_radius=20)
# entry.pack(pady=20)

# def pegar():
#     print(entry.get())
#     entry.delete(0,END)

# ctk.CTkButton(janela, width=300, text="Pegar texto",command=pegar).pack()

# img = ctk.CTkImage(light_image=Image.open("./Icone.png"), dark_image=Image.open("./Icone.png"),size=(20,20))

# def evento():
#     print("Você clicou")
#     pass
# ctk.CTkButton(janela, text="Retas",command=evento,width=300,height=70,fg_color="transparent",hover_color="green",text_color="#fff",font=("arial bold", 18),border_color="#fff",border_width=3,border_spacing=20,corner_radius=20,image=img).pack(pady=30)

# img1 = ctk.CTkImage(light_image=Image.open("./Icone.png"),dark_image=Image.open("./Icone.png"),size=(100,100))
# img2 = ctk.CTkImage(light_image=Image.open("./polygon.png"),dark_image=Image.open("./polygon.png"),size=(20,20))

# ctk.CTkLabel(janela,text=None, image=img1).pack()
# ctk.CTkButton(janela, text="Retas",width=300,height=70,fg_color="transparent",hover_color="green",text_color="#fff",font=("arial bold", 18),border_color="#fff",border_width=3,border_spacing=20,corner_radius=20,image=img2).pack(pady=30)

def sliderValue(value):
    if value == 10:
        slider.configure(fg_color="red")
    else:
        slider.configure(fg_color="gray")
    print(value)

slider = ctk.CTkSlider(janela, from_=0,to=100,command=sliderValue,width=500,button_color="black",button_hover_color="red",button_length=10,progress_color="green",fg_color="gray")
slider.pack(pady=30)

janela.mainloop()