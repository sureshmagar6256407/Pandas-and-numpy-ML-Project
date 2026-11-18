import numpy as np
from pandas.core.apply import Axis
from psutil import AIX  

class ChargingAnalysis : 
    def  __init__(self , battery_health , charging_time , energy_consumption) -> None:  
        self.battery_health = battery_health 
        self.charging_time = charging_time  
        self.energy_consumption = energy_consumption  


    def Basic_Battery_Analysis (self) : 
        self.EB_ABH   =  np.mean(self.battery_health , axis= 1 , keepdims= True)
        print(f"Every EV Average Battery health : \n {self.EB_ABH}")
        print()

        EB_LBH = np.min (self.battery_health , axis= 1 , keepdims= True)
        print(f"Every EV Battery lowest battery health is : \n {EB_LBH}")
        print()

        EB_HBH  = np.max(self.battery_health , axis= 1 , keepdims= True)
        print(f"every EV  battery highest battery health is : \n {EB_HBH}")
        print()

        EB_LBHI  = np.argmin(self.battery_health , axis=1 , keepdims= True)
        print(f"every EV battery Lowest battery health day index is : \n {EB_LBHI}")
        print()

        HBH  = np.max(self.battery_health)
        print(f"all EV battery highest battery health is : \n {HBH}")
        print()

        LBH  = np.min(self.battery_health )
        print(f"all EV battery lowest battery health is : \n {LBH}")
        print()

        ED_ABH  = np.mean(self.battery_health ,axis= 0, keepdims= True)
        print(f"every day average battery health is : {ED_ABH}")
        print()


    def Basic_Charging_Analysis (self) : 
        ET_CT   = np.sum(self.charging_time , axis= 1 ,keepdims= True)
        print(f"Every EV Total charging time is : \n {ET_CT}")
        print()

        EE_CT  = np.mean(self.charging_time , axis= 1 , keepdims= True)
        print(f"Every Ev   Average charging time is : \n {EE_CT}")
        print()

        highest_Charging_Ev  = np.argmax(np.max(self.charging_time ,axis= 1 ))
        print(f"Highest chargint Ev is : {highest_Charging_Ev}")  
        print()

        nine  =  np.mean(self.charging_time , axis= 0 , keepdims= True)
        print(f"Every day average charging time is : {nine}")
        print()  

        ten = self.charging_time[self.charging_time >= 55]     
        print(f"charging time >= 55 is : {len(ten)}")
        print()

    def Basic_Energy_Consumption (self) : 
        eleven  = np.sum(self.energy_consumption ,axis= 1 , keepdims= True)
        print(f"Every EV total energy consumption is : \n {eleven}")
        print()

        twelve  = np.argmax(np.max(self.energy_consumption ,axis= 1))
        print(f"highest energy consumption  EV is : {twelve}")
        print()

        thirteen  =  np.max(self.energy_consumption , axis= 1  ,  keepdims= True)
        print(f"Every Energy max energy consumption is : \n {thirteen}")
        print()

        fourteen  = self.energy_consumption[self.energy_consumption >=20]
        print(f"Energy consumption >= 20 : {fourteen}")
        print()

    def Advanced_Numpy(self) : 
        cond1  =   [ 
            self.battery_health >= 95 , 
            self.battery_health >= 85  , 
            self.battery_health < 85 
        ]
        choices  =["Excellent" ,"Good" ,"Need Attention"]  
        fifteen  = np.select(cond1 , choices , default="")
        print(F"battery health classification : \n {fifteen}")
        print()


        minimum_health  = np.min(self.battery_health ,axis= 1 , keepdims= True)  
        print(minimum_health)   
        maximum_health  = np.max(self.battery_health , axis= 1  , keepdims= True)
        print(maximum_health)
        sixteen  =   maximum_health  - minimum_health  
        print(f"Every Ev battery health fluctuation is :  {sixteen}")
        print()  

        seventeen  = np.argmax(sixteen )
        print(f"highest fluctuation EV is :  {seventeen}")
        print()

        eighteen  = np.argwhere (self.battery_health  < 85)
        print(f"battery health  < 85 : {eighteen}")  
        print() 


        nineteen = self.EB_ABH / np.mean(self.energy_consumption , axis= 1)
        print(f"Energy efficient indicator : {nineteen}")
        print()


        



def main() :
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

    c1  = ChargingAnalysis (battery_health , charging_time , energy_consumption)
    c1.Basic_Battery_Analysis()
    c1.Basic_Charging_Analysis()
    c1.Basic_Energy_Consumption()
    c1.Advanced_Numpy()

if __name__ == "__main__" : 
    main()







