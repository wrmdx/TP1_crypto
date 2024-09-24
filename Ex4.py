import random

def Tab():
    numbers = list(range(100))  
    random.shuffle(numbers)      
    return numbers

def homophonic_encrypt(plaintext, substitution_table):
    encrypted_text = []
    substitution_dict = {
        'A': [0, 1, 2],
        'B': [3, 4, 5],
        'C': [6, 7, 8],
        'D': [9, 10, 11, 12],
        'E': [13, 14, 15],
        'F': [16, 17, 18],
        'G': [19, 20, 21],
        'H': [22, 23, 24],
        'I': [25, 26, 27],
        'J': [28],
        'K': [29],
        'L': [30, 31],
        'M': [32, 33],
        'N': [34],
        'O': [35, 36],
        'P': [37, 38, 39],
        'Q': [40],
        'R': [41, 42],
        'S': [43, 44],
        'T': [45, 46],
        'U': [47, 48],
        'V': [49],
        'W': [50],
        'X': [51],
        'Y': [52],
        'Z': [53]
    }

    used_indices = {letter: [] for letter in substitution_dict.keys()}

    for char in plaintext:
        if char.upper() in substitution_dict:
            choices = substitution_dict[char.upper()]
            available_choices = [num for num in choices if num not in used_indices[char.upper()]]
            
            if available_choices:
                chosen = random.choice(available_choices)
                encrypted_text.append(str(chosen).zfill(2)) 
                used_indices[char.upper()].append(chosen)  
            else:
                encrypted_text.append(char)  
        else:
            encrypted_text.append(char)  

    return ''.join(encrypted_text)


def main() : 
    print(Tab())
main()