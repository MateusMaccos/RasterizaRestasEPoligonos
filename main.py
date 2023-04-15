from tkinter import * 
from tkinter import ttk
import re
import matplotlib.pyplot as plt
import numpy as np
import random


master = Tk()
master.title("Rasterização de Retas e Polígonos")
master.geometry("400x150")
master.configure(background='lightblue')
master.resizable(False, False)


	

def Retas():
  #Função de Rasterização da RETA
  def Rasterizacao(reta):
    

    def novaCoord(oldX, oldY, W, H):
      newX = (oldX - (-1)) * W / 2
      newY = (oldY - (-1)) * H / 2
      return [newX, newY]

    def produzFragmento(x, y, matrix, cor):
      Xm = round(x)
      Ym = round(y)

      try:
        matrix[Ym][Xm] = cor
      except IndexError:
        print(
          "Aviso: A posição ({}, {}) está fora dos limites da matriz.".format(
            Xm, Ym))

    def algoritmoRasterizacao(X1, Y1, X2, Y2, H, W, matrix, cor):
      X1, Y1 = novaCoord(X1, Y1, H, W)
      X2, Y2 = novaCoord(X2, Y2, H, W)
      dx = X2 - X1
      dy = Y2 - Y1
      if (X1 == X2):
        m = 0
      else:
        m = dy / dx
      x = X1
      y = Y1
      b = y - m * x
      produzFragmento(x, y, matrix, cor)

      def funcPlotX(x, matrix):
        y = m * x + b
        produzFragmento(x, y, matrix, cor)

      def funcPlotY(y, matrix):
        produzFragmento(x, y, matrix, cor)
      incremento = 0.1
      if (x < X2):
        while (x < X2):
          x = x + incremento
          funcPlotX(x, matrix)
      elif (x == X2):
        if (y < Y2):
          while (y < Y2):
            y = y + incremento
            funcPlotY(y, matrix)
        else:
          while (y > Y2):
            y = y - incremento
            funcPlotY(y, matrix)
      else:
        while (x > X2):
          x = x - incremento
          funcPlotX(x, matrix)

    def produzArestas(arrayPontos, arrayArestas, H, W, matrix, cor):
      for ponto in range(0, len(arrayArestas)):
        primeiroPonto = arrayArestas[ponto][0]
        segundoPonto = arrayArestas[ponto][1]
        origemX = arrayPontos[primeiroPonto][0]
        origemY = arrayPontos[primeiroPonto][1]
        destinoX = arrayPontos[segundoPonto][0]
        destinoY = arrayPontos[segundoPonto][1]
        algoritmoRasterizacao(origemX, origemY, destinoX, destinoY, H, W, matrix,
                              cor)
    def produzRetasContinuas(arrayPontos,cores):
      for index in range(len(arrayPontos)):
        cor = cores[index]
        arrayRetas=[[0,1]]
        for ponto in range(0, len(arrayRetas)):
          primeiroPonto = arrayRetas[ponto][0]
          segundoPonto = arrayRetas[ponto][1]
          origemX = arrayPontos[index][primeiroPonto][0]
          origemY = arrayPontos[index][primeiroPonto][1]
          destinoX = arrayPontos[index][segundoPonto][0]
          destinoY = arrayPontos[index][segundoPonto][1]
          continuo = plt.subplot(2, 3, 6)
          continuo.set_xlim([-1, 1])
          continuo.set_ylim([-1, 1])
          print(origemX,origemY)
          print(destinoX,destinoY)
          continuo.plot([origemX, destinoX], [origemY, destinoY],
                  color=(cor[0] / 255, cor[1] / 255, cor[2] / 255))
          
    def desenhaReta(arrayPontos):
      resolucoes = [[100, 100],[300, 300],[600, 600], [800, 600],[1920, 1080]]
      cores = []
      for quantidadeRetas in range(len(arrayPontos)):
        cores.append([
          random.randint(0, 255),
          random.randint(0, 255),
          random.randint(0, 255)
        ])
      for resolucao in range(len(resolucoes)):
        matrix = np.zeros(
          (resolucoes[resolucao][1], resolucoes[resolucao][0], 3),
          dtype=np.uint8)
        for index in range(len(arrayPontos)):
            arrayRetas=[[0,1]]
            produzArestas(arrayPontos[index], arrayRetas, resolucoes[resolucao][0], resolucoes[resolucao][1], matrix, cores[index])     
        plt.subplot(2, 3, resolucao + 1)
        plt.imshow(matrix.astype("uint8"))
        plt.gca().invert_yaxis()
      produzRetasContinuas(arrayPontos,cores)
      plt.show()
    desenhaReta(reta)

  def pegarRetas():
      coords=[]
      for reta in lbllst:
          (x1, y1, x2 ,y2) = re.findall(r'-?\d+\.?\d*', reta[1].get())
          coords.append([[float(x1),float(y1)],[float(x2),float(y2)]])
      Rasterizacao(coords)

    

  #config gerais
  retaWindow = Toplevel()
  retaWindow.title("Rasterização de Retas")
  retaWindow.geometry("500x400+750+300")
  retaWindow.resizable(False, False)
  retaWindow.transient(master)
  retaWindow.focus_force()
  retaWindow.grab_set() 

  #Layout
  panel1 = PanedWindow(retaWindow, bd=4, relief='raised', bg='LightSkyBlue4', orient='horizontal')
  panel1.pack(fill='both', expand=1)

  left_label = Label(panel1,  bg='LightSkyBlue3')
  panel1.add(left_label)

  panel2 = PanedWindow(panel1, orient='vertical', bd=4, relief='raised',bg='LightSkyBlue3')
  panel1.add(panel2)

  right_label = Label(panel2, text="INPUTS", bg='LightSkyBlue3')
  panel2.add(right_label)
  #COnfigurando ScrollBar 
      ##Adicionando um Frame dentro da right_label
  scrollable_frame = Frame(right_label)
  scrollable_frame.pack(fill='both', expand=1)

      ##Adicionando a scrollbar ao Frame
  scrollbar = ttk.Scrollbar(scrollable_frame, orient=VERTICAL)
  scrollbar.pack(side=RIGHT, fill=Y)

      ##Configurando a scrollbar para controlar o conteúdo do Frame
  canvas = Canvas(scrollable_frame, yscrollcommand=scrollbar.set)
  canvas.pack(side=LEFT, fill=BOTH, expand=1)
  scrollbar.config(command=canvas.yview)

      ##Adicionando o conteúdo desejado ao canvas
  content_frame = Frame(canvas)
  canvas.create_window((0, 0), window=content_frame, anchor=NW)

      ##Adicionando os widgets desejados ao content_frame
  label = Label(content_frame, text="Reta 1 (x1,y1,x2,y2)",font=('Helvetica 40',10))
  label.pack(pady=10,padx=50)
  retas = Entry(content_frame)
  retas.pack(pady=10)
  lbllst = [(label,retas)]

  def addReta():
      label = Label(content_frame, text="Reta " + str(len(lbllst)+1) + " (x1,y1,x2,y2)",font=('Helvetica 40',10))
      label.pack(pady=10,padx=50)
      #account.place(relx=0.01, rely=0.125*(len(lbllst)+1))
      retas = Entry(content_frame)
      retas.pack(pady=10)
      lbllst.append((label,retas))

  def removeReta():
      tamanho = len(lbllst)
      lbllst[tamanho-1][0].destroy()
      lbllst[tamanho-1][1].destroy()
      lbllst.pop()

  #Definindo a porcetangem de ocupação da tela
  panel1.paneconfig(left_label, width=0.35*retaWindow.winfo_width())
  panel1.paneconfig(panel2, width=0.65*panel1.winfo_width())

  #left_label
      ##inserir título
  left_sub_title1 = Label(left_label, text="Rasterização de Retas", font=('Arial', 10), bg='LightSkyBlue3')
  left_sub_title2 = Label(left_label, text=" Configurações", font=('Arial', 10), bg='LightSkyBlue3')

  left_sub_title1.pack(pady=0)
  left_sub_title2.pack(pady=5)

      ##adcionar botões 
  button1 = Button(left_label, text= 'Adicionar Reta(s)',command=addReta)
  button1.pack(padx=5, pady=40)

  button2 = Button(left_label, text= 'Remover Reta(s)',command = removeReta)
  button2.pack(padx=5, pady=0)

  button3 = Button(left_label, text= 'Iniciar',command= pegarRetas)
  button3.pack(padx=5, pady=50)

      #sub título
  left_sub_title1 = Label(left_label, text="Não configure restas que estejam", font=('Arial', 10), bg='LightSkyBlue3')
  left_sub_title2 = Label(left_label, text="fora dos limites da matriz! [-1,1]", font=('Arial', 10), bg='LightSkyBlue3')
  left_sub_title3 = Label(left_label, text="Preencha todos os inputs!", font=('Arial', 10), bg='LightSkyBlue3')
  left_sub_title1.pack(pady=1)
  left_sub_title2.pack(pady=1)
  left_sub_title3.pack(pady=0)

 



	


def Polygons():	


  def find_internal_points(matrix, cor):
    horizontal = []
    # ler a matriz horizontalmente e guardar as posições internas
    for i in range(matrix.shape[0]):
      inside_polygon = False
      horizontalLinha = []
      counter = 0
      for j in range(matrix.shape[1]):
        if all(matrix[i][j] == cor):
          if j != matrix.shape[1] - 1:
            if all(matrix[i][j + 1] != cor):
              inside_polygon = not inside_polygon
              counter += 1
          else:
            inside_polygon = not inside_polygon
            counter += 1
        elif inside_polygon:
          horizontalLinha.append((i, j))
      if counter == 1 or counter == 0:
        horizontalLinha.clear()
      else:
        for elemento in horizontalLinha:
          horizontal.append(elemento)

    # pintar os pontos internos na matriz
    for point in horizontal:
      matrix[point[0]][point[1]] = cor


  

  def novaCoord(oldX, oldY, W, H):
    newX = (oldX - (-1)) * W / 2
    newY = (oldY - (-1)) * H / 2
    return [newX, newY]

  def produzFragmento(x, y, matrix, cor):
    Xm = round(x)
    Ym = round(y)

    try:
      matrix[Ym][Xm] = cor
    except IndexError:
      print(
        "Aviso: A posição ({}, {}) está fora dos limites da matriz.".format(
          Xm, Ym))

  def algoritmoRasterizacao(X1, Y1, X2, Y2, H, W, matrix, cor):
    X1, Y1 = novaCoord(X1, Y1, H, W)
    X2, Y2 = novaCoord(X2, Y2, H, W)
    dx = X2 - X1
    dy = Y2 - Y1
    if (X1 == X2):
      m = 0
    else:
      m = dy / dx
    x = X1
    y = Y1
    b = y - m * x
    produzFragmento(x, y, matrix, cor)

    def funcPlotX(x, matrix):
      y = m * x + b
      produzFragmento(x, y, matrix, cor)

    def funcPlotY(y, matrix):
      produzFragmento(x, y, matrix, cor)

    incremento = 0.1
    if (x < X2):
      while (x < X2):
        x = x + incremento
        funcPlotX(x, matrix)
    elif (x == X2):
      if (y < Y2):
        while (y < Y2):
          y = y + incremento
          funcPlotY(y, matrix)
      else:
        while (y > Y2):
          y = y - incremento
          funcPlotY(y, matrix)
    else:
      while (x > X2):
        x = x - incremento
        funcPlotX(x, matrix)

  def produzArestas(arrayPontos, arrayArestas, H, W, matrix, cor):
    for ponto in range(0, len(arrayArestas)):
      primeiroPonto = arrayArestas[ponto][0]
      segundoPonto = arrayArestas[ponto][1]
      origemX = arrayPontos[primeiroPonto][0]
      origemY = arrayPontos[primeiroPonto][1]
      destinoX = arrayPontos[segundoPonto][0]
      destinoY = arrayPontos[segundoPonto][1]
      algoritmoRasterizacao(origemX, origemY, destinoX, destinoY, H, W, matrix,
                            cor)

  def produzLinhasContinuas(arrayPontos, cores):
    for index in range(len(arrayPontos)):
      cor = cores[index]
      arrayArestas = []
      for j in range(len(arrayPontos[index])):
        if j != (len(arrayPontos[index]) - 1):
          arrayArestas.append((j, j + 1))
        else:
          arrayArestas.append((j, 0))
      for ponto in range(0, len(arrayArestas)):
        primeiroPonto = arrayArestas[ponto][0]
        segundoPonto = arrayArestas[ponto][1]
        origemX = arrayPontos[index][primeiroPonto][0]
        origemY = arrayPontos[index][primeiroPonto][1]
        destinoX = arrayPontos[index][segundoPonto][0]
        destinoY = arrayPontos[index][segundoPonto][1]
        continuo = plt.subplot(2, 3, 6)
        continuo.set_xlim([-1, 1])
        continuo.set_ylim([-1, 1])
        continuo.plot([origemX, destinoX], [origemY, destinoY],
                color=(cor[0] / 255, cor[1] / 255, cor[2] / 255))

  def preenchePoligonos(arrayPontos):
    resolucoes = [[100, 100], [300, 300], [600, 600], [800, 600], [1920, 1080]]
    cores = []
    for quantidadePol in range(len(arrayPontos)):
      cores.append([
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255)
      ])
    for resolucao in range(len(resolucoes)):
      matrix = np.zeros(
        (resolucoes[resolucao][1], resolucoes[resolucao][0], 3),
        dtype=np.uint8)
      for index in range(len(arrayPontos)):
        arrayArestas = []
        for j in range(len(arrayPontos[index])):
          if j != (len(arrayPontos[index]) - 1):
            arrayArestas.append((j, j + 1))

          else:
            arrayArestas.append((j, 0))
        produzArestas(arrayPontos[index], arrayArestas,
                      resolucoes[resolucao][0], resolucoes[resolucao][1],
                      matrix, cores[index])

        find_internal_points(matrix, cores[index])
      plt.subplot(2, 3, resolucao + 1)
      plt.imshow(matrix.astype("uint8"))
      plt.gca().invert_yaxis()
    produzLinhasContinuas(arrayPontos, cores)
    plt.show()


  def pegarPolygons():
    count = 0
    allPolygons = []
    for polygon in listP:
        coordPolygon = []
        count+=1
        inputList = re.findall(r'-?\d+\.?\d*', polygon[1].get())
        for index in range(len(inputList)-1):
          if index%2==0:
            coordPolygon.append((float(inputList[index]), float(inputList[index+1])))
        allPolygons.append(coordPolygon)
    preenchePoligonos(allPolygons)  
          
      
   
  PWindow = Toplevel()
  PWindow.title("Rasterização de Polígonos")
  PWindow.geometry("500x400+750+300")
  PWindow.resizable(False, False)
  PWindow.transient(master)
  PWindow.focus_force()
  PWindow.grab_set() 

  #Layout
  panel1 = PanedWindow(PWindow, bd=4, relief='raised', bg='LightSkyBlue4', orient='horizontal')
  panel1.pack(fill='both', expand=1)

  left_label = Label(panel1,  bg='LightSkyBlue3')
  panel1.add(left_label)

  panel2 = PanedWindow(panel1, orient='vertical', bd=4, relief='raised',bg='LightSkyBlue3')
  panel1.add(panel2)

  right_label = Label(panel2, text="INPUTS", bg='LightSkyBlue3')
  panel2.add(right_label)
  #COnfigurando ScrollBar 
      ##Adicionando um Frame dentro da right_label
  scrollable_frame = Frame(right_label)
  scrollable_frame.pack(fill='both', expand=1)

      ##Adicionando a scrollbar ao Frame
  scrollbar = ttk.Scrollbar(scrollable_frame, orient=VERTICAL)
  scrollbar.pack(side=RIGHT, fill=Y)

      ##Configurando a scrollbar para controlar o conteúdo do Frame
  canvas = Canvas(scrollable_frame, yscrollcommand=scrollbar.set)
  canvas.pack(side=LEFT, fill=BOTH, expand=1)
  scrollbar.config(command=canvas.yview)

      ##Adicionando o conteúdo desejado ao canvas
  content_frame = Frame(canvas)
  canvas.create_window((0, 0), window=content_frame, anchor=NW)

      ##Adicionando os widgets desejados ao content_frame
  label = Label(content_frame, text="Polígono 1 [(x1,y1),(x2,y2),...]",font=('Helvetica 40',10))
  label.pack(pady=10,padx=50)
  polygon = Entry(content_frame)
  polygon.pack(pady=10)
  listP = [(label,polygon)]

  def addPolygon():
      label = Label(content_frame, text="Polígono " + str(len(listP)+1) + " [(x1,y1),(x2,y2),...]",font=('Helvetica 40',10))
      label.pack(pady=10,padx=50)
      
      polygon = Entry(content_frame)
      polygon.pack(pady=10)
      listP.append((label,polygon))

  def removePolygon():
      tamanho = len(listP)
      listP[tamanho-1][0].destroy()
      listP[tamanho-1][1].destroy()
      listP.pop()

  #Definindo a porcetangem de ocupação da tela
  panel1.paneconfig(left_label, width=0.35*PWindow.winfo_width())
  panel1.paneconfig(panel2, width=0.65*panel1.winfo_width())

  #left_label
      ##inserir título
  left_sub_title1 = Label(left_label, text="Rasterização de Polígonos", font=('Arial', 10), bg='LightSkyBlue3')
  left_sub_title2 = Label(left_label, text=" Configurações", font=('Arial', 10), bg='LightSkyBlue3')

  left_sub_title1.pack(pady=0)
  left_sub_title2.pack(pady=5)

      ##adcionar botões 
  button1 = Button(left_label, text= 'Adicionar Polígono(s)',command=addPolygon)
  button1.pack(padx=5, pady=40)

  button2 = Button(left_label, text= 'Remover Polígono(s)',command = removePolygon)
  button2.pack(padx=5, pady=0)

  button3 = Button(left_label, text= 'Iniciar', command= pegarPolygons)
  button3.pack(padx=5, pady=50)

      #sub título
  left_sub_title1 = Label(left_label, text="Não configure polígonos que estejam", font=('Arial', 10), bg='LightSkyBlue3')
  left_sub_title2 = Label(left_label, text="fora dos limites da matriz! [-1,1]", font=('Arial', 10), bg='LightSkyBlue3')
  left_sub_title3 = Label(left_label, text="Preencha todos os inputs!", font=('Arial', 10), bg='LightSkyBlue3')
  left_sub_title1.pack(pady=1)
  left_sub_title2.pack(pady=1)
  left_sub_title3.pack(pady=0)




label = Label(master,
			text ="Selecione o tipo de rasterização")

label.pack(pady = 10)

# a button widget which will open a
# new window on button click
btn = Button(master,
			text ="Retas",
			command = Retas)
btn.pack(pady = 10)

btn2 = Button(master,
            text="Polígonos",
            command =  Polygons)
btn2.pack(pady=10)

# mainloop, runs infinitely
mainloop()
