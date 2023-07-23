class UndergroundSystem:

    def __init__(self):
        
        self.time_dict = {}
        self.travellers = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        if id not in self.travellers:
            self.travellers[id] = (stationName, t)
        
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        
        if id not in self.travellers:
            return
        
        s1, t1 = self.travellers[id]
        
        if (s1, stationName) in self.time_dict:
            self.time_dict[(s1, stationName)].append((t-t1))
        else:
            self.time_dict[(s1, stationName)] = [t-t1]

        del self.travellers[id]
        
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        if (startStation, endStation) not  in self.time_dict:
            return 0.0
        return sum(self.time_dict[(startStation, endStation)])/len(self.time_dict[(startStation, endStation)])
        
        

# Your UndergroundSystem object will be instantiated and called as such:
obj = UndergroundSystem()
obj.checkIn(45,"Leyton",3)
obj.checkOut(45,"Waterloo",15)
print(obj.getAverageTime("Leyton","Waterloo"))