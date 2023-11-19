#Дромашко Константин Сергеевич 10-я когорта - Финальный проект


import sender_stand_request

def test_asser():
    make_order = sender_stand_request.create_order()
    find_order = sender_stand_request.get_order(make_order)
    assert find_order == 200



