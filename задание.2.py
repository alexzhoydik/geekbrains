def personal_info(**args):
    return args

print(personal_info(
    name=input('Имя: '),
    surname=input('Фамилия: '),
    bitrhday=input('День рождения: '),
    city=input('Город: '),
    email=input('E-mail: '),
    phone=input('Телефон: '),
))
