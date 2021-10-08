import re


class Thermometer:
    """
    Целевой класс ртутный градусник
    """
    
    # здесь условно происходит замер температуры
    CURRENT_TEMPERATURE = 36

    def request(self):
        return self.CURRENT_TEMPERATURE


class ElectricThermometer:
    """
    Адаптируемый класс электрического градусника
    """

    CURRENT_TEMPERATURE = 'temperature -  145 F'

    def take_the_temperature(self):
        return self.CURRENT_TEMPERATURE


class Adapter(ElectricThermometer, Thermometer):
    """
    Адаптер переводит значение электрического градусника в подходящее для клиента
    """

    def request(self):
        fahrenheit = int(re.search(r'\d+', self.take_the_temperature()).group())
        fahrenheit_to_celsius = int((fahrenheit - 32) * 5 / 9)
        return fahrenheit_to_celsius


def look_at_the_thermometer(target: "Thermometer") -> None:
    """
    Клиентский код поддерживающий ртутный градусник по цельсию.
    """
    
    temperature = target.request()
    if temperature < 30:
        print('температура ', temperature, 'ты холодный как труп!')
    elif temperature >= 37:
        print('температура ', temperature, 'Кажется, ты заболел, или горишь')
    else:
        print('температура ', temperature, 'всё хорошо')


#  проверяем как всё работает
if __name__ == "__main__":
    print("пробуем померять температуру с помощью ртутного градусника")
    target = Thermometer()
    look_at_the_thermometer(target)
    print("\n")

    adaptee = ElectricThermometer()
    print("меряем электрическим градусником без адаптера:")
    print(adaptee.take_the_temperature())
    print("\n")

    print("меряем электрическим градусником вместе с адаптером:")
    adapter = Adapter()
    look_at_the_thermometer(adapter)
