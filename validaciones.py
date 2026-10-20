def tipo_valido(tipo):
	return tipo.strip().lower() in ("moto", "carro")


def buscar(lista, campo, valor):
	for elemento in lista:
		if elemento.get(campo) == valor:
			return elemento
	return None
