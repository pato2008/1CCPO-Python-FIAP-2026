
#fuçao sem retorno e sem parametro
def print_lyrics():
    print("i am iron man")
    print("war pigs")

print_lyrics()

#fuçao sem retorno e com parametro

def bos_vindas(nome):
    print(f' ola {nome} seja bem vindo')


nome_digitado = input("digite seu linodo nome:")
bos_vindas(nome_digitado)

#fuçao com retorno e com parametro


def soma(num_a,num_b):
    soma = num_a + num_b
    return soma
resultado_soma = soma(17 ,2)
print(resultado_soma)


