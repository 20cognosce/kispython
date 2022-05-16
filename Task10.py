def main(table):
    result = []

    for row in table:
        temp = []
        index1 = row[0].find(']')
        index2 = row[0].find(';')
        if row[0][index2 + 1:] == "Да":
            temp.append('1')
        else:
            temp.append('0')
        mail = row[0][index1 + 1: index2]
        temp.append(mail)

        step1 = row[1][row[1].find('-') + 1:]
        step2 = step1[:len(step1) - 2] + '-' + step1[len(step1) - 2:]
        temp.append(step2)

        result.append(temp)

    return result


data = [['miroslav97[at]yandex.ru;Да', '451-619-3420'],
         ['meban79[at]mail.ru;Нет', '541-594-5485'],
         ['nozberg42[at]mail.ru;Да', '059-709-8561'],
         ['lukin37[at]yahoo.com;Нет', '862-084-6730']]
print(main(data))

