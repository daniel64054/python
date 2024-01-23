from class_conta_bancaria import ContaBancaria

class ContaCorrente(ContaBancaria):
    def __init__(self):
        self.__limite = 0.0

    def abrirconta(self,nb=0,na=0,nc="",Titular="",saldo=0,limite=0.0):
        self._nbanco =nb
        self._nangencia =na
        self._nconta =nc
        self._titular = Titular
        self._saldo = saldo
        self.__limite= limite
        print("A conta "+self._nconta+"do sr(a) "+self._titular+"foi aberta")