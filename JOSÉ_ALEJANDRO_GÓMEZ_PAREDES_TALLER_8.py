## contar números impares en una lista dada
def Count_imp(Ls_impares):
    try:
        Ls_int=Ls_impares.split(",")
        Ln_counter=0
        Ln_counter_par=0
        for Ln_num in Ls_int:
            if ((int(Ln_num)%2)!=0):
                Ln_counter+=1
            elif((int(Ln_num)%2)==0):
                Ln_counter_par+=1
        print(f"en la lista existen {Ln_counter}  números impares y {Ln_counter_par} números impares")
    except:
        print("solo se admiten números enteros")
#lista=input("escriba una serie de números sepárada por comas  ")
#Count_imp(lista)



## orden inverso
def invert_list(lista):
    try:
        lista=lista.split(",")
        Lst_num=list(lista)
        Lst_num=list(reversed(Lst_num))
        print(f" la  {Lst_num}")
    except:
        print("solo se admiten números")

#lista=input("escriba una serie de números sepárada por comas  ")
#;invert_list(lista)


##ordenar listas
def asc_desc(lista):
    Lst_num =[]
    try:
        lista=lista.split(",")
        for i in lista:
            Lst_num.append(int(i))
        print("desea ordenar la lista de forma ascendente o descendente? A/O")
        opcion=input(">>")
        if((opcion=="A")or(opcion=="a") ):
            Lst_num=sorted(Lst_num)
        elif((opcion=="D") or (opcion=="d")):
            Lst_num=sorted(Lst_num, reverse=True)
        print(f"La lista ordenada es: {Lst_num}")
    except:
        print("ingrese caracteres validos")

#lista=input("escriba una serie de números sepárada por comas  ")
#asc_desc(lista)



## buscar en lista
def list_search(lista):
    lista = lista.split(",")
    elm = input("ingrese el elemento que desea buscar >>")
    if (elm in lista):
        print(f"el elemento buscado está en la posición {lista.index(elm)+1}")
    else:
        print("el elemento buscado no está en la lista")



#lista=input("escriba una serie de números sepárada por comas  ")
#list_search(lista)


