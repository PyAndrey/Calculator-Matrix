def bypass_list(list):
    """Обходит список, преобразует в int, если строка выводит ошибку."""
    list1 = []
    for i in list:
        try:
            list1.append(int(i))
        except ValueError:
            raise ValueError
    return list1