from equacoes import *

def analfabeto(numero): # O rodrigo é uma pessoa especial.
    match numero:
        case 2: return 'A'
        case 3: return 'B'
        case 4: return 'C'
        case 5: return 'D'
        case 6: return 'E'
        case 7: return 'F'
        case 8: return 'G'
        case 9: return 'H'
        case 10: return 'I'
        case 11: return 'J'
        case 12: return 'K'
        case 13: return 'L'
        case 14: return 'M'
        case 15: return 'N'
        case 16: return 'O'
        case 17: return 'P'
        case 18: return 'Q'
        case 19: return 'R'
        case 20: return 'S'
        case 21: return 'T'
        case 22: return 'U'
        case 23: return 'V'
        case 24: return 'W'
        case 25: return 'X'
        case 26: return 'Y'
        case 27: return 'Z'
        case 28: return ' '

def alfabeto(letra):
    match letra:
        case 'a' | 'A': return 2
        case 'b' | 'B': return 3
        case 'c' | 'C': return 4
        case 'd' | 'D': return 5
        case 'e' | 'E': return 6
        case 'f' | 'F': return 7
        case 'g' | 'G': return 8
        case 'h' | 'H': return 9
        case 'i' | 'I': return 10
        case 'j' | 'J': return 11
        case 'k' | 'K': return 12
        case 'l' | 'L': return 13
        case 'm' | 'M': return 14
        case 'n' | 'N': return 15
        case 'o' | 'O': return 16
        case 'p' | 'P': return 17
        case 'q' | 'Q': return 18
        case 'r' | 'R': return 19
        case 's' | 'S': return 20
        case 't' | 'T': return 21
        case 'u' | 'U': return 22
        case 'v' | 'V': return 23
        case 'w' | 'W': return 24
        case 'x' | 'X': return 25
        case 'y' | 'Y': return 26
        case 'z' | 'Z': return 27
        case ' ': return 28

def validar_numeros(p, q, e):
    if not eh_primo(p): 
        print(f"o número {p} em p não é primo.")
        return
    if not eh_primo(q): 
        print(f"o número {q} em q não é primo.")
        return
    
    n = p * q
    euler = euler_n(p, q)
    if not eh_coprimo(euler, e): 
        print(f"o número do expoente que é {e} é coprimo de euler de n:{euler}.")
        return
    
    d = inverso_modular(e, euler)
    print(f"Parâmetros válidos. n: {n}, euler: {euler}, d: {d}, e: {e}")
    return [(n, d), (n, e)]

def criptografar(mensagem, chave):
    codigo = []
    for letra in mensagem:
        m = alfabeto(letra)
        c = exponenciacao_por_quadrados(m ,chave[1], chave[0])
        codigo.append(c)
    return codigo
    
def descriptografar(codigo, chave):
    mensagem = ''
    for c in codigo:
        m = exponenciacao_por_quadrados(c, chave[1], chave[0])
        mensagem += analfabeto(m)
    return mensagem

sistema = input("Escolher as chaves manualmente (M) ou automaticamente (A)? ")
if sistema.upper() == 'M':
    p = int(input("Digite um número primo p: "))
    q = int(input("Digite um número primo q: "))
    e = int(input("Digite o expoente e (coprimo de φ(n)): "))
else:
    p = 13
    q = 11
    e = 73

print("-------------------------------------------------------")
print(f"p: {p}, q: {q}, e: {e}")
chaves = validar_numeros(p, q, e)
if chaves == None:
    print("Chaves inválidas.")
    quit()
print(f"chaves privadas: {chaves[0]} e públicas: {chaves[1]}")
print("-------------------------------------------------------")

texto = input("Digite a mensagem a ser criptografada: ")
print("-------------------------------------------------------")

codigo = criptografar(texto, chaves[1])
print("Mensagem criptografada:", codigo)
print("-------------------------------------------------------")

mensagem = descriptografar(codigo, chaves[0])
print("mensagem descriptografada:", mensagem)    
#print(eh_primo(chaves[1][0]))