import random

def generate_substitution_table():
    return random.sample(range(100), 100)

def homophonic_encrypt(plaintext):
    encrypted_text = []
    substitution_dict = {
        'A': ['09', '12', '33', '47', '53', '67', '78', '92'],
        'B': ['48'],
        'C': ['13', '41', '62'],
        'D': ['01', '03', '45', '79'],
        'E': ['14', '16', '24', '25', '31', '39', '44', '46', '55', '57', '64', '74', '81', '82', '87', '98'],
        'F': ['10'],
        'G': ['06'],
        'H': ['23'],
        'I': ['32', '50', '70', '73', '83', '88', '93'],
        'J': ['15'],
        'K': ['04'],
        'L': ['26', '37', '51', '84', '88'],
        'M': ['22', '27', '56'],
        'N': ['18', '39', '58', '59', '66', '71', '91'],
        'O': ['00', '05', '54', '72', '90'],
        'P': ['07', '38', '95'],
        'Q': ['94'],
        'R': ['29', '35', '40', '42', '77', '80'],
        'S': ['11', '19', '36', '43', '65', '76', '86', '96'],
        'T': ['17', '20', '30', '49', '69', '75', '97'],
        'U': ['08', '52', '60', '61', '63', '99'],
        'V': ['34'],
        'W': ['89'],
        'X': ['28'],
        'Y': ['02'],
        'Z': ['21']
    }
    
    used_symbols = {letter: [] for letter in substitution_dict.keys()}

    for char in plaintext:
        if char.upper() in substitution_dict:
            choices = substitution_dict[char.upper()]
            available_choices = [symbol for symbol in choices if symbol not in used_symbols[char.upper()]]

            if available_choices:
                chosen = random.choice(available_choices)
                encrypted_text.append(chosen)  
                used_symbols[char.upper()].append(chosen)  
            else:
                encrypted_text.append(char)  
        else:
            encrypted_text.append(char)  

    return ''.join(encrypted_text)

def polybius_square():
    return {
        'A': '11', 'B': '12', 'C': '13', 'D': '14', 'E': '15',
        'F': '21', 'G': '22', 'H': '23', 'I': '24', 'K': '25',
        'L': '31', 'M': '32', 'N': '33', 'O': '34', 'P': '35',
        'Q': '41', 'R': '42', 'S': '43', 'T': '44', 'U': '45',
        'V': '51', 'W': '52', 'X': '53', 'Y': '54', 'Z': '55'
    }

def polybius_encrypt(plaintext):
    square = polybius_square()
    encrypted_text = []
    
    for char in plaintext:
        if char.upper() in square:
            encrypted_text.append(square[char.upper()])
        else:
            encrypted_text.append(char) 
    
    return ''.join(encrypted_text)

def alternative_encrypt(plaintext):
    substitution_table = generate_substitution_table()
    encrypted_text = []

    for char in plaintext:
        if char.isalpha():
            index = ord(char.upper()) - ord('A')
            encrypted_char = substitution_table[index]
            encrypted_text.append(str(encrypted_char).zfill(2))
        else:
            encrypted_text.append(char)  

    return ''.join(encrypted_text)

def main() : 
    plaintext = "EVENEMENT"
    
    substitution_table = generate_substitution_table()
    print("Tableau de substitution:", substitution_table)

    encrypted_text = homophonic_encrypt(plaintext)
    print("Texte chiffré avec chiffre homophone:", encrypted_text)

    polybius_encrypted_text = polybius_encrypt(plaintext)
    print("Texte chiffré avec carré de Polybe:", polybius_encrypted_text)

    alternative_encrypted_text = alternative_encrypt(plaintext)
    print("Texte chiffré avec alternative:", alternative_encrypted_text)
main()