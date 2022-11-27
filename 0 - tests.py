import modules

modules.init()


def test_get_int() -> None:
    # data = modules.get_data_string("1") # error
    data = modules.get_data("1", int)
    print(sum(data[0:5]))
