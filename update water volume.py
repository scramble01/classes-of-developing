while True:
    print('now you will find out your daily water allowance')
    weight = int(input('Write down your weight:'))
    volume = weight * 30
    answer = f'you need to drink {volume} Ml of water a day'
    print(answer)
