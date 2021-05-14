conjunto = {1, 2, 3, 4, 5}
conjunto2 = {5, 6, 7, 8}
conjunto_uniao = conjunto.union(conjunto2)
print('Uniao:{}'.format(conjunto_uniao))
conjunto_interseccao = conjunto.intersection(conjunto2)
print('interseccao: {}'.format(conjunto_interseccao))
conjunto_diferenca1 = conjunto.difference(conjunto2)
conjunto_diferenca2 = conjunto2.difference(conjunto)
print('diferenca entre 1 e 2: {}'.format(conjunto_diferenca1))
print('diferenca entre 2 e 1: {}'.format(conjunto_diferenca2))
conjunto_diff_simetrica = conjunto.symmetric_difference(conjunto2)
print('diferenca simetrica: {}'.format(conjunto_diff_simetrica))
conjunto_a = {1, 2, 3}
conjunto_b = {1, 2, 3, 4, 5}
conjunto_subset = conjunto_a.issubset(conjunto_b)
print('a conjunto_subset de b:{}'.format(conjunto_subset))
conjunto_superset = conjunto_b.issuperset(conjunto_a)
print('b e um superconjunto de a: {}'.format(conjunto_superset))
