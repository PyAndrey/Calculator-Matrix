def bypass_list(list_of_str: list) -> list:
    """Обходит список, преобразует в int, если строка выводит ошибку."""
    list_of_int = []
    for i in list_of_str:
        try:
            list_of_int.append(int(i))
        except ValueError:
            raise ValueError
    return list_of_int
