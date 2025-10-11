def euler_n(p, q):
    return (p - 1) * (q - 1)

def mdc(p, q):
    self_p = p
    self_q = q

    while self_q != 0:
        resto = self_p % self_q
        self_p = self_q
        self_q = resto 
    return self_p

def eh_primo(x):
    if x < 2:
        return False
    
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
        
    return True

def eh_coprimo(p, q):
    return mdc(p, q) == 1

def combinacao_linear(p, q):
    # Algoritmo de Euclides Estendido
    old_r, r = p, q
    old_s, s = 1, 0
    old_t, t = 0, 1

    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t

    # old_r é o mdc, old_s e old_t são os coeficientes
    return old_s, old_t

def inverso_modular(e, n):
    s, t = combinacao_linear(e, n)
    return s % n

def exponenciacao_por_quadrados(m, e, n):
    exp = 0
    bits = []
    while 2**exp <= e:
        exp += 1
    
    for i in range(exp-1, -1, -1):
        if e >= 2**i:
            bits.append(1)
            e -= 2**i
        else:
            bits.append(0)

    valor = 1
    finais = []
    for i in range(len(bits)-1, -1, -1):
        if i == len(bits) - 1:
            finais.append(m % n)
            if bits[i] == 1: valor = finais[-1]
        else:
            finais.append((finais[-1] ** 2) % n)
            if bits[i] == 1:
                valor *= finais[-1]
        valor %= n
    
    return valor

#print(exponenciacao_por_quadrados(89, 71, 143))
"""x = 120
y = 11
fat = combinacao_linear(x, y)
print('Fatores:', fat, 'soma: ', x*fat[0] + y*fat[1], 'mdc:', mdc(x, y))
print(inverso_modular(y, x))"""