from race import *
from runner import Runner
from typing import List,Tuple,Dict,Union

class Competition:

    """
    A class of a competition amongst runners.

    Attributes:
        MAX_ROUNDS (int): The maximum number of rounds allowed in the competition.

    Methods:
        __init__: Initializes a Competition instance.
        __get_ordinal: Helper method to get the ordinal suffix for a number.
        conduct_competition: Conducts the competition, for all the rounds.
        conduct_race:Conducts the race
        update_leaderboard: Updates the leaderboard with the race results.
        print_leaderboard: Prints the leaderboard.
    """

    MAX_ROUNDS = 3 # Maximum number of rounds

    def __get_ordinal(self, n:int) -> str:
        suffixes = {1: 'st', 2: 'nd', 3: 'rd'}
        if 11 <= n % 100 <= 13:
            suffix = 'th'
        else:
            suffix = suffixes.get(n % 10, 'th')
        return f"{n}{suffix}"

    def __init__(self, runners: list, rounds: int, distances_short: list, distances_marathon: list)-> None:
        """
        Initializes a Competition instance.

        Args:
        runners (list): List of runners present in the competition.
        rounds (int): Number of rounds of the competition.
        distances_short (list): List of distances for short races.
        distances_marathon (list): List of distances for marathon races.
        
        Raises:
        CustomAttributeError: If an attribute is not present.
        CustomTypeError: If a variable has incorrect type.
        CustomValueError: If a variable has incorrect value.
        """

        #raise error if MAX_ROUNDS is not presnet in class competition
        if not hasattr (self.__class__, 'MAX_ROUNDS'):
            raise CustomAttributeError ("MAX_ROUNDS is not present in the class competition")
        #raise error if runners is not a list 
        if not isinstance(runners,list):
            raise CustomTypeError ("Incorrect input type for runners, expected list got {type(runners)} instead")
        #setting attributes 
        self.runners = runners
        self.runners_count=len(self.runners)
        self.rounds = rounds
        self.distances_short = distances_short
        self.distances_marathon = distances_marathon
        self.intial_leaderboard = {runner.name: 0 for runner in runners}
        self.leaderboard={}
        #raise error if distances_short is not presnet in class competition
        if not hasattr (self,'distances_short'):
            raise CustomAttributeError ("distances_short is not present in the class competition")
        #raise error if rounds is not presnet in class competition
        if not hasattr (self,'rounds'):
            raise CustomAttributeError ("rounds is not present in the class the class competition")
        #raise error if distances_marathon is not presnet in class competition
        if not hasattr (self, 'distances_marathon'):
            raise CustomAttributeError ("distances_marathon is not present in the class competition")
        # Raise error if rounds is not a integer
        if not isinstance(self.rounds,int):
            raise CustomTypeError ("Incorrect input type for rounds, expected int got {type(rounds)} instead")
        # Raise error if rounds is a negative integer
        if self.rounds <=0:
            raise CustomValueError("Incorrect input type for rounds,rounds is cannot be a negative integer")
        # Raise error if rounds are greater then max.rounds
        if self.rounds> self.MAX_ROUNDS:
            raise CustomValueError ("Incorrect input type for rounds,rounds cannot be more than max rounds")
        # Raise error if distances_short is not a list
        if not isinstance(self.distances_short, list):
            raise CustomTypeError("Incorrect input type for distances_short, expected list got {type(distances_short)} instead")
        # Raise error if distances_marathon is not a list
        if not isinstance(self.distances_marathon, list):
            raise CustomTypeError("Incorrect input type for distances_marathon, expected list got {type(distances_marathon)} instead")
        for i in range(len(self.distances_short)):
            # Raise error if short_distance is not a float
            if not isinstance(self.distances_short[i],float):
                raise CustomTypeError ("Incorrect input type for short_distance, expected float got {type(distances_short[i])} instead")
            # Raise error if distance_short is a negative integer
            if self.distances_short[i] <0:
                raise CustomValueError("Incorrect input value for distances_short, distances_short cannot be a negative integer")
        for i in range(len(self.distances_marathon)):
            # Raise error if distance_marathon is not a float
            if not isinstance(self.distances_marathon[i],float):
                raise CustomTypeError ("Incorrect input type for marathon_distance, expected float got {type(distances_marathon[i])} instead")
            # Raise error if distance_marathon is a negative integer
            if self.distances_marathon[i] <0:
                raise CustomValueError("Incorrect input value for distances_marathon, distances_marathon cannot be a negative integer")
        # Raise error if distance_shorts are not equal to the number of rounds
        if len(self.distances_short) != self.rounds:
            raise CustomValueError("the number of distances for short race are not equal to the number of rounds")
         # Raise error if distance_marathons are not equal to the number of rounds
        if len(self.distances_marathon) != self.rounds:
            raise CustomValueError("the number of distances for marathon race are not equal to the number of rounds")

    def conduct_competition(self)-> dict:
        """
        Conducts the competition for all rounds.

        Returns: dict: Leaderboard with final results.
        """
        # Conducts the competition, loop is being runned for all rounds.
        current_round = 1
        while current_round <= self.rounds:
            # Conduct short race for the current round
            short_race = ShortRace(self.distances_short[current_round-1], runners = self.runners)
            short_result = short_race.conduct_race()
            
            # Conduct marathon race for the current round
            marathon_race = MarathonRace(self.distances_marathon[current_round-1], runners = self.runners)
            marathon_result = marathon_race.conduct_race()
            
            # Here we recover energy for players who did not finish the race
            for runner, time_taken in marathon_result :
                if time_taken =='DNF':
                    runner.recover_energy(1000) # calling recovery energy function

             # Update leaderboard with results from both races
            self.update_leaderboard(short_result)
            self.update_leaderboard(marathon_result)
            current_round = current_round + 1 # iterate to the next round
        return self.leaderboard

    def conduct_race(self,race: Union[ShortRace, MarathonRace]) -> List[Tuple[Runner, str]]:
        """
        Conducts a race.
        Args:
        race: The race object to be conducted can be either ShortRace or MarathonRace.
        Returns:The result of the race(tuple).
        """
        return race.conduct_race()

    def update_leaderboard(self, results:List[Tuple[Runner, str]])-> None:
        """
        Updates the leaderboard according to the results of each round of race.

        Args:results (list): List of tuples which has runner name and their time taken to finish the race.
        """
        # Updates the leaderboard based on race results.
        # Sort the results based on time_taken by runners
        sorted_result = sorted(results, key=lambda x: x[1] if isinstance(x[1], float) else float('inf'))
        num_players = len(results)
         
        # Assign points based on position in the race
        for i, runner_time_taken in enumerate(sorted_result):
            runner, run_time = runner_time_taken
            if run_time == 'DNF': # if time_taken is DNF then assign 0 to points
                points = 0
            else:
                points = num_players - (i + 1) # else calculate the points according to their position
            # add points to the specific runners' points 
            self.intial_leaderboard[runner.name] = self.intial_leaderboard[runner.name]+points
        # Sort the leaderboard based on total points
        sorted_leaderboard = sorted(self.intial_leaderboard.items(), key=lambda x: x[1], reverse=True)
        # Assign runners and their points positions according to their points in the original leaderboard
        for i, (runner, points) in enumerate(sorted_leaderboard):
            location = self.__get_ordinal(i + 1)
            self.leaderboard[location] = (runner, points)
   
        # Set positions beyond the number of runners to None
        for i in range(num_players,self.runners_count):
            location = self.__get_ordinal(i + 1)
            self.leaderboard[location] = None

    def print_leaderboard(self)-> None:
        """
        Prints the leaderboard.
        """
        # Prints the leaderboard.
        for location, value in self.leaderboard.items():
            if value is None:
                pass
            else:
                runner, points = value
                print(f"{location} - {runner} ({points})")


if __name__ == '__main__':
    runners = [
        Runner("Elijah", 19, 'Australia', 6.4, 5.2),
        Runner("Rupert", 67, 'Botswana', 2.2, 1.8),
        Runner("Phoebe", 12, 'France', 3.4, 2.8),
        Runner("Lauren", 13, 'Iceland', 4.4, 5.1),
        Runner("Chloe", 21, 'Timor-Leste', 5.2, 1.9),
        
    ]

    competition = Competition(runners, 3, [0.5, 0.6, 1.2], [4.0, 9.0, 4.5])
    _ = competition.conduct_competition()
    competition.print_leaderboard()
