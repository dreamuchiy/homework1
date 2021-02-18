def pref_by_age(age):
    assert age >= 0
    if age <= 5:
        return "Учиться в детском саду"
    elif age <= 18:
        return "Учиться в школе"
    elif age <= 23:
        return "Учиться в ВУЗе"
    else:
        return "Работать"
    # Про пенсию в ТЗ не было

age =  int(input("Введите возраст, пожалуйста:\n"))
to_do = pref_by_age(age)
print(to_do)       

