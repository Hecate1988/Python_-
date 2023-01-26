name = "Lena"
print(f"She said her name is {name}")
print(f"She said her name is {name!r}")
#Формат для дробных чисел "result:{value:{width}.{precision}}"
#Для метода .format() будет: {value:10.5f}
num = 23.875527221
print("My number is: {0:10.5f}". format(num))
print("My number is: {0:7.4f}". format(num))

#Для f-strings будет: {value:{10}.{5}}
print(f"My number is: {num:{10}.{5}}")
print(f"My number is: {num:{7}.{4}}")
#Для f-strings точность  озн.общ.колличество цифр, а не только цифры после разделителя дробной части
#Можно использовать метод .format() внутри f-string:
print(f"My number is: {num:{10.6}}")
