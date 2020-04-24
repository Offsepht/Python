vowels =['a', 'e', 'i', 'o', 'u']
word = input("Provide a word:")
found = {
    'a' = 0,
    'e' = 0,
    'i' = 0,
    'o' = 0,
    'u' = 0
}
for  letter in word:
    if letter in vowels:
        if letter not in found:
            found.append(letter)
for k, v in sorted(found.items()):
    print(k, 'was found', v, 'time(s).')

