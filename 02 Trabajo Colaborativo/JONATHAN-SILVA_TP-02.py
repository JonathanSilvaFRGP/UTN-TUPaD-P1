def pedir_bit(mensaje):
    while True:
        try:
            bit = int(input(mensaje))
            if bit in (0, 1):
                return bit
            else:
                print("Por favor, ingresa solo 0 o 1.")
        except ValueError:
            print("Entrada inválida. Usa solo 0 o 1.")

#Solicitar entradas al usuario
print("Simulación de puertas lógicas")
a = pedir_bit("Ingresa el primer valor (0 o 1): ")
b = pedir_bit("Ingresa el segundo valor (0 o 1): ")

#Operaciones
and_result = a & b
or_result = a | b
not_a = 1 - a
not_b = 1 - b
nand_result = 1 - (a & b)
nor_result = 1 - (a | b)
xor_result = a ^ b

#Mostrar resultados
print("\nResultados de operaciones lógicas:")
print(f"{a} AND {b}  = {and_result}")
print(f"{a} OR {b}   = {or_result}")
print(f"NOT {a}     = {not_a}")
print(f"NOT {b}     = {not_b}")
print(f"{a} NAND {b} = {nand_result}")
print(f"{a} NOR {b}  = {nor_result}")
print(f"{a} XOR {b}  = {xor_result}")