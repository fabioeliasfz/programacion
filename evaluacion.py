class Alumno:
    def __init__(self, id_alumno, nombre):
        self.id_alumno = id_alumno
        self.nombre = nombre
        self.cursos = {}

    def asignar_calificacion(self, curso, calificacion):
        self.cursos[curso] = calificacion

    def mostrar_calificaciones(self):
        for curso, calificacion in self.cursos.items():
            print(f"Curso: {curso}, Calificación: {calificacion}")


class Profesor:
    def __init__(self, id_profesor, nombre):
        self.id_profesor = id_profesor
        self.nombre = nombre
        self.cursos = []

    def asignar_curso(self, curso):
        self.cursos.append(curso)

    def mostrar_cursos(self):
        print(f"Cursos asignados a {self.nombre}:")
        for curso in self.cursos:
            print(f"- {curso}")


class Curso:
    def __init__(self, id_curso, nombre, profesor=None):
        self.id_curso = id_curso
        self.nombre = nombre
        self.profesor = profesor
        self.alumnos = []

    def inscribir_alumno(self, alumno):
        self.alumnos.append(alumno)

    def mostrar_alumnos(self):
        print(f"Alumnos inscritos en {self.nombre}:")
        for alumno in self.alumnos:
            print(f"- {alumno.nombre}")


class SistemaGestionEscolar:
    def __init__(self):
        self.alumnos = {}
        self.profesores = {}
        self.cursos = {}

    # CRUD de Alumnos
    def agregar_alumno(self, id_alumno, nombre):
        self.alumnos[id_alumno] = Alumno(id_alumno, nombre)

    def mostrar_alumno(self, id_alumno):
        alumno = self.alumnos.get(id_alumno)
        if alumno:
            print(f"ID: {alumno.id_alumno}, Nombre: {alumno.nombre}")
            alumno.mostrar_calificaciones()
        else:
            print("Alumno no encontrado.")

    def actualizar_alumno(self, id_alumno, nuevo_nombre):
        if id_alumno in self.alumnos:
            self.alumnos[id_alumno].nombre = nuevo_nombre
            print("Alumno actualizado correctamente.")
        else:
            print("Alumno no encontrado.")

    def eliminar_alumno(self, id_alumno):
        if id_alumno in self.alumnos:
            del self.alumnos[id_alumno]
            print("Alumno eliminado correctamente.")
        else:
            print("Alumno no encontrado.")

    # CRUD de Profesores
    def agregar_profesor(self, id_profesor, nombre):
        self.profesores[id_profesor] = Profesor(id_profesor, nombre)

    def mostrar_profesor(self, id_profesor):
        profesor = self.profesores.get(id_profesor)
        if profesor:
            print(f"ID: {profesor.id_profesor}, Nombre: {profesor.nombre}")
            profesor.mostrar_cursos()
        else:
            print("Profesor no encontrado.")

    def actualizar_profesor(self, id_profesor, nuevo_nombre):
        if id_profesor in self.profesores:
            self.profesores[id_profesor].nombre = nuevo_nombre
            print("Profesor actualizado correctamente.")
        else:
            print("Profesor no encontrado.")

    def eliminar_profesor(self, id_profesor):
        if id_profesor in self.profesores:
            del self.profesores[id_profesor]
            print("Profesor eliminado correctamente.")
        else:
            print("Profesor no encontrado.")

    # CRUD de Cursos
    def agregar_curso(self, id_curso, nombre, id_profesor=None):
        profesor = self.profesores.get(id_profesor) if id_profesor else None
        curso = Curso(id_curso, nombre, profesor)
        if profesor:
            profesor.asignar_curso(nombre)
        self.cursos[id_curso] = curso

    def mostrar_curso(self, id_curso):
        curso = self.cursos.get(id_curso)
        if curso:
            print(f"ID: {curso.id_curso}, Nombre: {curso.nombre}")
            curso.mostrar_alumnos()
        else:
            print("Curso no encontrado.")

    def actualizar_curso(self, id_curso, nuevo_nombre):
        if id_curso in self.cursos:
            self.cursos[id_curso].nombre = nuevo_nombre
            print("Curso actualizado correctamente.")
        else:
            print("Curso no encontrado.")

    def eliminar_curso(self, id_curso):
        if id_curso in self.cursos:
            del self.cursos[id_curso]
            print("Curso eliminado correctamente.")
        else:
            print("Curso no encontrado.")


# Ejemplo de uso
sistema = SistemaGestionEscolar()

# Agregar datos de ejemplo
sistema.agregar_alumno(1, "Ckeimy Flores")
sistema.agregar_profesor(1, "Fabio Figueroa")
sistema.agregar_curso(1, "Desarrollo Agil", 1)

# Mostrar datos
sistema.mostrar_alumno(1)
sistema.mostrar_profesor(1)
sistema.mostrar_curso(1)
