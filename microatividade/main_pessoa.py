from Pessoa import Pessoa

pessoa1 = Pessoa("João", "2000-01=01", "000.111.222-33", "15975388-1", False)

pessoa1.nome = "Ana"
pessoa1.dataNascimento = "2001-02-02"
pessoa1.cpf = "123.456.789-12"
pessoa1.rg = "12345678-2"
pessoa1.status = True


attrs = vars(pessoa1)
print('Instancia da classe Pessoa: ')
print(', '.join("%s: %s" % item for item in attrs.items()))