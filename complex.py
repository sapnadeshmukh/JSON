import json
def is_complex_num(objct):
    if 'img' in objct:
        return complex(objct['real'], objct['img'])
    return objct

complex_object =json.loads('{"complex": true, "real": 4, "img": 5}', object_hook = is_complex_num)
print("Complex_object: ",complex_object)


