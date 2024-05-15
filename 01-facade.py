"""Facade pattern with an example of WashingMachine"""
                   #Structures
#واجهة مبسطة لنظام فرعي معقد 
	#	"""facdeمتى نستخدم 
	#نظام فرعي معقد  
	#تحسين قابلية الاستخدام
	#فصل الواجهات عن التنفيذ
	#	"""
 
 
 #proved simple interface

                                  #client        Complex class             facade

class Washing: 
	'''Subsystem # 1'''

	def wash(self): 
		print("Washing...") 


class Rinsing: 
	'''Subsystem # 2'''

	def rinse(self): 
		print("Rinsing...") 


class Spinning: 
	'''Subsystem # 3'''

	def spin(self): 
		print("Spinning...") 


class WashingMachine: 
	'''Facade'''

	def __init__(self): 
		self.washing = Washing() 
		self.rinsing = Rinsing() 
		self.spinning = Spinning() 

	def startWashing(self): 
		self.washing.wash() 
		self.rinsing.rinse() 
		self.spinning.spin() 

""" main method """
if __name__ == "__main__": 

	washingMachine = WashingMachine() 
	washingMachine.startWashing() 
#-------------------------------------------------------------------------
"""
Output:

Washing...
Rinsing...
Spinning...
"""
#-------------------------------------------------------------------------
print ("#-------------------------------------------------------------------------")
class cars:
    def car(self):
        print("BMW")
class models:
    def model(self):
        print("BMW X5")

class factory:
    def __init__(self):
        self.car = cars()
        self.model = models()

    def get_car(self):
        self.car.car()
        self.model.model()


if __name__ == "__main__":
    factory = factory()
    factory.get_car()

"""
Output:

BMW
BMW X5
"""
#-------------------------------------------------------------------------