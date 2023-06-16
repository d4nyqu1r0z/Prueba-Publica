def registrar(rut,nombre,edad,pais,ciudad):
  return(rut,nombre,edad,pais,ciudad)

def mostrar_menu():
    print("--- Menú ---")
    print("1. Registrar Persona")
    print("2. Buscar Persona")
    print("3. Imprimir Certificados")
    print("4. Eliminar")
    print("5. Salir")

info_persona = []

while True:
  mostrar_menu()
  opcion = int(input("Ingrese una opción: "))

  match opcion:
    case 1:
      print("1. Registrar Persona")
      registrar()
      info_persona.append()
    case 2:
      print("2. Buscar Persona")

    case 3:
      print("3. Imprimir Certificados")

    case 4:
      print("4. Eliminar")
      info_persona = []
      continue
    case 5:
      print("5. Salir")
      break
#hola
