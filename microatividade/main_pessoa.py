from Pessoa import Pessoa

pessoa1 = Pessoa("João", "2000-01=01", "000.111.222-33", "15975388-1", False)
pessoa1.alterarStatus(False)

attrs = vars(pessoa1)
print('Instancia da classe Pessoa: ')
print(', '.join("%s: %s" % item for item in attrs.items()))