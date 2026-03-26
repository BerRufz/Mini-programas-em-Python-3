def teste(b):
    global a #"a" passará a valer 1 dentro e fora!
    a = 1
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')

def teste1(b):
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')

a = 5
teste1(a)
teste(a)
print(f'A fora vale {a}')
