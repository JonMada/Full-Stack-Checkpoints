#Creamos la clase
class Usuario:
    def __init__(self, user_name, contraseña):
        self.user_name = user_name
        self.contraseña = contraseña

#Creamos el objeto
usario1 = Usuario ('Jon', '12345')

#Lo imprimimos
print(usario1.user_name)
print(usario1.contraseña)
