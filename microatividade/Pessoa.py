class Pessoa:
    def __init__(self, nome, dataNascimento, cpf, rg, status):
        self.__nome = nome
        self.__dataNascimento = dataNascimento
        self.__cpf = cpf
        self.__rg = rg 
        self.__status = status

    @property
    def nome(self, nome):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def dataNascimento(self, dataNascimento):
        return self.__dataNascimento
    
    @dataNascimento.setter
    def  dataNascimento(self, dataNascimento):
        self.__dataNascimento = dataNascimento

    @property
    def cpf(self, cpf):
        return self.__cpf
    
    @cpf.setter 
    def cpf(self,cpf):
        if len(cpf) != 14:
            raise ValueError("O CPF deve conter 14 caracteres (no formado000.000.000-00).")
        
    @property
    def rg(self, rg):
        return self.__rg

    
    @rg.setter
    def rg(self, rg):
        self.__rg = rg
            
        
    @property 
    def status(self, status):
        return self.__status

    status.setter
    def status(self, status):
        self.__status = status    



    
    