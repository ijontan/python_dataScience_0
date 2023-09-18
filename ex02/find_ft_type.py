def all_thing_is_obj(object: any) -> int:
    objectType = type(object)
    name = objectType.__name__
    if name == "int":
        print("Type not found")
    elif name == "str":
        print(f"{object} is in the kitchen : {objectType}")
    else:
        print(f"{name.capitalize()} : {objectType}")
    return 42