from colorama import Fore, Back, Style
# Management System
class Vehicle:
    def __init__(self, registration_number, vehicle_type, owner):
        self.registration_number = registration_number
        self.type = vehicle_type
        self.owner = owner

    def update_owner(self, new_owner):
        self.owner = new_owner
        print(f"Vehicle {self.registration_number} owner updated to {new_owner}")

# Creating instances of Vehicles 
vehicle1 = Vehicle(Fore.GREEN + "ABC001" + Style.RESET_ALL, "Car", Fore.RED + "Johnny Test" + Style.RESET_ALL)
vehicle2 = Vehicle(Fore.BLUE + "DEF002" + Style.RESET_ALL, "MotorCycle", Fore.RED + "Kanye West" + Style.RESET_ALL)
vehicle3 = Vehicle(Fore.MAGENTA + "GHI003" + Style.RESET_ALL, "Vespa", Fore.RED + "George Michael" + Style.RESET_ALL)
vehicle4 = Vehicle(Fore.YELLOW + "JKL004" + Style.RESET_ALL, "Truck", Fore.RED + "Bart Simpson" + Style.RESET_ALL)

# Display the vehicle owners 
print(f"Vehicle 1: Owner\n {vehicle1.registration_number}, {vehicle1.type}, {vehicle1.owner}")
print(f"Vehicle 2: Owner\n {vehicle2.registration_number}, {vehicle2.type}, {vehicle2.owner}")
print(f"Vehicle 3: Owner\n {vehicle3.registration_number}, {vehicle3.type}, {vehicle3.owner}")
print(f"Vehicle 4: Owner\n {vehicle4.registration_number}, {vehicle4.type}, {vehicle4.owner}")

# Updating owners 
vehicle1.update_owner(Fore.RED + "Mary Test" + Style.RESET_ALL)
vehicle2.update_owner(Fore.RED + "Kim Kardashian"+ Style.RESET_ALL)
vehicle3.update_owner(Fore.RED + "Michael Cera" + Style.RESET_ALL)
vehicle4.update_owner(Fore.RED + "Lisa Simpson" + Style.RESET_ALL)

# Display the updated vehicle owners
print(f"Vehicle 1: New Owner\n {vehicle1.registration_number}, {vehicle1.type}, {vehicle1.owner}")
print(f"Vehicle 2: New Owner\n {vehicle2.registration_number}, {vehicle2.type}, {vehicle2.owner}")
print(f"Vehicle 3: New Owner\n {vehicle3.registration_number}, {vehicle3.type}, {vehicle3.owner}")
print(f"Vehicle 4: New Owner\n {vehicle4.registration_number}, {vehicle4.type}, {vehicle4.owner}")


