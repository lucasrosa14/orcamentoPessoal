# imports
from tkinter import *
from tkinter import Tk, ttk
from PIL import Image, ImageTk
from tkinter.ttk import Progressbar
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt 
from matplotlib.figure import Figure
from tkcalendar import Calendar, DateEntry
from datetime import date


# cores 
co0 = "#2e2d2b"  
co1 = "#feffff"  
co2 = "#4fa882"  
co3 = "#38576b"  
co4 = "#403d3d"   
co5 = "#e06636"   
co6 = "#038cfc"   
co7 = "#3fbfb9"   
co8 = "#263238"   
co9 = "#e9edf5"   

colors = ['#008000', '#FF0000', '#66bbbb','#99bb55', '#ee9944', '#444466', '#bb5555']

# Criando a janela
janela = Tk()
janela.title()
janela.geometry('1400x660')
janela.configure(background=co9)
janela.resizable(width=FALSE, height=FALSE)

style = ttk.Style(janela)
style.theme_use("clam")

# Criando frames
frameCima = Frame(janela, width=2000, height=50, bg=co1, relief="flat")
frameCima.grid(row=0, column=0)

frameMeio = Frame(janela, width=1500, height=360, bg=co1, pady=20, relief="raised")
frameMeio.grid(row=1, column=0, pady=1,padx=0, sticky=NSEW)

frameBaixo = Frame(janela, width=1500, height=1000, bg=co1, relief="flat")
frameBaixo.grid(row=2 , column=0, pady=0,padx=10, sticky=NSEW)

frameGrafPizza = Frame(frameMeio, width=580, height=250, bg=co2)
frameGrafPizza.place(x=415, y=5)

frameTabelaDespesa = Frame(frameBaixo, width=500, height=250, bg=co1, relief="flat")
frameTabelaDespesa.grid(row=0, column=0)

frameCrud = Frame(frameMeio, width=500, height=300, bg=co4, relief="flat")
frameCrud.place(x=880, y=1)

frameConfig = Frame(frameBaixo, width=250, height=250, bg=co1, relief="flat")
frameConfig.grid(row=0, column=3, padx=5)

# Incluindo logo
app_img = Image.open('logo.png')
app_img = app_img.resize((45,45))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(frameCima, image=app_img, text=" Orçamento Pessoal", width=1500, compound=LEFT, padx=5, relief=RAISED, anchor=NW, font=('Verdana 20 bold'), bg=co1, fg=co4)
app_logo.place(x=0, y=0)

# Criando barra de progresso de porcentagem de receita
def percent():
    lblNome = Label(frameMeio, text="Receita disponível", height=1, anchor=NW, font=('Verdana 12'), bg=co1, fg=co4)
    lblNome.place(x=7, y=5)

    style = ttk.Style()
    style.theme_use('default')
    style.configure("black.Horizontal.TProgressbar", background='#daed6b')
    style.configure("TProgressbar", thickness=25)
    bar = Progressbar(frameMeio, length=180, style='black.Horizontal.TProgressbar')
    bar.place(x=10, y=35)
    bar['value'] = 50

    valor = 50
    lblPorcentagem = Label(frameMeio, text="{:,.2f}%".format(valor), anchor=NW, font=('Verdana 12'), bg=co1, fg=co4)
    lblPorcentagem.place(x=200, y=35)

# Criando gráfico de barras
def graficoBarra():
    listaCategorias = ['Renda', 'Despesas', 'Saldo']
    listaValores = [3000, 2000, 1000]
    
    figura = plt.Figure(figsize=(4, 3.45), dpi=60)
    ax = figura.add_subplot(111)
    ax.autoscale(enable=True, axis='both', tight=None)
    ax.bar(listaCategorias, listaValores,  color=colors, width=0.9)
    
    c = 0
    for i in ax.patches:
        ax.text(i.get_x()-.001, i.get_height()+.5,
                str("{:,.0f}".format(listaValores[c])), fontsize=17, fontstyle='italic',  verticalalignment='bottom',color='dimgrey')
        c += 1

    ax.set_xticklabels(listaCategorias,fontsize=16)
    ax.patch.set_facecolor('#ffffff')
    ax.spines['bottom'].set_color('#CCCCCC')
    ax.spines['bottom'].set_linewidth(1)
    ax.spines['right'].set_linewidth(0)
    ax.spines['top'].set_linewidth(0)
    ax.spines['left'].set_color('#CCCCCC')
    ax.spines['left'].set_linewidth(1)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.tick_params(bottom=False, left=False)
    ax.set_axisbelow(True)
    ax.yaxis.grid(False, color='#EEEEEE')
    ax.xaxis.grid(False)

    canva = FigureCanvasTkAgg(figura, frameMeio)
    canva.get_tk_widget().place(x=10, y=70)

# Criando Resumo
def mostraResumo():
    valor = [3000, 2000, 1000]

    lblLinha = Label(frameMeio, text="", width=215, height=1, anchor=NW, font=('Arial 1'), bg='#545454')
    lblLinha.place(x=309, y=52)
    lblRenda = Label(frameMeio, text="Total Renda                    ".upper(), anchor=NW, font=('Verdana 12 bold'), bg=co1, fg='#83a9e6')
    lblRenda.place(x=309, y=35)
    lblRenda = Label(frameMeio, text="R$ {:,.2f}".format(valor[0]),anchor=NW, font=('Arial 17'), bg=co1, fg='#545454')
    lblRenda.place(x=309, y=60)

    lblLinha = Label(frameMeio, text="", width=215, height=1, anchor=NW, font=('Arial 1'), bg='#545454')
    lblLinha.place(x=309, y=122)
    lblDespesa = Label(frameMeio, text="Total Despesas             ".upper(), anchor=NW, font=('Verdana 12 bold'), bg=co1, fg='#83a9e6')
    lblDespesa.place(x=309, y=105)
    lblDespesa = Label(frameMeio, text="R$ {:,.2f}".format(valor[1]), anchor=NW, font=('Arial 17'), bg=co1, fg='#545454')
    lblDespesa.place(x=309, y=130)

    lblLinha = Label(frameMeio, text="", width=215, height=1, anchor=NW, font=('Arial 1'), bg='#545454')
    lblLinha.place(x=309, y=192)
    lblSaldo = Label(frameMeio, text="Total Saldo                    ".upper(), anchor=NW, font=('Verdana 12 bold'), bg=co1, fg='#83a9e6')
    lblSaldo.place(x=309, y=175)
    lblSaldo = Label(frameMeio, text="R$ {:,.2f}".format(valor[2]), anchor=NW, font=('Arial 17'), bg=co1, fg='#545454')
    lblSaldo.place(x=309, y=200)

# Cria gráfico de pizza
def graficoPizza():
    figura = plt.Figure(figsize=(5, 3), dpi=90)
    ax = figura.add_subplot(111)

    listaValores = [3000,2000,1000]
    listaCategorias = ['Renda', 'Despesa', 'Saldo']

    explode = []
    for i in listaCategorias:
        explode.append(0.05)

    ax.pie(listaValores, explode=explode, wedgeprops=dict(width=0.2), autopct='%1.1f%%', colors=colors,shadow=True, startangle=90)
    ax.legend(listaCategorias, loc="center right", bbox_to_anchor=(1.55, 0.50))

    canvaCategoria = FigureCanvasTkAgg(figura, frameGrafPizza)
    canvaCategoria.get_tk_widget().grid(row=0, column=0)

percent()
graficoBarra()
mostraResumo()
graficoPizza()

# Criando tabelas
appTabelaDespesa = Label(frameMeio, text="Tabela de Despesas", anchor=NW, font=('Verdana 12'), bg=co1, fg=co4)
appTabelaDespesa.place(x=5, y=310)

def mostraTabelaDespesa():
    tabela_head = ['#Id','Categoria','Valor', 'Data Inclusão','Tipo de Pagamento', 'Tipo de Despesa', 'Usuário', 'Observação']
    lista_itens = [[1,2,3,4,5,6,7,8],[1,2,3,4,5,6,7],[1,2,3,4,5,6,7],[1,2,3,4,5,6,7],[1,2,3,4,5,6,7],[1,2,3,4,5,6,7],[1,2,3,4,5,6,7],[1,2,3,4,5,6,7]]
    
    global tree

    tree = ttk.Treeview(frameTabelaDespesa, selectmode="extended",columns=tabela_head, show="headings")
    vsb = ttk.Scrollbar(frameTabelaDespesa, orient="vertical", command=tree.yview)
    hsb = ttk.Scrollbar(frameTabelaDespesa, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')

    hd=["center","center","center", "center", "center", "center", "center", "center"]
    h=[30,100,50,100,120,120,70,120]
    n=0

    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor=CENTER)
        tree.column(col, width=h[n],anchor=hd[n])
        
        n+=1

    for item in lista_itens:
        tree.insert('', 'end', values=item)

appTabela = Label(frameMeio, text="Tabela de Receitas", anchor=NW, font=('Verdana 12'), bg=co1, fg=co4)
appTabela.place(x=750, y=310)

def mostraTabelaReceita():
    tabela_head = ['#Id','Categoria','Valor', 'Data Inclusão', 'Usuário', 'Observação']
    lista_itens = [[1,2,3,4,5,6],[1,2,3,4,5,6]]
    
    global tree

    tree = ttk.Treeview(frameTabelaDespesa, selectmode="extended",columns=tabela_head, show="headings")
    vsb = ttk.Scrollbar(frameTabelaDespesa, orient="vertical", command=tree.yview)
    hsb = ttk.Scrollbar(frameTabelaDespesa, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(column=4, row=0, sticky='nsew')
    vsb.grid(column=5, row=0, sticky='ns')
    hsb.grid(column=4, row=1, sticky='ew')

    hd=["center","center","center", "center", "center", "center", ]
    h=[30,100,50,100,70,120]
    n=0

    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor=CENTER)
        tree.column(col, width=h[n],anchor=hd[n])
        
        n+=1

    for item in lista_itens:
        tree.insert('', 'end', values=item)

mostraTabelaDespesa()
mostraTabelaReceita()

# Inserir Despesa
lblDescricaoDespesa = Label(frameCrud, text='Nova Despesa', height=1, anchor=NW, font=('Verdana 10 bold'), bg=co1, fg=co4)
lblDescricaoDespesa.place(x=10, y=10)

lblCategoriaDespesa = Label(frameCrud, text='Categoria', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
lblCategoriaDespesa.place(x=10, y=35)

categoriaDespesa = ['Alimentação','Lazer','Educação','Aluguel','Combustível']
listaCategoriaDespesa = []

for i in categoriaDespesa:
    listaCategoriaDespesa.append(i[1])

comboCategDespesa = ttk.Combobox(frameCrud, width=10, height=1, font=('Ivy 10'))
comboCategDespesa['values'] = (listaCategoriaDespesa)
comboCategDespesa.place(x=80, y=35)

lblDataDespesa = Label(frameCrud, text='Data', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
lblDataDespesa.place(x=10, y=60)

calDataDespesa = DateEntry(frameCrud, width=12, background='darkblue', foreground='white', borderwidth=2, year=2023)
calDataDespesa.place(x=80, y=60)

lblValorDespesa = Label(frameCrud, text='Valor', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
lblValorDespesa.place(x=10, y=85)

inputValorDespesa = Entry(frameCrud, width=14, justify='left', relief='solid')
inputValorDespesa.place(x=80, y=85)

btnInserirDespesa = Button(frameCrud, text='Inserir'.upper(),width=19, compound=CENTER, font=('Ivy 10 bold'), bg=co1, fg=co0, overrelief=RIDGE)
btnInserirDespesa.place(x=10, y=110)

# Inserir Receita
lblDescricaoReceita = Label(frameCrud, text='Nova Receita', height=1, anchor=NW, font=('Verdana 10 bold'), bg=co1, fg=co4)
lblDescricaoReceita.place(x=250, y=10)

lblCategoriaReceita = Label(frameCrud, text='Categoria', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
lblCategoriaReceita.place(x=250, y=35)

categoriaReceita = ['Salário','Outros']
listacategoriaReceita = []

for i in categoriaReceita:
    listacategoriaReceita.append(i[1])

comboCategReceita = ttk.Combobox(frameCrud, width=10, height=1, font=('Ivy 10'))
comboCategReceita['values'] = (listacategoriaReceita)
comboCategReceita.place(x=320, y=35)

lblDataDespesa = Label(frameCrud, text='Data', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
lblDataDespesa.place(x=250, y=60)

calDataDespesa = DateEntry(frameCrud, width=12, background='darkblue', foreground='white', borderwidth=2, year=2023)
calDataDespesa.place(x=320, y=60)

lblValorDespesa = Label(frameCrud, text='Valor', height=1, anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
lblValorDespesa.place(x=250, y=85)

inputValorDespesa = Entry(frameCrud, width=14, justify='left', relief='solid')
inputValorDespesa.place(x=320, y=85)

btnInserirDespesa = Button(frameCrud, text='Inserir'.upper(),width=19, compound=CENTER, font=('Ivy 10 bold'), bg=co1, fg=co0, overrelief=RIDGE)
btnInserirDespesa.place(x=250, y=110)


janela.mainloop()

