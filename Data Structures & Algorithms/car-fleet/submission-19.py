class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        res = len(position)
        cars = [[position[i],speed[i]] for i in range(len(position))]
        cars = sorted(cars, key = lambda x: x[0])
        
        front_pos = cars[-1][0]
        front_speed = cars[-1][1]
        for i in range(len(cars)-2,-1,-1):
            if (target - cars[i][0])/cars[i][1] <= (target - front_pos)/front_speed:
                res -= 1
            else:
                front_pos = cars[i][0]
                front_speed = cars[i][1]
            

        return res