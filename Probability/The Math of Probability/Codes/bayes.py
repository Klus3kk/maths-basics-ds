p_drinking_cola = .19
p_cancer = .020
p_drinking_cola_if_cancer = .80

p_cancer_if_drinking_cola = p_drinking_cola_if_cancer * p_cancer / p_drinking_cola

print(p_cancer_if_drinking_cola)