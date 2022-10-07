def check_error(user_str):
    user_data = user_str.split()
    if len(user_data) != 3:
        raise IndexError
    name, email, age = tuple(user_data)
    if not name.isalpha():
        raise NameError
    if '@' and '.' not in email:
        raise SyntaxError
    if int(age) < 10 or int(age) > 99:
        raise ValueError


with open('registrations.txt', 'r', encoding='utf-8') as data, \
        open('registrations_good.log', 'wb') as good_log, \
        open('registrations_bad.log', 'wb') as bad_log:
    for str_data in data:
        str_data = str_data.rstrip()
        fail = ''
        try:
            check_error(str_data)
        except IndexError:
            error = 'НЕ присутствуют все три поля'
        except NameError:
            error = 'Поле «Имя» содержит НЕ только буквы'
        except SyntaxError:
            error = 'Поле «Имейл» НЕ содержит @ и . (точку)'
        except ValueError:
            error = 'Поле «Возраст» НЕ является числом от 10 до 99'
        if error:
            bad_log.write(('{:<35}'.format(str_data) + '\t' + error + '\n').encode('utf-8'))
        else:
            good_log.write((str_data + '\n').encode('utf-8'))

# Почему так долго закрывается файл с регистрациями?
# Я думаю, что это из-за проверки каждой ошибки, отображающийся в верхнем правом углу.
# На этой странице их 29 (types). А вот в логах их 23000. PyCharm зависает, возможно, обрабатывая все ошибки.
