# 1) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.
# IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;

def pertence_fibonacci(numero):
    if numero < 0:
        return False
    
    a, b = 0, 1
    while a <= numero:
        if a == numero:
            return True
        a, b = b, a + b
    
    return False

try:
    numero = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))
    
    if pertence_fibonacci(numero):
        print(f"O número {numero} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {numero} não pertence à sequência de Fibonacci.")
except ValueError:
    print("Por favor, digite um número inteiro válido.")


# 2) Escreva um programa que verifique, em uma string, a existência da letra ‘a’, seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre.

# IMPORTANTE: Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;

letra = input("Digite a letra que deseja buscar:").lower()
texto = input("Digite o a palavra, frase ou texto que deseja verifivar:").lower()

contador = texto.count(letra)

if(contador > 0):
    print(f"A letra {letra} ocorre {contador} na string")
else:
    print(f"A letra {letra} não existe na string")


# 3) Observe o trecho de código abaixo: int INDICE = 12, SOMA = 0, K = 1; enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; } imprimir(SOMA);

# Ao final do processamento, qual será o valor da variável SOMA?

indice = 12
soma = 0
k = 1

while k < indice:
    k = k + 1
    soma = soma + k

print("O resultado da soma é",soma)

# 4) Descubra a lógica e complete o próximo elemento:
# a) 1, 3, 5, 7, 9
# b) 2, 4, 8, 16, 32, 64, 128
# c) 0, 1, 4, 9, 16, 25, 36, 48
# d) 4, 16, 36, 64, 100
# e) 1, 1, 2, 3, 5, 8, 13
# f) 2,10, 12, 16, 17, 18, 19, 200

# 5. Você está em uma sala com três interruptores, cada um conectado a uma lâmpada em salas diferentes. Você não pode ver as lâmpadas da sala em que está, mas pode ligar e desligar os interruptores quantas vezes quiser. Seu objetivo é descobrir qual interruptor controla qual lâmpada. Como você faria para descobrir, usando apenas duas idas até uma das salas das lâmpadas, qual interruptor controla cada lâmpada?

#OBS: Sabia da resposta porque assisti Alice in Borderland (T01E05)

# Passo 1: Preparação na Sala dos Interruptores
# Ligue o primeiro interruptor e deixe-o ligado por cerca de 5 minutos.
# Após os 5 minutos, desligue o primeiro interruptor.
# Ligue o segundo interruptor e deixe-o ligado.
# O terceiro interruptor permanece desligado o tempo todo.
# Passo 2: Primeira Ida à Sala das Lâmpadas
# Vá até a sala das lâmpadas.

# Observe as lâmpadas:

# Lâmpada acesa: É controlada pelo segundo interruptor (o que está ligado no momento).

# Lâmpadas apagadas: Toque cuidadosamente nas duas lâmpadas que estão apagadas.

# Lâmpada quente: É controlada pelo primeiro interruptor (foi ligado e depois desligado, por isso está quente).
# Lâmpada fria: É controlada pelo terceiro interruptor (nunca foi ligado).
# Anote qual interruptor corresponde a cada lâmpada.

# Passo 3: Retorno à Sala dos Interruptores
# Volte para a sala dos interruptores.
# Passo 4: Segunda Ida à Sala das Lâmpadas (Confirmação)
# Para confirmar suas observações, você pode fazer o seguinte:

# Desligue o segundo interruptor.
# Ligue o terceiro interruptor.
# Vá novamente à sala das lâmpadas.
# Na sala das lâmpadas:

# A lâmpada que agora está acesa será a controlada pelo terceiro interruptor.
# Isso confirma que suas observações anteriores estão corretas.
# Resumo
# Primeiro Interruptor: Lâmpada que estava quente na primeira visita (ligado inicialmente e depois desligado).
# Segundo Interruptor: Lâmpada que estava acesa na primeira visita (ligado durante a primeira ida).
# Terceiro Interruptor: Lâmpada que estava fria e apagada na primeira visita e acesa na segunda (nunca ligada antes da segunda ida).
# Dessa forma, usando apenas duas idas à sala das lâmpadas, você identifica com precisão qual interruptor controla cada lâmpada.