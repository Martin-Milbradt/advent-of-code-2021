import modules

modules.init()


def test_get_int() -> None:
    # data = modules.get_data_string("1") # error
    data = modules.get_data("1", int)
    print(sum(data[0:5]))


def test_index_string() -> None:
    a = ["python"]
    s1 = a[0]
    print(s1[1])
    s2 = "python"
    print(s2[1])


test_index_string()
