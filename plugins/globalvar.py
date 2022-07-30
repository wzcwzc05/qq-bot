def init()->None:
    global global_var
    global_var = {}
    
def get_value(key:str):
    try:
        return global_var[key]
    except KeyError:
        return None

def set_value(key:str, value):
    global_var[key] = value