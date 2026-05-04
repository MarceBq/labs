def calcular_score(compras, activo, tiene_deuda):
    if not activo:
        return 0
    score = compras * 10
    
    if tiene_deuda:
        score = score / 2
        
    return min(score, 100)

# Uso real
print(calcular_score(5, True, False))  # Output: 50
print(calcular_score(5, True, True))   # Output: 25
print(calcular_score(5, False, False))  # Output: 0

