

def somar(parcela_1, parcela_2) -> float:
    return parcela_1 + parcela_2


def subtrair(aditivo_1, subtrativo_2) -> float:
    return aditivo_1 - subtrativo_2


def multiplicar(fator_1, fator_2) -> float:
    return fator_1 * fator_2


def dividir(dividendo, divisor, option:bool=True) -> float:
    if divisor == 0:
        return "Entrada inválida"
    if option:
        return dividendo / divisor
    quociente_inteiro = dividendo // divisor
    resto = dividendo % divisor
    return [quociente_inteiro, resto]


def potenciar(num, expoente) -> float:
    return num ** expoente


def raiz_quadrada(radicando):
    return radicando ** .5


def fatorial(num:int) -> int:
    if num < 0:
        return "Entrada inválida"
    if num <= 1:
        return 1
    contagem = 2
    soma = num
    while contagem != num:
        soma *= contagem
        contagem += 1
    return soma


