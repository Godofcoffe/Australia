# .1 abstração
# .2 herança
# .3 polimorfismo

from time import sleep

class Barco:
    flutua = True

    def __init__(self, tamanho, cor, material):
        self.tamanho = tamanho
        self.cor = cor
        self.material = material

class Barco_motor(Barco):
    def __init__(self, tamanho, cor, material, motor):
        super().__init__(tamanho, cor, material)
        self.motor = motor
        self.vel = 0

    def acelerar(self):
        while self.vel < self.motor:
            print(self.vel)
            self.vel += 5
            sleep(0.5)
    
    def frear(self):
        while self.vel >= 0:
            print(self.vel)
            self.vel -= 10
            sleep(0.5)

class Barco_sem_motor(Barco):
    def __init__(self, tamanho, cor, material):
        super().__init__(tamanho, cor, material)

lancha = Barco_motor('3 metros', 'vermelho', 'aço', 100)
barco_comum = Barco_motor('2 metros', 'preto', 'polietileno', 50)

