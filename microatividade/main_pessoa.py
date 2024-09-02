from Pessoa import Pessoa
from PessoaFisica import PessoaFisica
from PessoaJuridica import PessoaJuridica

pessoa1 = Pessoa("Empresa XYZ", "12345", "2022-01-01", True)
pessoa_fisica = PessoaFisica("Ana", "54321", "2020-06-15", True, "1995-05-15", "123.456.789-10", "98765432-1")
pessoa_juridica = PessoaJuridica("Empresa ABC", "67890", "2023-03-10", True, "2023-01-01", "00.000.000/0001-00")

pessoa_fisica.cpf = "987.654.3-0"
try:
    pessoa_juridica.cpf = "123.345"
except ValueError as error:
    print(f"Error: {error})


pessoa_juridica.cnpj= "123.432"




attrs = vars(pessoa1)
print(', '.join("%s: %s" % item for item in attrs.items()))
attrs = vars(pessoa_fisica)
print(', '.join("%s: %s" % item for item in attrs.items()))
attrs = vars(pessoa_juridica)
print(', '.join("%s: %s" % item for item in attrs.items()))