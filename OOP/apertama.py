class Hero:
    pass

hero1 = Hero() # object instance(instansiace)
hero2 = Hero()
hero3 = Hero()

hero1.name = "Sniper"
hero1.health = 100

hero2.name = "Joni"
hero2.health = 100

hero3.name = "Orico"
hero3.health = 100

print(hero1)
print(hero1.__dict__)
print(hero1.name)