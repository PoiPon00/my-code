class TempMeasurement():

    def __init__(self, temp1, temp2):
        self.temp1 = temp1
        self.temp2 = temp2

    def __str__(self):
        return "Temperatura1 to " + str(self.temp1) + "," + " Temperatura2 to " + str(self.temp2)

    def temp_combinations(self):
        l = [];
        for i in range(self.temp1 + 1):
            for k in range(self.temp2 + 1):
                l.append((i, k))
        return l


my_operations = (TempMeasurement(2, 3))
print(my_operations)
print(my_operations.temp_combinations())

