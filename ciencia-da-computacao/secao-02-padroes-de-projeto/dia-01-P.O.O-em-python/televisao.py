class TV:
    def __init__(self, tamanho):
        self.volume = 50
        self.canal = 1
        self.tamanho = tamanho
        self.ligada = False


    def aumentar_volume(self):
        if self.volume < 99:
            self.volume += 1
            
        print(self.volume)


    def diminuir_volume(self):
        if self.volume > 0:
            self.volume -= 1

        print(self.volume)
      
    
    def modificar_canal(self, param):
        if param < 1 or param > 99:
            raise ValueError('Canal inválido')
        self.canal = param


    def ligar_desligar(self):
        if self.ligada == False:
            self.ligada = True
        else:
            self.ligada = False

minha_tv = TV(150)

print(minha_tv.aumentar_volume())

