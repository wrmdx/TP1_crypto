import random
def Tab():
    original = list(range(ord('A'), ord('Z')+1))
    shuffled = original.copy()  
    random.shuffle(shuffled)
    letter_mapping = {chr(orig): chr(shuf) for orig, shuf in zip(original, shuffled)}
    return letter_mapping



def load_file(file_path) : 
    with open(file_path , 'r') as file :
        return file.read()

def crypt_file(file_path) : 
    content = load_file(file_path)
    x = Tab()
    encrypted_content = ''
    for ch in content : 
        ch_upper = ch.upper()
        encrypted_content += x.get(ch_upper, ch)
    return encrypted_content

def save_file(content , file_path) : 
    with open(file_path , 'w+') as file : 
        file.write(content)

def letter_frequence(content):
    letter_count = {}
    total_letters = 0
    
    for ch in content:
        ch = ch.upper()
        if 'A' <= ch <= 'Z':  
            letter_count[ch] = letter_count.get(ch, 0) + 1
            total_letters += 1
    
    letter_frequency = {ch: count / total_letters for ch, count in letter_count.items()}
    
    return letter_frequency

def cryptanalyse_substitution(encrypted_text, language='english'):
    french_frequencies = {
        'E': 14.69, 'S': 6.33, 'A': 7.54, 'I': 7.18, 'N': 6.89, 'T': 6.88,
        'O': 7.51, 'R': 6.49, 'U': 6.12, 'L': 5.63, 'D': 3.66
    }
    english_frequencies = {
        'E': 12.70, 'T': 9.06, 'A': 8.17, 'O': 7.51, 'I': 6.97, 'N': 6.75,
        'S': 6.33, 'H': 6.09, 'R': 5.99, 'D': 4.25, 'L': 4.03, 'C': 2.78,
        'U': 2.76, 'M': 2.41, 'W': 2.36, 'F': 2.23, 'G': 2.02, 'Y': 1.97,
        'P': 1.93, 'B': 1.49, 'V': 0.98, 'K': 0.77, 'X': 0.15, 'J': 0.15,
        'Q': 0.10, 'Z': 0.07
    }

    frequencies = french_frequencies if language == 'french' else english_frequencies

    encrypted_frequencies = letter_frequence(encrypted_text)

    sorted_encrypted = sorted(encrypted_frequencies, key=encrypted_frequencies.get, reverse=True)
    sorted_lang = sorted(frequencies, key=frequencies.get, reverse=True)

    min_length = min(len(sorted_encrypted), len(sorted_lang))
    decryption_table = {sorted_encrypted[i]: sorted_lang[i] for i in range(min_length)}

    decrypted_text = ''
    for char in encrypted_text:
        if char in decryption_table:
            decrypted_text += decryption_table[char]
        else:
            decrypted_text += char

    return decrypted_text

def main() : 
    encrypted_text = crypt_file('./fr_text.txt')
    decrypted_text = cryptanalyse_substitution(encrypted_text, 'french')
    print("Texte décrypté approximatif:", decrypted_text)

main()