# contar palabras en un archivo

def count_Line_file(archivo):
    file = open(archivo, "r")
    lineas=file.readlines()
    print(f"la cantidad de lineas en el archivo es: {len(lineas)}")

#count_Line_file("a.txt")

# contar caracteres en un archivo
def count_car_file(archivo):
    file = open(archivo, "r")
    text = file.read()
    file.close
    print(f"la cantidad de caracteres en el archivo es: {len(text)}")

#count_car_file("a.txt")


#contar_ocurrencias("a.txt")

def contar_ocurrencias(archivo):
    counter = 0
    palabra= input("que palabra desea buscar?")
    with open(archivo, "r+") as file:
        texto = file.read()
        counter= texto.count(palabra)
        file.close()
    print(f"la palabra ingresada se repite: {counter} veces")


#sumar_de_archivo("numbers.txt")
def sumar_de_archivo(file):
    separadores=[",",".","\n","\t",":",";","!","?","¿","¡"]
    num_list=[]
    with open(file,"r")as file:
        numeros=file.readlines()
        for i in numeros:
            for sep in separadores:
                i.replace(sep,"")

        for i in numeros:
            num_list.append(int(i))
    file.close()

    suma=sum(num_list)
    print(suma)


# reemplazar
def replace(archivo):
    palabra=input("que palabra quiere reemplazar?")
    replaced=input("que palabra quiere escribir en su lugar?")
    file = open(archivo,"r")
    content=file.read()
    newcont=content.replace(palabra,replaced)
    file=open(archivo,"w")
    file.write(newcont)
    file.close()

#replace("a.txt")

#eliminar lineas vacias
def del_lines(archivo):
    conten=""
    file = open(archivo,"r")
    text = file.readlines()
    for line in text:
        if(line.strip()):
            conten+=line
    file= open(archivo,"w")
    file.write(conten)
    file.close()
#del_lines("a.txt")


def count_dif_words(archivo):
    newtext=[]
    separadores=[",",".","\n","\t",":",";","!","?","¿","¡"]
    file = open(archivo,"r")
    text=file.read()
    for i in text:
        for sep in separadores:
            text.replace(sep,"")
        newtext=text.split()
    conten=set(newtext)
    file.close()
    print(f"la cantidad de palabras diferentes en el texto es: {len(conten)}")
#count_dif_words("a.txt")

# ordenar palabras alfabeticamente
def alphabetic_order(archivo):
    separadores=[",",".","\n","\t",":",";","!","?","¿","¡"]
    file = open(archivo,"r")
    conten=file.read()
    for i in conten:
        for sep in separadores:
            conten.replace(sep,"")
    text=sorted(conten.split())
    print(text)
        


##alphabetic_order("a.txt")
        
# mostrar palabras mayores a el largo indicado
def len_word(archivo):
    counter=0
    ln=int(input("cantidad de caracteres a superar: "))
    file=open(archivo,"r")
    conten=file.read()
    separadores=[",",".","\n","\t",":",";","!","?","¿","¡"]
    for i in conten:
        for sep in separadores:
            conten.replace(sep,"")
    lst=conten.split()
    for i in lst:
        if len(i)>ln:
            counter+=1
    print(f"la cantidad de palabas que superan el número de caracteres ingresados es: {counter}")
len_word("a.txt")

    




