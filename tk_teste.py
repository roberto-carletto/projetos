import tkinter as tk


window = tk.Tk()
window.title('Seleção de Hubs')
window.geometry('500x350')

def confirmar():

    lista = [var1.get(),var2.get(),var3.get(),var4.get(),var5.get(),var6.get(),var7.get(),var8.get()]
    if lista == [0,0,0,0,0,0,0,0]:
        closing = tk.Tk()
        closing.title('Confirmação')
        closing.geometry('300x200')
        t = tk.Label(closing, bg='white', text='Nenhum Hub selecionado.\nDeseja prosseguir?', font= ('Aerial', 15))
        t.pack()
        s = tk.Button(closing, text ="Confirmar", command=lambda:[window.destroy(), closing.destroy()])
        s.place(x=70,y=120)
        n = tk.Button(closing, text ="Retornar", command=closing.destroy)
        n.place(x=170,y=120)

    else:
        window.destroy()



l = tk.Label(window, bg='white',text='Escolha os hubs a serem utilizados:',font= ('Aerial', 15))
l.pack()

var1 = tk.IntVar()
c1 = tk.Checkbutton(window, text='Barra',variable=var1, onvalue=1, offvalue=0, anchor='w', width=10)
c1.pack()
var2 = tk.IntVar()
c2 = tk.Checkbutton(window, text='São Cristóvão',variable=var2, onvalue=1, offvalue=0, anchor='w', width=10)
c2.pack()
var3 = tk.IntVar()
c3 = tk.Checkbutton(window, text='Tatuapé',variable=var3, onvalue=1, offvalue=0, anchor='w', width=10)
c3.pack()
var4 = tk.IntVar()
c4 = tk.Checkbutton(window, text='Vila Olímpia',variable=var4, onvalue=1, offvalue=0, anchor='w', width=10)
c4.pack()
var5 = tk.IntVar()
c5 = tk.Checkbutton(window, text='São Bernardo',variable=var5, onvalue=1, offvalue=0, anchor='w', width=10)
c5.pack()
var6 = tk.IntVar()
c6 = tk.Checkbutton(window, text='Campinas',variable=var6, onvalue=1, offvalue=0, anchor='w', width=10)
c6.pack()
var7 = tk.IntVar()
c7 = tk.Checkbutton(window, text='Brasília',variable=var7, onvalue=1, offvalue=0, anchor='w', width=10)
c7.pack()
var8 = tk.IntVar()
c8 = tk.Checkbutton(window, text='Alphaville',variable=var8, onvalue=1, offvalue=0, anchor='w', width=10)
c8.pack()

B = tk.Button(window, text ="Confirmar", command=confirmar)
B.place(x=210,y=280)

window.protocol("WM_DELETE_WINDOW", confirmar)


window.mainloop()