def juros_simples(valorEmp, taxa, n_periodos):
    return valorEmp * taxa * n_periodos;



#teste
#23000 * 0.03 * 7 = 2560
assert 23.000,00 == juros_simples(23.000,00, 0.03, 7)
