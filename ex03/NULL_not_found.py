import math 

def NULL_not_found(object: any) -> int:
    if isinstance(object, float) and math.isnan(object):
        print(f"Cheese: nan {type(object)}")
        return 0
    elif object is None :
        print(f"Nothing: {object} {type(object)}")
        return 0
    elif object == 0:
        print(f"Zero: {object} {type(object)}")
        return 0
    elif object == '':
        print(f"Empty: {object} {type(object)}")
        return 0
    elif object == False:
        print(f"Fake: {object} {type(object)}")
        return 0
    print("Type not found")
    return 1