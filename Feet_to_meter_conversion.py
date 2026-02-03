def feet_to_meters():
    """ In this fucntion we are converting the user input that is string into meters and then reterning it back """
    feet = input("please enter a number that you want to convert to feet ")
    try:
        feet = float(feet)
    except(TypeError, ValueError):
        print("Error: you have not enterd a number please enter a number and not another value")
        return feet_to_meters()

    return feet * 0.3048
meters = feet_to_meters()
print(f"The number that you enterd converts to {meters}")
