while True:
    x = int(input('Digite um numero para descobrir sua tabuada: '))
    if x < 0:
        break
    for c in range(1, 11):
        print(f'{x} x {c} = {x*c}')
print('ATE MAIS')
