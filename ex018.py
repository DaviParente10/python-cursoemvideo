import math
angulo = float(input("Qual o ângulo que você deseja?"))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print(f"Seno {seno:.2f}, cosseno {cosseno:.2f}, tangente {tangente:.2f}")