class Mobile:
    def __init__(self,name,version,battery,price):
        self.name = name
        self.version = version
        self.battery = battery
        self.__price = price

    def show_mobile(self):
        print("Mobile Name:",self.name)
        print("Android Version:",self.version)
        print("Battery Power:",self.battery)

    def get_price(self):
        return self.__price


class Tecno(Mobile):
    def __init__(self, name, version, battery, price):
        Mobile.__init__(self, name, version, battery, price)


class Samsung(Tecno):
    def __init__(self, name, version, battery, price):
        Tecno.__init__(self, name, version, battery, price)


phone = Samsung("Samsung Galaxy", "S25", 6000, 65000)
phone.show_mobile()
print("Mobile Price:", phone.get_price())
