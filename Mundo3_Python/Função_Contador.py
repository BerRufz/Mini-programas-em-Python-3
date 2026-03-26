def contador(*num):
    tamanho = len(num)
    print(f'Recebi os valores {num} e são ao todo {tamanho} números')


contador(2, 1, 3)
contador(4, 4)
contador(1, 43, 4, 2, 5, 2, 1, 0, 4)