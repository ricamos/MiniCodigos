import random

def cara_coroa(n_test=100):
	"""
	Teste da moeda que tende a ficar 50/50 quanto maior o número de testes.
	Cria uma lista de numeros aleatoriamente. Os números possiveis são 1 ou 2 que representam cara e coroa respectivamente.
	Por padrão serão feitos "100 testes de arremesso da moeda". Mas é possivel um input de n_test.
	Seŕa mostrado os números finais do teste. Qual a porcentagem de cara e de coroa.

	Input: 
		n_test = Número de vezes que a moeda será "jogada para cima"

	Output:
		cara = Quantas vezes deu cara?
		coroa = Quantas vezes deu coroa?
		p_cara = Porcentagem de resultados de cara no teste
		p_coroa = Porcentagem de resultados de coroa no teste
	"""

	result = []
	num = 0
	X = 0

	while X < n_test:
		X += 1
		num = random.randrange(1,3)
		result.append(num)

	total = len(result)
	cara = result.count(1)
	coroa = result.count(2)

	p_cara = (cara / total) * 100
	p_coroa = (coroa / total) * 100

	print(f"Número de teste: {total}, Número de cara: {cara}, Número de coroa: {coroa}. Porcentagem de Coroa {p_coroa:.2f}, Porcentagem de Cara {p_cara:.2f}")

	return cara, coroa, p_cara, p_coroa


cara_coroa(100000000)