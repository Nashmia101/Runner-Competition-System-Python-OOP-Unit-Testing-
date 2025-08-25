from custom_errors import *
from abc import ABC, abstractmethod
from runner import Runner
import math
from typing import List,Tuple,Dict,Union

class Race(ABC):
    """
    Abstract base class representing a race.
    Attributes:
    distance(float):The distance in kilometers of the race.
    runners(List[Runner]):The list of runners present in the race.

    Methods:
    add_runner:Adds a runner to the race.
    remove_runner:Removes a runner from the race.
    conduct_race():Abstract method to conduct the race.
    """
    def __init__(self, distance, runners: List[Runner] = None)-> None:
        """
        Initializes a Race object.
        Args:
        distance(float):The distance of the race in kilometers.
        runners(List):The list of runners present in the race., by default None which assigns an empty list.
        Raises:
        CustomTypeError: This error is raised if 'runners' is not None or a list, or if 'distance' is not a float.
        CustomValueError: This error is raised if 'distance' is negative.
        CustomAttributeError:This error is raised if any runner in 'runners' is not an instance of the Runner class.
        """
        # raise error if runner is not none or list 
        if not (runners is None or isinstance(runners, list)):
            raise CustomTypeError("runners must be None or a list")

        if runners is None or runners == []:
            self.runners = [] # Initialize an empty list if runners is None or empty
        else:
            self.runners = []
            for i in runners: # check if runner is an instance of Runner class
                if isinstance(i, Runner):
                    self.runners.append(i) # Append runner if it is an instance of Runner
                else:
                    raise CustomAttributeError("runner is not an object of Runner class") # if it is not an instance of runner class raise attribute error
        # Raise error if distance is not a float
        if not isinstance(distance,float):
            raise CustomTypeError ("Incorrect input type for distance, expected float got {type(distance)} instead")
        # Raise error if distance is negative
        elif distance <=0:
            raise CustomValueError("Incorrect input value for distance, distance must be a positive integer")
        # Set the distance 
        else:
            self.distance = distance
    
    def add_runner(self, runner: Runner) -> None:
        """
        Adds a runner to the race.
        Args:
        runner (Runner):The runner that needs to be added
        Raises:
        CustomAttributeError: This error is raised if the 'runners' attribute is not found.
        RunnerAlreadyExistsError:This error is raised if the runner is already in the race.
        RaceIsFullError:This error is raised if the race is full.
        """
        # Raise error if 'runners' attribute is not present
        if not hasattr(self, 'runners'):
            raise CustomAttributeError("Attribute 'runners' not found in Class Race.")
        # Raise error if runner is already in the race
        if runner in self.runners:
            raise RunnerAlreadyExistsError("Runner {runner.name} already exists so cannot add again")
        else:
            self.runners.append(runner)  # Add runner to the race
        # Raise error if the race is full
        if len(self.runners)>self.maximum_participants:
            raise RaceIsFullError ("The limit of maximum participants has been reached so cannot add more runners")
    
    def remove_runner(self, runner: Runner) -> None:
        """
        Removes a runner from the race.
        Args:
        runner(Runner):The runner that needs to be removed
        Raises:
        CustomAttributeError:This error is raised if the 'runners' attribute is not found.
        RunnerDoesntExistError: This error is raised if the runner is not in the race.
        """
        #Raise error if 'runners' attribute is not present
        
        if not hasattr(self, 'runners'):
            raise CustomAttributeError("Attribute 'runners' not found.")
        # Raise error if runner is not in the race
        if runner not in self.runners:
            raise RunnerDoesntExistError ("Runner {runner.name} doesn't exist so cannot remove ")
        else:
            self.runners.remove(runner) # Remove runner from the race
    
    @abstractmethod
    def conduct_race(self) -> List[Tuple[Runner, Union[str, float]]]:
        """
        Conducts the race and returns the results.
        Returns:
        List[Tuple[Runner, Union[str, float]]]:
        A list of tuples containing the runner and their time taken to finish the race.
        """
        pass

class ShortRace(Race):

    """
    Class representing a short race.
    Attributes:
    race_type(str):The type of the race is short.
    maximum_participants(int):The maximum number of participants allowed in the race.
    time_multiplier(float):The time multiplier for the race time.

    Methods:
    conduct_race():Conducts the short race and returns the results
    Raises:

    CustomAttributeError: This error is raised,if attribute is not present.
    CustomTypeError:This error is raised, if 'maximum_participants' is not an int, or if 'race_type' is not str or 'time_multiplier' is not float.
    """
    
    def __init__(self, distance, runners: List[Runner] = None)-> None:
        """
        Initializes a ShortRace object.
        Args:
        distance(float):The distance in kilometers of the race.
        runners(List[Runner] = None):The list of runners present in the race, by default None.
        """
        super().__init__(distance, runners) # inheriting parent class init method 

        # Set specific attributes for ShortRace
        self.race_type = "short"
        self.maximum_participants = 8
        self.time_multiplier = 1.2
        
        # Raise error if 'race_type' attribute is not present 
        if not hasattr(self, 'race_type'):
            raise CustomAttributeError ("Attribute 'race_type' not found in class ShortRace.")
        # Raise error if 'maximum_participants' attribute is not present
        if not hasattr(self, 'maximum_participants'):
            raise CustomAttributeError ("Attribute 'maximum_participants' not found in ShortRace .")
        # Raise error if 'time_multiplier' attribute is not present
        if not hasattr(self, 'time_multiplier'):
            raise CustomAttributeError("Attribute 'time_multiplier' not found in ShortRace .")
        # Raise error if maximum_participants's data type is not an int
        if not isinstance(self.maximum_participants,int):
            raise CustomTypeError ("Incorrect input type for maximum_participants, expected int got {type(maximum_participants)} instead")
        # Raise error if race_type's data type is not a str
        if not isinstance(self.race_type,str):
            raise CustomTypeError ("Incorrect input type for race_type, expected str got {type(race_type)} instead")
        
    def conduct_race(self)-> List[Tuple[Runner, Union[str, float]]]:

        """
        Conducts the short race and returns the results.
        Returns:List[Tuple[Runner, Union[str, float]]]:A list of tuples containing the runner's name and their time taken to finish the race.
        """
        result = []
        # Calculate time taken by each runner and apply time multiplier
        for i, runner in enumerate(self.runners):
            time_taken = runner.run_race(self.race_type, self.distance) * self.time_multiplier
            result.append((runner, time_taken)) # append the runner and the time taken in result list as tuple
        return result

class MarathonRace(Race):

    """
    Class representing a marathon race.
    Attributes:
    race_type(str):The type of the race is long.
    energy_per_km(int):The energy drained per kilometer.
    maximum_participants(int):The maximum number of participants allowed in the race.

    Methods:
    conduct_race():Conducts the marathon race and returns the results.
    """
    
    def __init__(self, distance: float, runners: List[Runner] = None)-> None:
        """
        Initializes a MarathonRace object.

        Args:
        distance(float):The distance in kilometers of the race.
        runners(List[Runner] = None):The list of runners present in the race, by default None

        Raises:
        CustomAttributeError: Error is raised ,if a attribute is not present.
        CustomTypeError:Error is raised, if 'maximum_participants is not int 'or 'energy_per_km' is not int, or if 'race_type' is not str.
        """
        super().__init__(distance, runners) # inheriting parent class init method 
        # Set specific attributes for MarathonRace
        self.race_type = "long"
        self.energy_per_km = 100
        self.maximum_participants = 16
         
        # Raise error if 'race_type' attribute is not present 
        if not hasattr(self, 'race_type'):
            raise CustomAttributeError("Attribute 'race_type' not found in class MarathonRace.")
        # Raise error if 'maximum_participants' attribute is not present 
        if not hasattr(self, 'maximum_participants'):
            raise CustomAttributeError("Attribute 'maximum_participants' not found in MarathonRace .")
        # Raise error if 'energy_per_km' attribute is not present 
        if not hasattr(self, 'energy_per_km'):
            raise CustomAttributeError("Attribute 'energy_per_km' not found in class MarathonRace.")
        # Raise error if maximum_participants's data type is not an int
        if not isinstance(self.maximum_participants,int):
            raise CustomTypeError ("Incorrect input type for maximum_participants, expected int got {type(maximum_participants)} instead")   
        # Raise error if race_type's data type is not a str
        if not isinstance(self.race_type,str):
            raise CustomTypeError ("Incorrect input type for race_type, expected str got {type(race_type)} instead")
        # Raise error if energy_per_km's is not an int
        if not isinstance(self.energy_per_km,int):
            raise CustomTypeError ("Incorrect input type for energy_per_km, expected str got {type(energy_per_km)} instead")
    
    def conduct_race(self)-> List[Tuple[Runner, Union[str, float]]]:
        result = []
       
        for i, runner in enumerate(self.runners): # Iterate through each runner
             time_taken = 0
             for km in range(math.ceil(self.distance)): # Iterate through each kilometer
                    if runner.energy > 0:
                        time_taken += runner.run_race("long", self.distance) # Calculate time taken by the runner and drain energy per km
                        runner.drain_energy(self.energy_per_km)
                    else:
                        time_taken = 'DNF'  # Assign 'DNF' if runner has no energy left anymore
                        break
             result.append((runner, time_taken)) # Append result for each runner
        return result
        
if __name__ == '__main__':
    short_race = ShortRace(5.0)
    long_race = MarathonRace(5.0)

    # Add a Runner
    eli = Runner('Elijah', 18, 'Australia', 5.8, 4.4)
    rup = Runner('Rupert', 23, 'Australia', 2.3, 1.9)

    long_race.add_runner(eli)
    long_race.add_runner(rup)

    results = long_race.conduct_race()
    for runner, time in results:
        print(runner.name, time) 
