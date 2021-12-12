alfavit = 'АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯАБВ ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ 123456789123'
shifr = int(input())
while True:
    message = str(input("Повідомлення для дешифровки: ")).upper()
    nothing = ''
    long = 'UA'
    if long == 'UA':
            for i in message:
                mr = alfavit. find(i)
                new_mr = mr + shifr
                if i in alfavit:
                    nothing += alfavit[new_mr]
                else:
                    nothing += i
    print(nothing)