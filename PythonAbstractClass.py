from abc import ABC,abstractmethod,ABCMeta
class TravelService(metaclass=ABCMeta):
    def __init__(self,startpoint,endpoint):
        self.start_point= startpoint
        self.end_point= endpoint
        self.total_fare = None
    @abstractmethod
    def calaculate_total_fare(self):
        pass

class AirService(TravelService):
    def __init__(self,startpoint,endpoint,baggage_weight,basicfare):
        super().__init__(startpoint,endpoint)
        self.baggage_handling_charges= None
        self.baggage_weight_in_kgs=baggage_weight
        self.basic_fare=basicfare

    def calaculate_total_fare(self):
        self.total_fare=self.basic_fare+ self.calculate_baggage_handling_charges()
        return self.total_fare
    """"
    Business Senario to calculate Baggage charges:
            upto 10kgs weight charge is:- 100rs
            each kg more than 10kg will charge 50rs per kg
    """
    def calculate_baggage_handling_charges(self):
        if(self.baggage_weight_in_kgs<=10):
            self.baggage_handling_charges=100
        else:
            self.baggage_handling_charges=200+(self.baggage_weight_in_kgs-10)*50
        return  self.baggage_handling_charges


class CabService(TravelService):
    def __init__(self, startpoint, endpoint, distance_in_kms,unitprice):
        super().__init__(startpoint, endpoint)
        self.distance_in_kms = distance_in_kms
        self.charge_per_km = unitprice


    def calaculate_total_fare(self):
        self.total_fare = self.distance_in_kms*self.charge_per_km

        return self.total_fare

if __name__ == '__main__':
    travelMode=["By Air","By Road"]
    print("Enter Mode of Travel:- 0 for By AIR, 1 for By Road")
    user_travel_mode_input= input()
    #print(travelMode[int(user_travel_mode_input)])
    if(int(user_travel_mode_input)==0):
        available_cities=["Banglore","Vishakapatnam","Chennai","Delhi","Mumbai"]
        prices=[1000,2000,3000,5000,6000]
        print("Select Your Source City:- Banaglore:- 0 , Vishakapatnam:- 1 , Chennai:- 2, Delhi:- 3, Mumbai:- 4")
        start_city= available_cities[int(input())]
        print("Select Your Destination City:- Banaglore:- 0 , Vishakapatnam:- 1 , Chennai:- 2, Delhi:- 3, Mumbai:- 4")
        price_index=int(input(),10)
        end_city = available_cities[price_index]
        baseprice = prices[price_index]
        print("Base Price"+ str(baseprice) )
        air_traveler_1= AirService(start_city,end_city,20,baseprice)
        print("Total Travel Cost: "+str(air_traveler_1.calaculate_total_fare()))


