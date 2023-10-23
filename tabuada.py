def criar_tabuada(produto:int, maximo:int):
    for i in range(maximo):
        if i<10:
            print(f"0{i} X {produto} = {(i)*produto}")
        else:
            print(f"{i} X {produto} = {(i)*produto}")

print("Vamos estudar a tabuada de multiplicação?\n")
produto = int(input("Digite qual tabuada você quer estudar: "))
maximo = int(input("Agora digite até qual número multiplicar: "))+1
print("\n")

criar_tabuada(produto, maximo)