class Pessoa:
    def __init__(self, nome, numeroConta, dataAbertura, status):
        self.__nome = nome
        self.__numeroConta = numeroConta
        self.__dataAbertura = dataAbertura
        self.__status = status

    @property
    def nome(self, nome):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def numeroConta(self, numeroConta):
        return self.__numeroConta
    
    @numeroConta.setter
    def  numeroConta(self, numeroConta):
        self.__numeroConta = numeroConta

        
    @property
    def dataAbertura(self, dataAbertura):
        return self.__dataAbertura

    
    @dataAbertura.setter
    def dataAbertura(self, dataAbertura):
        self.__dataAbertura = dataAbertura
            
        
    @property 
    def status(self, status):
        return self.__status

    status.setter
    def status(self, status):
        self.__status = status    



    
    