class Length:
    def __init__(self, cm=0):
        self.__cm = cm

    def set_cm(self, cm):
        # TODO: Implement the method to set the value of __cm
        self.__cm = cm 

    def get_cm(self):
        # TODO: Implement the method to return the value of __cm
        return self.__cm

    def set_inch(self, inch):
        # TODO: Implement the method to convert inches to cm and set the value of __cm
        convertValue = inch * 2.54
        self.__cm = convertValue
        
    def get_inch(self):
        # TODO: Implement the method to convert __cm to inches
        return self.__cm/2.54
        

# Example usage
length = Length()

cm_value = 10
length.set_cm(cm_value)
inch_value = length.get_inch()
print(f"{cm_value} cm is {inch_value} inches.")

inch_value = 5
length.set_inch(inch_value)
cm_value = length.get_cm()
print(f"{inch_value} inches is {cm_value} cm.")
