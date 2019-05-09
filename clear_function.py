def clear_grid(window):
    """Очищает окно от grid"""
    list = window.grid_slaves()
    for l in list:
        l.destroy()


def clear_place(window):
    """Очищает окно от place"""
    list = window.place_slaves()
    for l in list:
        l.destroy()
