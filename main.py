class Node:
    def __init__(self, country):
        self.country = country
        self.edges = {}

    def add_edge(self, country, cost, time):
        self.edges[country] = {"cost": cost, "time": time}

    def get_edges(self):
        return self.edges

    

class Graph:
    def __init__(self, directed=False):
        self.vertices = {}
        self.directed = directed

    def add_vertex(self, country):
        node = Node(country)
        self.vertices[country] = node

    def bidirectional_flights(self, country_a, country_b, cost, time):
        self.vertices[country_a].add_edge(country_b, cost, time)
        self.vertices[country_b].add_edge(country_a, cost, time)

    

flights = Graph()
flights.add_vertex("Kuwait")
flights.add_vertex("Dubai")
flights.add_vertex("Doha")
flights.add_vertex("Tokyo")
flights.add_vertex("Male")
flights.add_vertex("Oslo")
flights.add_vertex("Tokyo")
flights.add_vertex("Colombo")

flights.bidirectional_flights("Kuwait", "Dubai", 120, 2)
flights.bidirectional_flights("Kuwait", "Colombo", 200, 4)
flights.bidirectional_flights("Colombo", "Male", 60, 1)
flights.bidirectional_flights("Dubai", "Doha", 100, 1.5)
flights.bidirectional_flights("Doha", "Tokyo", 500, 11)
flights.bidirectional_flights("Dubai", "Oslo", 300, 6)


for i in flights.vertices.keys():
    print (f"{i}")

country_a = input("\nChoose one of those countries: ")
print("")
print("-"*30)
print("")
print(f"avilable flights from {country_a}: ")

edges = flights.vertices[country_a].get_edges()
for choice in edges.keys():
    print (f"{choice}")

country_b = input("\nChoose your distination: ")

total = edges[country_b]

print ("cost: %d$ - time: %d H" % (total["cost"], total["time"]))


        



    



