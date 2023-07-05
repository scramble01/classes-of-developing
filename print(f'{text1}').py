text1 = '1_Remember the weight'

print('=' * (len(text1) + 4))
print('=', text1, '=')
print('=' * (len(text1) + 4))

text2 = '2_Show History'

print('=' * (len(text2) + 4))
print('=', text2, '=')
print('=' * (len(text2) + 4))

answer = int(input('Enter the number of the function you selected: '))
    
if answer == '1' :
    user_weight_date = input('Write down your weight and todays date: ')
    with open('weight_date.txt', 'w') as f:
        f.write([user_weight_date])
elif answer == '2' :
    with open('weight_date.txt', 'r') as f:
        data = f.read()
        print(data)
else:
    print('there is no such function')


