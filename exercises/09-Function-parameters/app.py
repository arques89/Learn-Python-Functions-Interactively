# Your code goes here:
def render_person(nombre , fecha , color , edad , genero):
    param = nombre + " is a " + str(edad) + " years old " + genero + " born in " + str(fecha) + " whith " + color + " eyes"
    return param


# Do not edit below this line
print(render_person('Bob', '05/22/1983', 'green', 23, 'male'))