class ADN:
    def __init__(self,id,nombre,secuencia:str,riesgo:int):
        self.id = id
        self.nombre = nombre
        self.secuencia: str = secuencia
        self.riesgo: int = riesgo
    
    def __repr__(self):
        return(f"ID: {self.id}, Nombre: {self.nombre}, Secuencia: {self.secuencia}, Riesgo: {self.riesgo}")

class secuencias:
    def __init__(self):
            self.secuencias = []

    def registrar(self, ADN, i=0):
        if i == len(self.secuencias):
            self.secuencias.append(ADN)
            return "secuencia agregada correctamente"

        if self.secuencias[i].id == ADN.id:
            return "Secuencia ya existe"

        return self.registrar(ADN, i + 1)

    def contar_patron(self, secuencia, patron, i=0):
        if patron == "":
            return 0

        if i + len(patron) > len(secuencia):
            return 0

        actual = secuencia[i:i + len(patron)]

        if actual == patron:
            return 1 + self.contar_patron(secuencia, patron, i + 1)
        
        return self.contar_patron(secuencia, patron, i + 1)

    
    def contar_en_todas(self, patron, i=0):
        if i == len(self.secuencias):
            return []

        muestra = self.secuencias[i]

        cantidad = self.contar_patron(muestra.secuencia, patron)

        resultado_actual = [
            (muestra.id, muestra.nombre, "RESULTADO:",cantidad)
        ]

        return resultado_actual + self.contar_en_todas(patron, i + 1)

    
    def promedio_riesgo(self, i=0, suma=0, cantidad=0):
        if i == len(self.secuencias):
            if cantidad == 0:
                return None
            return suma / cantidad

        return self.promedio_riesgo(i + 1,suma + self.secuencias[i].riesgo,cantidad + 1)

    def generar_subcadenas(self, secuencia, n, i=0):
        if n <= 0 or i + n > len(secuencia):
            return []

        actual = secuencia[i:i+n]

        return [actual] + self.generar_subcadenas(secuencia, n, i+1)

    
    def comparar_a_t(self, secuencia, i=0):
        if i == len(secuencia):
            return (0, 0)

        a, t = self.comparar_a_t(secuencia, i + 1)

        if secuencia[i] == "A":
            a += 1
        elif secuencia[i] == "T":
            t += 1

        if i == 0:
            if a > t:
                return "Tiene más A que T"
            elif t > a:
                return "Tiene más T que A"
            return "Tiene igual cantidad de A y T"

        return (a, t)

    def mutar(self, secuencia, i=0):
        if i == len(secuencia):
            return ("", 0)

        resto, cantidad = self.mutar(secuencia, i + 1)

        if secuencia[i] == "A":
            return ("T" + resto, cantidad + 1)

        elif secuencia[i] == "T":
            return ("A" + resto, cantidad + 1)

        return (secuencia[i] + resto, cantidad)

    def buscar_por_criterios(self, riesgo_minimo, longitud_minima, patron, i=0):
        if i == len(self.secuencias):
            return None

        muestra = self.secuencias[i]

        if (muestra.riesgo >= riesgo_minimo
            and len(muestra.secuencia) >= longitud_minima
            and self.contar_patron(muestra.secuencia, patron) > 0):
            return muestra

        return self.buscar_por_criterios(riesgo_minimo, longitud_minima, patron, i + 1)

    def eliminar_bajo_riesgo(self, riesgo_minimo, i=0):
        if i == len(self.secuencias):
            return 0

        if self.secuencias[i].riesgo < riesgo_minimo:
            del self.secuencias[i]
            return 1 + self.eliminar_bajo_riesgo(riesgo_minimo, i)

        return self.eliminar_bajo_riesgo(riesgo_minimo, i + 1)

    def mutar_CAMBIO(self, secuencia, i=0):
        if i == len(secuencia):
            return ("", 0)

        resto, cantidad = self.mutar_CAMBIO(secuencia, i + 1)

        if i % 2 == 0:
            if secuencia[i] == "A":
                return ("T" + resto, cantidad + 1)
            elif secuencia[i] == "T":
                return ("A" + resto, cantidad + 1)

        return (secuencia[i] + resto, cantidad)


    def contar_patron_CAMBIO(self, secuencia, patron, i=0):
        if patron == "":
            return 0

        if i + len(patron) > len(secuencia):
            return 0

        actual = secuencia[i:i + len(patron)]

        if actual.upper() == patron.upper():
            return 1 + self.contar_patron_CAMBIO(secuencia, patron, i + 1)

        return self.contar_patron_CAMBIO(secuencia, patron, i + 1)

    
    def equilibrada(self, secuencia):

        if len(secuencia) <= 1:
            return True

        cantidad_a = secuencia.count("A")
        cantidad_t = secuencia.count("T")

        diferencia = abs(cantidad_a - cantidad_t)

        if diferencia > 1:
            return False

        mitad = len(secuencia) // 2

        izquierda = secuencia[:mitad]
        derecha = secuencia[mitad:]

        resultado_izquierda = self.equilibrada(izquierda)
        resultado_derecha = self.equilibrada(derecha)

        return resultado_izquierda and resultado_derecha


  

sistema = secuencias()


a1 = ADN(1, "Ana", "ATATCGAT", 7)
a2 = ADN(2, "Luis", "TTATATCC", 9)
a3 = ADN(3, "Mia", "CCGGAT", 4)
a4 = ADN(4, "Sol", "ATATATAT", 8)


print("\n REGISTRAR ")
print(sistema.registrar(a1))
print(sistema.registrar(a2))
print(sistema.registrar(a3))
print(sistema.registrar(a4))
print(sistema.registrar(a1))  

    
print("\n CONTAR EN TODAS ")
print("PATRON EN TODAS:", sistema.contar_en_todas("ATA"))


print("\n PROMEDIO ")
print("PROMEDIO:", sistema.promedio_riesgo())  


print("\n SUBCADENAS ")
print("SUBCADENAS:", sistema.generar_subcadenas("ATCG", 2))


print("\n COMPARAR A Y T ")
print("COMPARACIÓN A Y T:", sistema.comparar_a_t("AATTG"))

print("\n MUTAR ")
print("MUTADAS:", sistema.mutar("ATCG"))

print("\nBUSCAR por criterios")
print(sistema.buscar_por_criterios(7, 8, "AT"))

print("\n ELIMINAR bajo riesgo")
print("Eliminadas:", sistema.eliminar_bajo_riesgo(6))
print("Muestras restantes:", sistema.secuencias)

print("\n mutar_CAMBIO")
print("MUTADAS:", sistema.mutar_CAMBIO("ATCGTA"))


print("\n contar_patron_CAMBIO")
print("PATRON:", sistema.contar_patron_CAMBIO("aTATat", "AT"))

print("\n SECUENCIAS EQUILIBRADAS")
print("ATAT:", sistema.equilibrada("ATAT"))    
print("AATT:", sistema.equilibrada("AATT"))   
print("A:", sistema.equilibrada("A"))          
print("ATATA:", sistema.equilibrada("ATATA"))  