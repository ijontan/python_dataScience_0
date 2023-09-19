def all_thing_is_obj(object: any) -> int:
    objectType = type(object)
    name = objectType.__name__
    if name == "list" or name == "tuple" or name == "set" or name == "dict":
        print(f"{name.capitalize()} : {objectType}")
    elif name == "str":
        print(f"{object} is in the kitchen : {objectType}")
    else:
        print("Type not found")
    return 42
