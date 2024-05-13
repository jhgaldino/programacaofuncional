import functools
#1. Usando encapsulamento e comprehensions, crie uma lista que contenha os números primos no intervalo de 1 a 100.
N = 100
print([p for p in range(1,N) if 0 not in [p%d for d in range(2,p)]])

 



print("----------------------------------------------------")
#2. Usando reduce, retorne o maior elemento de uma lista.
xis = [float(x) for x in input("Entre com uma lista de valores separados por espaço.Aperte enter para finalizar: ").split()] 
print ("O maior elemento da lista é : ",end="")
print (functools.reduce(lambda a,b : a if a > b else b,xis)) 
print("----------------------------------------------------")
#3. Com apenas uma linha de código, crie uma lista que contenha o dobro dos números da lista: [1,5,2,4,1,3].
print ([x*2 for x in [1,5,2,4,1,3]])

#4. Usando as regras abaixo crie uma função recursiva
#para a sequência de Fibonacci.
#a. fibonacci(1)= 1
#b. fibonacci(2)= 1
#c. fibonacci(n+2) = fibonacci(n+1) + fibonacci(n)
def fibonacci(n):
    if n<0:
        print("Sintaxe Incorreta")
    elif n==1 or n==2:
        return 1
    elif n==0:
        return 0
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
termos = int(input("Quantos termos da sequencia de fibbonaci vc quer imprimir? "))
if termos < 0:
    print("Erro de Sintaxe!!!!")
for o in range(termos):
    print (fibonacci(o))

print("----------------------------------------------------")
#   5. Crie uma função lambda que retorne os n primeiros números pares.
termos1 = int(input("Qual o final da lista de numeros pares vc quer imprimir? "))
if termos1 < 0 :
    print("Erro de Sintaxe!!!!")

calcular_pares = lambda limite: [v for v in range(limite + 1) if v %2 == 0]                                    
print(calcular_pares(termos1))

