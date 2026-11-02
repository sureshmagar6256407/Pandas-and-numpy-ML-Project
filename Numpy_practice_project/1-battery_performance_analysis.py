
import numpy  as np  

class ChargingAnalysis : 
    def  __init__(self , battery_health , charging_time , energy_consumption) -> None:  
        self.battery_health = battery_health 
        self.charging_time = charging_time  
        self.energy_consumption = energy_consumption  



def main() : 
    c1  = ChargingAnalysis

    
    # Rows = Electric vehicles, Columns = 7 days
    battery_health = np.array([
        [98, 97, 97, 96, 96, 95, 95],
        [92, 92, 91, 91, 90, 90, 89],
        [85, 85, 84, 84, 83, 82, 82],
        [99, 99, 98, 98, 98, 97, 97],
        [78, 78, 77, 76, 76, 75, 74],
        [88, 87, 87, 86, 85, 85, 84]
    ])
    
    charging_time = np.array([
        [35, 38, 36, 40, 37, 39, 35],
        [45, 48, 46, 50, 47, 49, 51],
        [55, 58, 56, 60, 59, 62, 61],
        [30, 32, 31, 33, 30, 34, 32],
        [70, 72, 75, 73, 76, 78, 80],
        [50, 52, 51, 55, 54, 56, 53]
    ])
    
    energy_consumption = np.array([
        [14, 15, 14, 16, 15, 14, 15],
        [17, 18, 17, 19, 18, 17, 18],
        [20, 21, 20, 22, 21, 23, 22],
        [13, 14, 13, 14, 13, 15, 14],
        [24, 25, 24, 26, 25, 27, 26],
        [18, 19, 18, 20, 19, 20, 19]
    ])

if __name__ == "__main___" : 
    main()