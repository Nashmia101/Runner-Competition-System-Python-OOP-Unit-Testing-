import csv
from custom_errors import *

class Runner:
    """
    A class representing a runner.

    Attributes:
    
    max_energy(int):The maximum energy level of the runner.
    name(str):The name of the runner.
    age(int):The age of the runner.
    country(str):The country from where the runner belongs.
    sprint_speed(float):The sprint speed of the runner.
    endurance_speed(float):The endurance speed of the runner.
    energy(int):The current level of energy of the runner.

    Methods:
    __init__:Initializes a new Runner instance.
    country_csv():Reads the country names from a CSV file and returns them as a list.
    drain_energy:Drains the energy from the runner.
    recover_energy:Recovers the energy of the runner.
    run_race:conducts the race and calculates the time taken by runner to finish the race.
    __str__:Returns a string representation of the Runner instance.
    
    """
   
    max_energy = 1000
    def __init__(self,name: str, age: int, country: str, sprint_speed: float, endurance_speed: float) ->None:


        """
        Initializes a new Runner instance.

        Args:
        name(str):The name of the runner.
        age(int):The age of the runner.
        country(str):The country the runner represents.
        sprint_speed(float):The sprint speed of the runner.
        endurance_speed(float):The endurance speed of the runner.
        
        Raises:
        CustomAttributeError:Error is raised, if the 'max_energy' attribute is not present.
        CustomValueError:Error is raised,if any of the input values are incorrect.
        CustomTypeError:Error is raised,if any of the input types are incorrect.

        """
            # Raise an error if max_energy attribute is not found in the class
        if not hasattr(self.__class__, 'max_energy'):
                raise CustomAttributeError("Attribute 'max_energy' not found in class runner.")
            # Raise an error if name is an empty string
        if not name:
                raise CustomValueError("Incorrect input value for name, as name cannot be empty strings")
            # Raise an error if name is not of type str
        if not isinstance(name,str):
                raise CustomTypeError ("Incorrect input type for name, expected str got {type(name)} instead")
            # Raise an error if name is not alphanumeric
        if not ''.join(name.split()).isalnum():
                raise CustomValueError ("Incorrect input type for name,name is not alphanumeric")
            # Raise an error if name is purely digits
        if name.isdigit():
                raise CustomValueError ("Incorrect input type for name,name is not alphanumeric")
            # Raise an error if age is not of type int
        if not isinstance(age,int):
                raise CustomTypeError ("Incorrect input type for age, expected int got {type(age)} instead")
            # Raise an error if age is not between 5 and 120
        if (age<5 or age >120):
                raise CustomValueError ("Incorrect input value for age, age is not between 5 and 120")
            # Raise an error if sprint_speed is not of type float
        if not isinstance(sprint_speed,float):
                raise CustomTypeError ("Incorrect input type for sprint_speed, expected float got {type(sprint_speed)} instead")
            # Raise an error if sprint_speed is not between 2.2 and 6.8
        if (sprint_speed<2.2 or sprint_speed >6.8):
                raise CustomValueError ("Incorrect input value for sprint_speed, sprint_speed is not between 2.2 and 6.8")
            # Raise an error if endurance_speed is not of type float
        if not isinstance(endurance_speed,float):
                raise CustomTypeError ("Incorrect input type for endurancess_speed, expected float got {type(endurance_speed)} instead")
            # Raise an error if endurance_speed is not between 1.8 and 5.4
        if (endurance_speed<1.8 or endurance_speed >5.4):
                raise CustomValueError ("Incorrect input value for endurance_speed, endurance_speed is not between 1.8 and 5.4") 
            # Raise an error if country is not alphabetic
        if not isinstance(country,str):
                raise CustomTypeError ("Incorrect input type for country, expected str got {type(country)} instead")
            # Validate country against the CSV file
        correct_country=self.country_csv()
        # Raise an error if country is not in the list of countries from the CSV
        if country not in correct_country:
                raise CustomValueError ("This country is not present in the provided csv")

        # Initialize instance attributes
        self.name = name
        self.age = age
        self.country = country
        self.sprint_speed = sprint_speed
        self.endurance_speed = endurance_speed
        self.energy = self.max_energy
        
    def country_csv(self) -> list:
        """
        Reads the country names from a CSV file and returns them as a list.
        Returns:
        list: A list of country names.
        Raises:
        CustomKeyError: Error is raised,if a given country name (key) is not found in the CSV row
        """
        countries=[]
        with open ('countries.csv','r') as file:
            # Read the CSV file
            dict1=csv.DictReader(file)
            for row in dict1:
                if 'name' not in row:
                    # Raise an error if 'name' key is not found in a row
                    raise CustomKeyError("Key 'name' not found in CSV row.")
                # making list of countries
                countries.append(row['name'])
            return countries
    
    def drain_energy(self, drain_points: int)-> None:
        """
        Drains energy from the runner.
        Args:
        drain_points(int):The amount of energy that needs to be drained.
        Raises:
        CustomAttributeError:Error is raised, if the 'energy' attribute is not present.
        CustomTypeError:Error is raised, if 'drain_points' is not of type int.
        CustomValueError:Error is raised, if 'drain_points' is an negative value or greater than max_energy.
        """
        # Raise an error if energy attribute is not found
        if not hasattr(self, 'energy'):
            raise CustomAttributeError("Attribute 'energy' not found in class runner.")
            # Raise an error if drain_points is not of type int
        if not isinstance(drain_points,int):
            raise CustomTypeError ("Incorrect input type for drain_points, expected int got {type(drain_points)} instead")
            # Raise an error if drain_points is negative
        if drain_points <0:
            raise CustomValueError("Incorrect input value for drain_points, drain_points must be a positive integer")
            # Raise an error if drain_points is greater than max_energy
        if drain_points > self.max_energy:
            raise CustomValueError("Incorrect input value for drain_points, drain_points must be less then max energy")

        self.energy=self.energy-drain_points #reduce energy by drain_points
        if self.energy <=0: # check if energy goes below 0
            # Ensure energy does not go below 0
            self.energy=0
        
    
    def recover_energy(self, recovery_amount:int)-> None:
        """
        Recovers energy for the runner.
        Args:
        recovery_amount(int):The energy level to be recovered.
        Raises:
        CustomAttributeError: Error is raised,if the 'energy' attribute is not present.
        CustomTypeError:Error is raised, if 'recovery_amount' is not of type int.
        CustomValueError:Error is raised, if 'recovery_amount' is a negative value or greater than max_energy.
        """
        # Raise an error if energy attribute is not found
        if not hasattr(self, 'energy'):
            raise CustomAttributeError("Attribute 'energy' not found in class runner.")
        # Raise an error if recovery_amount is not of type int
        if not isinstance(recovery_amount,int):
            raise CustomTypeError ("Incorrect input type for recovery_amount, expected int got {type(recovery_amount)} instead")
        # Raise an error if recovery_amount is negative
        if recovery_amount <0:
            raise CustomValueError("Incorrect input value for recovery_amount, recovery_amount must be a positive integer")
        # Raise an error if recovery_amount is greater than max_energy
        if recovery_amount > self.max_energy:
            raise CustomValueError("Incorrect input value for Recovery amount, Recovery_amount cannot be greater than max energy")
        
        self.energy = self.energy + recovery_amount # recovering energy by the recovery_amount
        if self.energy > self.max_energy: # checking if energy is greater than max energy 
            self.energy=self.max_energy #if it is assign max energy to energy
        
    
    def run_race(self, race_type: str, distance: float)->float:

        """
        conducts the race and calculates the time taken by the runner to finish the race.

        Args:
        race_type(str):The type of race can be either 'short' or 'long'.
        distance(float):The distance in kilometers of the race.

        Returns:
        The time taken by the runner to finish the race in seconds.

        Raises:
        CustomTypeError: Error is raised,if 'distance' is not of type float.
        CustomValueError:Error is raised, if 'distance' is negative.
        CustomTypeError:Error is raised, if 'race_type' is not of type str.
        CustomValueError:Error is raised, if 'race_type' is not 'short' or 'long'.
        """
          #Raise an error if distance is not of type float
        if not isinstance(distance,float):
            raise CustomTypeError ("Incorrect input type for distance, expected float got {type(distance)} instead")
          # Raise an error if distance is negative
        if distance <=0:
            raise CustomValueError("Incorrect input value for distance, distance must be a positive integer")
         # Raise an error if race_type is not of type str
        if not isinstance(race_type,str):
            raise CustomTypeError ("Incorrect input type for race_type, expected str got {type(race_type)} instead")
          # Raise an error if race_type is not 'short' or 'long'
        if race_type not in ["short","long"]:
            raise CustomValueError("Incorrect input value for race_type, race_type must be either long or short")
       # checking if race_type is short 
        if race_type=='short':
            speed=self.sprint_speed
       # checking if race_type is long 
        elif race_type=='long':
            speed=self.endurance_speed
         # Convert distance to meters
        distance_meters = distance * 1000
        # Calculate time taken to complete the race
        time=(distance_meters/speed)
        time_taken=round(time,2)

        return time_taken
    
    def __str__(self):
        return f"Name: {self.name} Age: {self.age} Country: {self.country}"

if __name__ == '__main__':
    runner = Runner('Elijah',5,'Australia', 2.2,5.4)
    
    # running a short race
    time_taken = runner.run_race('long', 5.0)
    print(f"Runner {runner.name} took {time_taken} seconds to run 5.0km!")
    
