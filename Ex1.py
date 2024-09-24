##Exercice 1 

def cesar_crypt(text, shift):
    result = []

    for ch in text:
        if 'A' <= ch <= 'Z':  
            shifted = chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))
            result.append(shifted)
        elif 'a' <= ch <= 'z':  
            shifted = chr((ord(ch) - ord('a') + shift) % 26 + ord('a'))
            result.append(shifted)
        else:
            result.append(ch)  

    return ''.join(result)


def cesar_decrypt(ch, k):
    return cesar_crypt(ch, -k)


def main():
    ch = input("Entrez une chaine de caractères à chiffrer: ")
    k = int(input("Entrez le nombre de décalage (entre 1 et 25): "))
    
    chaine_cryptee = cesar_crypt(ch, k)
    print(f"Chaine cryptée avec décalage {k}: {chaine_cryptee}")
    
    chaine_decryptee = cesar_decrypt(chaine_cryptee, k)
    print(f"Chaine décryptée avec décalage {k}: {chaine_decryptee}")
    
main()



