from Pessoa import Pessoa

class PessoaJuridica(Pessoa):
    def __init__(self, nome, numeroConta, dataAberturaConta, status, dataAberturaEmpresa, cnpj ):
        super().__init__(nome, numeroConta, dataAberturaConta, status)
        self.__dataAbertura = dataAberturaEmpresa
        self.__cnpj = cnpj


@property
def dataAberturaEmpresa(self, dataAberturaEmpresa):
    return self, dataAberturaEmpresa

@dataAberturaEmpresa.setter
def dataAberturaEmpresa(self, dataAberturaEmpresa):
    self.__dataAberturaEmpresa = dataAberturaEmpresa

@property
def cnpj(self, cnpj):
    return self.__cnpj

@cnpj.setter
def cnpj(self, cnpj):
    if len != 18:
        raise ValueError("O CPF deve conter 18 (para comportar o formatob 00.000.000/0001-00);")
    




  
   