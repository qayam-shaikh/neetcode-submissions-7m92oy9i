class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars=[]
        for p,s in zip(position,speed):
            cars.append((p,(target-p)/s))
        cars.sort()
        fleet=fleet_time=0
        for car in cars[::-1]:
            _,t=car
            if t>fleet_time:
                fleet+=1
                fleet_time=t
        return fleet