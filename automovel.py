def custoFinal(custoFab):
    percentualDist = custoFab * 0.28
    custoImpst    = custoFab * 0.45
    return custoFab + percentualDist + custoImpot

#teste

assert 17300 == custoFinal(10000), "'custoFinal' deve ser igual a 17300"
