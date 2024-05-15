class Flyweight:
#     def __init__(self, shared_state):
#         self._shared_state = shared_state

#     def operation(self, unique_state):
#         s = self._shared_state.copy()
#         s.update(unique_state)
#         print(f"Flyweight: Displaying shared ({s}) and unique ({unique_state}) states.")


# class FlyweightFactory:
#     _flyweights = {}

#     def __init__(self, initial_flyweights):
#         for state in initial_flyweights:
#             self._flyweights[self.get_key(state)] = Flyweight(state)

#     def get_key(self, state):
#         return "_".join(sorted(state))

#     def get_flyweight(self, shared_state):
#         key = self.get_key(shared_state)
#         if not self._flyweights.get(key):
#             print("FlyweightFactory: Can't find a flyweight, creating new one.")
#             self._flyweights[key] = Flyweight(shared_state)
#         else:
#             print("FlyweightFactory: Reusing existing flyweight.")
#         return self._flyweights[key]


# def main():
#     factory = FlyweightFactory([
#         ["Chevrolet", "Camaro2018", "pink"],
#         ["Mercedes Benz", "C300", "black"],
#         ["Mercedes Benz", "C500", "red"],
#         ["BMW", "M5", "red"],
#         ["BMW", "X6", "white"]
#     ])

#     def client(factories, brand, model, color):
#         print("\nClient: Trying to create a car.")
#         flyweight = factories.get_flyweight([brand, model, color])
#         flyweight.operation({"mileage": "10000", "owner": "John Doe"})

#     client(factory, "BMW", "M5", "red")
#     client(factory, "Mercedes Benz", "C300", "black")
#     client(factory, "Chevrolet", "Camaro2018", "pink")
#     client(factory, "BMW", "X6", "white")

# if __name__ == "__main__":
#     main()
