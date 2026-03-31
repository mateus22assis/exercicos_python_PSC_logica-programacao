
Lx = float(input("digite o valor de Lx: "))
Ly = float(input("digite o valor de Ly: "))
Lz = float(input("digite o valor de Lz: "))

if (Lx < Ly + Lz) and (Ly < Lx + Lz) and (Lz < Lx + Ly):
    print("Os valores podem formar um triângulo.")
else:
    print("Os valores não podem formar um triângulo.")