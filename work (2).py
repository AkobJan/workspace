class Lift:
    def __init__(self, itog, ostanovki, gruz, type_build,country,MP,count):
        self.itog = itog
        self.ostanovki = ostanovki
        self.gruz = gruz
        self.type_build = type_build
        self.country = country
        self.MP = MP
        self.count = count
                        #МОСКВА И ОБЛАСТЬ
    def moscov_lift(self):
    #На основе этих чисел будет меняться цена
        if self.ostanovki == 2 and self.gruz == 320 and self.type_build == 'Торговый центр' and self.country == 'Россия' and self.MP == 'Без МП' and self.count == 1:
            self.itog == 4600
    #Остановки
        if self.ostanovki >= 5:
            self.itog += 250
        elif self.ostanovki >= 9:
            self.itog += 900
        elif self.ostanovki >= 18:
            self.itog += 1400
    #Грузоподьемность
        if self.gruz == 400:
            self.itog += 50
        elif self.gruz == 630:
            self.itog += 200
        elif self.gruz == 800:
            self.itog += 500
        elif self.gruz == 1000:
            self.itog += 550
        elif self.gruz == 1250:
            self.itog += 650
        elif self.gruz == 1600:
            self.itog += 800
        elif self.gruz == 2000:
            self.itog += 4700
    #Тип здания
        if self.type_build == 'Жилой дом':
            self.itog -= 450
        elif self.type_build == 'Предприятие':
            self.itog += 400
        elif self.type_build == 'Офисное здание':
            self.itog -= 100
    #Страна-производитель
        if self.country == 'Европа':
            self.itog += 500
        if self.country == 'Турция':
            self.itog += 500
        if self.country == 'Китай':
            self.itog += 500
    #Машинное оборудование
        if self.MP == 'C машинным помещением':
            self.itog -= 200
    #Количество лифтов выбранной конфигурации
        if self.count == 2:
            self.itog * 2
                        #ТУЛА И ОБЛАСТЬ
    def tula_lift(self,itog,ostanovki,gruz,type_build,country,MP,count):
    #На основе этих чисел будет меняться цена
        if self.ostanovki == 2 and self.gruz == 320 and type == 'Торговый центр' and self.country == 'Россия' and MP == 'Без МП' and count == 1:
            self.itog == 3300
        #Остановки
        if self.ostanovki >= 5:
            self.itog += 200
        elif self.ostanovki >= 9:
            self.itog += 700
        elif self.ostanovki >= 18:
            self.itog += 1000
    #Грузоподьемность
        if self.gruz == 400:
            self.itog += 40
        elif self.gruz == 630:
            self.itog += 60
        elif self.gruz == 800:
            self.itog += 360
        elif self.gruz == 1000:
            self.itog += 400
        elif self.gruz == 1250:
            self.itog += 450
        elif self.gruz == 1600:
            self.itog += 550
        elif self.gruz == 2000:
            self.itog += 3200
    #Тип здания
        if self.type_build == 'Жилой дом':
            self.itog -= 300
        elif self.type_build == 'Предприятие':
            self.itog += 350
        elif self.type_build == 'Офисное здание':
            self.itog -= 50
    #Страна-производитель
        if self.country == 'Европа':
            self.itog += 320
        if self.country == 'Турция':
            self.itog += 320
        if self.country == 'Китай':
            self.itog += 320
    #Машинное оборудование
        if MP == 'C машинным помещением':
            self.itog -= 150
    #Количество лифтов выбранной конфигурации
        if count == 2:
            self.itog * 2
                        #КАЛУГА И ОБЛАСТЬ
    def kaluga_lift(self,itog,ostanovki,gruz,type_build,country,MP,count):
    #На основе этих чисел будет меняться цена
        if self.ostanovki == 2 and self.gruz == 320 and type == 'Торговый центр' and self.country == 'Россия' and MP == 'Без МП' and count == 1:
            self.itog == 3900
        #Остановки
        if self.ostanovki >= 5:
            self.itog += 200
        elif self.ostanovki >= 9:
            self.itog += 850
        elif self.ostanovki >= 18:
            self.itog += 1200
    #Грузоподьемность
        if self.gruz == 400:
            self.itog += 40
        elif self.gruz == 630:
            self.itog += 70
        elif self.gruz == 800:
            self.itog += 260
        elif self.gruz == 1000:
            self.itog += 400
        elif self.gruz == 1250:
            self.itog += 450
        elif self.gruz == 1600:
            self.itog += 580
        elif self.gruz == 2000:
            self.itog += 2900
    #Тип здания
        if self.type_build == 'Жилой дом':
            self.itog -= 350
        elif self.type_build == 'Предприятие':
            self.itog += 370
        elif self.type_build == 'Офисное здание':
            self.itog -= 80
    #Страна-производитель
        if self.country == 'Европа':
            self.itog += 400
        if self.country == 'Турция':
            self.itog += 400
        if self.country == 'Китай':
            self.itog += 400
    #Машинное оборудование
        if MP == 'C машинным помещением':
            self.itog -= 170
    #Количество лифтов выбранной конфигурации
        if count == 2:
            self.itog * 2
        return self.itog
mylift = Lift()
print(mylift.moscov_lift())