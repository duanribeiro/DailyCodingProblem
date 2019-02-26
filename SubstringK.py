# This problem was asked by Amazon.

# Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.
# For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".

from itertools import combinations
unique_letters,result = [], []
position_start = 0

# Input do usuário
string_input = input('DIGITE SUA PALAVRA: ')
k_input = int(input('DIGITE VALOR K: '))

# Contando a quantidade de letras diferentes.
for letter in string_input:
    if letter not in unique_letters:
        unique_letters.append(letter)
total_combinations = combinations(unique_letters, k_input)

# Para cada combinação, verifiar a maior 'substring'
for combination in total_combinations:
    print(f'LETRAS ESCOLHIDAS: {combination}')
    string = string_input

    for position_end, letter in enumerate(string):
        if letter not in combination:
            result.append(string[position_start:position_end])
            position_start = position_end + 1
            if result[-1] != '':
                print(result[-1])
                
# Checar a maior substring
if result == []:
    resultado = string
else:
    resultado = max(result, key=len)

# Mostrar resultado
print(f'MAIOR STRING: {resultado}')
