noise_level = float(input("Введите уровень шума в децибелах:"))
if noise_level <40:
    print("Уровень шума ниже тихой комнаты(40дБ)")
elif noise_level ==40:
    print("Уровень шума соответсвует тихой комнате(40 дБ)")
elif noise_level <70:
    print("Уровень шума между тихой комнатой и будильником (40-70дБ")
elif noise_level ==70:
    print("Уровень шума соответствует будильнику (70дБ)")
elif noise_level <106:
    print("Уровень шума между будильником и газовой газоколонкой (70-106 дБ)")
elif noise_level == 106:
    print("Уровень шума соответствует газовой газоколонке (106 дБ)")
elif noise_level <130:
    print("Уровень шума между газовой газоколонкой и отбойным молотком (106 -130 дБ)")
elif noise_level ==130:
    print("Уровень шума соответствует отбойному молотку (130 дБ)")
else:
    print("Уровень шума превышает значение отбойного молотка (130дБ)")