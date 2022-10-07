while True:
    ip_address = input('Введите IP: ').split('.')
    if len(ip_address) != 4:
        print('Адрес — это четыре положительных числа, разделённые точками.')
        continue
    element_not_digit = [element for element in ip_address if not element.isdigit()]
    if len(element_not_digit):
        print(','.join(element_not_digit), '— это не целое(ые) число(а).')
        continue
    element_out_limit = [element for element in ip_address if int(element) > 255]
    if len(element_out_limit):
        print(','.join(element_out_limit), 'превышает(ют) 255')
    else:
        print('IP-адрес корректен.')
        break
