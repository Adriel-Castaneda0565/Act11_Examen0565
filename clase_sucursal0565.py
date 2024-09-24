#zona de clases
class sucursal0565:
#zona de atributos
    id=0
    direccion=""
    telefono=0
    email=""
    horario=""
    nombre=""
    CP=0
#zona de funciones
    def mostrar_datos(self):
        print("--Datos--")
        print(f"ID: {p.id}",f"\nDireccion: {p.direccion}",
            f"\nTelefono: {p.telefono}"f"\nEmail: {p.email}"f"\nHorario: {p.horario}"
            f"\nNombre: {p.nombre}"f"\nCodigo Postal: {p.CP}\n")
    def listar_sucursales(self):
        print("\n--Lista de sucursales--")
        sucursales=["las torres","misiones","gran patio","aztecas","plaza juarez"]
        for a in sucursales:
            print(a)
    def tupla_sucursales(self):
        print("\n--tupla de estados con sucursales--")
        estado=("Chihuahua","Nuevo leon","Jalisco","CDMX","Sonora")
        for b in estado:
            print(b)
    def diccionario_empleados_sucursal(self):
        print("\n--diccionario de empleados--")
        c_empleados={"Las Torres:":"10","Misiones:":"20","Gran Patio:":"12","Aztecas:":"5","Plaza Juarez:":"6"}
        for c,d in c_empleados.items():
            print(c,d)
    def alta(self):
        print("\nSucursal en las americas: inaugurda")
    def baja(self):
        print("\nSucursal en Mi Plaza: sin ventas")
#objetos
p=sucursal0565()
#llamada a funciones
p.id=1930
p.direccion="Gallareta1006"
p.telefono=6565308689
p.email="elprieto@gmail.com"
p.horario="10AM/10PM"
p.CP=32582
p.mostrar_datos()
p.listar_sucursales()
p.tupla_sucursales()
p.diccionario_empleados_sucursal()
p.alta()
p.baja()