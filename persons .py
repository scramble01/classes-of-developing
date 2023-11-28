persons = [

    {'name': 'Иван', 'surname': 'Иванов'},

    {'name': 'Василий', 'surname': 'Васьков'},

    {'name': 'Геннадий', 'surname': 'Генов'},
    
]

user_answer = input('Напишите Свое Имя: ')

surnames = []
for person in persons:
    if user_answer == person['name']:
        surnames.append(person['surname'])
        print(user_answer,surnames)
    else:
        print('Этого Имени нету в базе данных')






