class Measurement():

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __str__(self):
        return str(self.p1) + " " + str(self.p2)

    def __repr__(self):
        return self.__str__()

    def __lt__(self, other):
        return self.p2 < other.p2


m1 = Measurement("Pomiar", "Temperatury")
m2 = Measurement("Pomiar", "Czegos")
m3 = Measurement("Pomiar", "Wilgotnosci")
print(m1)
print(m2)
print(m3)
meas_list = [m1, m2, m3]
print(meas_list)
meas_list = sorted(meas_list)
print(meas_list)
