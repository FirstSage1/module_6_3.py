# Модуль 6_3 множественные наследования.
# =======================================

class Horse:
    def __init__(self):
        self.x_distance = 0     #- пройденный путь.
        self.sound = 'Frrr'        #- звук, который издаёт лошадь.
        super().__init__()
    def run(self, dx):  #dx-изменение дистанции,увеличивает x_distance на dx.
        self.x_distance += dx

class Eagle:  #класс орла.
    def __init__(self):
        self.y_distance = 0  #высотаполёта
        self.sound = 'I train, eat, sleep, and repeat' #звук,который издаёт орёл (отсылка)

    def fly(self, dy):  #где dy - изменение дистанции, увеличивает y_distance на dy.
        self.y_distance += dy

class Pegasus(Horse, Eagle):    #Класс Пегаса
    def __init__(self):
        super().__init__()

    def move(self, dx, dy):  # где dx и dy изменения дистанции.
    # В этом методе должны запускаться наследованные методы run и fly соответственно.
        super().run(dx)
        super().fly(dy)
    def get_pos(self): # возвращает текущее положение пегаса в виде кортежа
                    # - (x_distance, y_distance) в том же порядке.
        return self.x_distance, self.y_distance
    def voice(self): #- который печатает значение унаследованного атрибута sound.
        print(self.sound)

p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())
p1.voice()
