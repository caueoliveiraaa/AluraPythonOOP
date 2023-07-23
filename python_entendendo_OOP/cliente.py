class Cliente:
    
    def __init__(self, nome) -> None:
        self.__nome = nome
        
    @property
    def nome(self):
        print("chamando @proprety nome()")
        return self.__nome.title()

    @nome.setter
    def nome(self, nome):
        print("chamando setter nome()")
        self.__nome = nome
