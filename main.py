'''arquivo = open("texto.txt","r")
print(arquivo.read())
print(arquivo.tell())
print(arquivo.seek(0))
print(arquivo.read())
arquivo.close()'''

'''arquivo = open("novo.txt","w")
arquivo.write("Arquivo de escrita")
arquivo.close()
print(arquivo.closed)'''

'''arquivo = open("frutas.txt","w")
arquivo.write("banana"+ "\mamão")
arquivo.close()'''

'''precos = [20,100,500,600]
with open("precos_roupas.txt","w") as arquivo:
 for preco in precos:
     arquivo.write(str(preco) + '\n')
print(arquivo.closed)'''

precos = [8000]
with open("precos_roupas.txt","a") as arquivo:
    for preco in precos:
        arquivo.write(str(preco) + '\n')