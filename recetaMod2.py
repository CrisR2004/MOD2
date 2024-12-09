from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configuración de la base de datos
DATABASE_URI = 'mariadb+mariadbconnector://usuario:password@localhost/recetario'
engine = create_engine(DATABASE_URI, echo=True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

# Modelo de la tabla recetas
class Receta(Base):
    __tablename__ = 'recetas'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    ingredientes = Column(Text, nullable=False)
    pasos = Column(Text, nullable=False)

# Crear la tabla en la base de datos
Base.metadata.create_all(engine)

# Función para agregar una receta
def agregar_receta():
    nombre = input("Ingrese el nombre de la receta: ")
    ingredientes = input("Ingrese los ingredientes (separados por comas): ")
    pasos = input("Ingrese los pasos: ")
    nueva_receta = Receta(nombre=nombre, ingredientes=ingredientes, pasos=pasos)
    session.add(nueva_receta)
    session.commit()
    print("Receta agregada exitosamente.\n")

# Función para actualizar una receta
def actualizar_receta():
    id_receta = input("Ingrese el ID de la receta a actualizar: ")
    receta = session.query(Receta).get(id_receta)
    if receta:
        receta.nombre = input("Ingrese el nuevo nombre de la receta: ")
        receta.ingredientes = input("Ingrese los nuevos ingredientes (separados por comas): ")
        receta.pasos = input("Ingrese los nuevos pasos: ")
        session.commit()
        print("Receta actualizada exitosamente.\n")
    else:
        print("Receta no encontrada.\n")

# Función para eliminar una receta
def eliminar_receta():
    id_receta = input("Ingrese el ID de la receta a eliminar: ")
    receta = session.query(Receta).get(id_receta)
    if receta:
        session.delete(receta)
        session.commit()
        print("Receta eliminada exitosamente.\n")
    else:
        print("Receta no encontrada.\n")

# Función para ver todas las recetas
def ver_recetas():
    recetas = session.query(Receta).all()
    print("\nListado de recetas:")
    for receta in recetas:
        print(f"{receta.id} - {receta.nombre}")
    print()

# Función para buscar los ingredientes y pasos de una receta
def buscar_receta():
    id_receta = input("Ingrese el ID de la receta que desea buscar: ")
    receta = session.query(Receta).get(id_receta)
    if receta:
        print(f"\nReceta: {receta.nombre}\nIngredientes: {receta.ingredientes}\nPasos: {receta.pasos}\n")
    else:
        print("Receta no encontrada.\n")

# Función para mostrar el menú
def mostrar_menu():
    print("Seleccione una opción:")
    print("a) Agregar nueva receta")
    print("b) Actualizar receta existente")
    print("c) Eliminar receta existente")
    print("d) Ver listado de recetas")
    print("e) Buscar ingredientes y pasos de receta")
    print("f) Salir")

# Función principal para ejecutar el programa
def main():
    while True:
        mostrar_menu()
        opcion = input("Opción: ").lower()

        if opcion == 'a':
            agregar_receta()
        elif opcion == 'b':
            actualizar_receta()
        elif opcion == 'c':
            eliminar_receta()
        elif opcion == 'd':
            ver_recetas()
        elif opcion == 'e':
            buscar_receta()
        elif opcion == 'f':
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Intente de nuevo.\n")

    # Cerrar la sesión al salir
    session.close()

# Ejecutar el programa
main()
