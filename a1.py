class Computer:
    def __init__(self , maxPrice):
        self.__maxPrice = maxPrice

    def PrintInfo (self):
        print(self.__maxPrice)

    def SetMaxPrice(self , newMaxPrice):
        self.__maxPrice = newMaxPrice

    def GetMaxPrice(self):
        return self.__maxPrice
    
price = Computer("$750")
print(price.GetMaxPrice())
price.SetMaxPrice("$800")
print(price.GetMaxPrice())
