def test_types(var_list: list, var_name_list: list, type_list: list):
    """Checks if all vars are of appropriate type

    Args:
        var_list (list): vars to check
        var_name_list (list): var names as char or string
        type_list (list): desired type of each var

    Raises:
        TypeError: One of the vars has the wrong type
    """
    for var, var_name, typ in zip(var_list, var_name_list, type_list):
        if type(var) != typ:
            raise TypeError(f"Type of {var_name} is {type(var)} instead of {typ}")
