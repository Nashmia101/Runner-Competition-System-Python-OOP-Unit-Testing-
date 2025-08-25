import unittest
from competition import Competition
from runner import Runner
from custom_errors import CustomTypeError, CustomValueError
from race import Race, ShortRace, MarathonRace

class SimpleShortRace(ShortRace):
    """A simple race implementation to simulate ShortRace"""
    def __init__(self, distance, runners):
        super().__init__(distance, runners)
       
    def conduct_race(self):
        # Return a sorted list of runners based on a simple criterion (e.g., speed)
        return sorted(
            [(runner, self.distance / runner.sprint_speed) for runner in self.runners],
            key=lambda x: x[1]
        )

class SimpleMarathonRace(MarathonRace):
    """A simple race implementation to simulate MarathonRace"""
    def __init__(self, distance, runners):
        super().__init__(distance, runners)
       
    def conduct_race(self):
        # Return a sorted list of runners based on a simple criterion (e.g., speed)
        return sorted(
            [(runner, self.distance / runner.endurance_speed) for runner in self.runners],
            key=lambda x: x[1]
        )

class TestCompetition(unittest.TestCase):

    def setUp(self):
        # Create some runner instances for testing
        self.runners = [
            Runner("Elijah", 19, 'Australia', 6.4, 5.2),
            Runner("Rupert", 67, 'Botswana', 2.2, 1.8),
            Runner("Phoebe", 12, 'France', 3.4, 2.8),
            Runner("Lauren", 13, 'Iceland', 4.4, 5.1),
            Runner("Chloe", 21, 'Timor-Leste', 5.2, 1.9)
        ]
       
        # Set up a competition instance
        self.distances_short = [0.5, 0.6, 1.2]
        self.distances_marathon = [4.0, 11.0, 4.5]
        self.competition = Competition(self.runners, 3, self.distances_short, self.distances_marathon)

    def test_init_valid_input(self):
        # Assert that the competition instance is properly initialized
        self.assertEqual(self.competition.runners, self.runners)
        self.assertEqual(self.competition.rounds, 3)
        self.assertEqual(self.competition.distances_short, self.distances_short)
        self.assertEqual(self.competition.distances_marathon, self.distances_marathon)
        self.assertIsNotNone(self.competition.leaderboard)

    def test_init_invalid_input(self):
        # Test invalid runners list
        with self.assertRaises(CustomTypeError):
            Competition("not a list", 3, self.distances_short, self.distances_marathon)
       
        # Test invalid rounds
        with self.assertRaises(CustomValueError):
            Competition(self.runners, 0, self.distances_short, self.distances_marathon)
       
        with self.assertRaises(CustomValueError):
            Competition(self.runners, 4, self.distances_short, self.distances_marathon)
       
        # Test invalid distance lists
        with self.assertRaises(CustomTypeError):
            Competition(self.runners, 3, "not a list", self.distances_marathon)
       
        with self.assertRaises(CustomTypeError):
            Competition(self.runners, 3, self.distances_short, "not a list")

    def test_conduct_competition(self):
        # Conduct the competition
        leaderboard = self.competition.conduct_competition()

        # Assert the leaderboard is of the correct type
        self.assertIsInstance(leaderboard, dict, f"Leaderboard should be a dictionary")

    
    def test_conduct_race(self):
        # Use real race classes for testing
        short_race = SimpleShortRace(0.5, self.runners)
        marathon_race = SimpleMarathonRace(4.0, self.runners)
       
        # Conduct races
        short_result = self.competition.conduct_race(short_race)
        marathon_result = self.competition.conduct_race(marathon_race)
       
        # Verify that results are sorted by time correctly
        # Assuming lower times indicate higher rank
        self.assertLess(short_result[0][1], short_result[1][1])  # 1st should be faster than 2nd
        self.assertLess(marathon_result[0][1], marathon_result[1][1])  # 1st should be faster than 2nd  


    def test_update_leaderboard(self):
        # Define test results for updating the leaderboard
        race_results = [(self.runners[0], 10.0), (self.runners[1], 12.0), (self.runners[2], 14.0)]
        self.competition.update_leaderboard(race_results)
       
        # Validate the leaderboard
        expected_leaderboard = {
            '1st': ('Elijah', 2),
            '2nd': ('Rupert', 1),
            '3rd': ('Phoebe', 0),
            '4th': None,
            '5th': None
        }
        self.assertEqual(self.competition.leaderboard, expected_leaderboard)

    
    def test_conduct_competition1(self):
        """
        Test conducting the competition and checking if the leaderboard is sorted correctly.
        """
        leaderboard = self.competition.conduct_competition()
        leaderboard_values = list(leaderboard.values())
        sorted_values = sorted(leaderboard_values, key=lambda x: x[1], reverse=True) # sorting the results
        self.assertEqual(leaderboard_values, sorted_values) # check if it matches the expected output 

    def test_conduct_competition2(self):
        """
        Test conducting the competition with the minimum allowed rounds (1).
        """
        competition = Competition(self.runners, 1, [3.9], [5.1])
        leaderboard = competition.conduct_competition()
        leaderboard_values = list(leaderboard.values())
        sorted_values = sorted(leaderboard_values, key=lambda x: x[1], reverse=True)
        self.assertEqual(leaderboard_values, sorted_values) # check if it matches the expected output 
    
    def test_conduct_competition_3(self):
        """ 
        Testing Conduct competition
        """
        leaderboard = self.competition.conduct_competition()

        self.assertEqual(len(leaderboard), 5, f"Leaderboard should have 5 entries")

    def test_conduct_competition_4(self):
        """
        Testing competition with different numbers of distances for short and marathon races
        """
        unequal_distances_short = [1.5, 7.6]
        unequal_distances_marathon = [5.0, 6.0, 7.5]
   
        with self.assertRaises(CustomValueError):
          competition = Competition(self.runners, 3, unequal_distances_short, unequal_distances_marathon)

            

    def test_conduct_race1(self):
        """
        Test conducting a race with different speeds for each runner for short race.
        """
        self.runners[0].sprint_speed = 2.4
        self.runners[1].sprint_speed = 5.4
        self.runners[2].sprint_speed = 3.4
        self.runners[3].sprint_speed = 3.8
        self.runners[4].sprint_speed = 4.4
    
        short_race = SimpleShortRace(7.5, self.runners)
        result = self.competition.conduct_race(short_race)
        duration = []
        for runner, time in result:
            duration.append(time)
        self.assertEqual(duration, sorted(duration)) # check if it matches the expected output 
        
    def test_conduct_race2(self):
        """
        Test conducting a race with only one runner for short race.
        """
        one_runner = [self.runners[0]]
        one_runner[0].sprint_speed = 4.0 
   
        short_race = SimpleShortRace(3.5, one_runner)
        result = self.competition.conduct_race(short_race) #calculating the expected result 
        expected_result = 3.5 / one_runner[0].sprint_speed
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], (one_runner[0], expected_result)) # check if it matches the expected output 

    def test_conduct_race3(self):
        """
        Test conducting a race with only one runner for marathon race.
        """
        one_runner = [self.runners[0]]
        one_runner[0].endurance_speed = 3.3 
   
        long_race = SimpleMarathonRace(2.5, one_runner)
        result = self.competition.conduct_race(long_race)#calculating the expected result 
        expected_result = 2.5 / one_runner[0].endurance_speed
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], (one_runner[0], expected_result)) # check if it matches the expected output 

    def test_conduct_race4(self):
        """
        Test conducting a race with different speeds for each runner for marathon race.
        """
        self.runners[0].sprint_speed = 2.2
        self.runners[1].sprint_speed = 3.1
        self.runners[2].sprint_speed = 4.2
        self.runners[3].sprint_speed = 2.9
        self.runners[4].sprint_speed = 5.0
    
        long_race = SimpleMarathonRace(5.7, self.runners)
        result = self.competition.conduct_race(long_race)
        duration = []
        for runner, time in result:
            duration.append(time)
        self.assertEqual(duration, sorted(duration)) # check if it matches the expected output    

    def test_conduct_race5(self):
        """
        Conducting a race with no runner
        """
        short_race = SimpleShortRace(6.7, [])
        result = self.competition.conduct_race(short_race)
       
        # checking if results match 
        self.assertEqual(result, [])

    
    def test_update_leaderboard1(self):
        """
        Test updating the leaderboard with no runners.
        """
        race_results = []
        self.competition.update_leaderboard(race_results)
       
        # Validate the leaderboard with no runners
        expected_leaderboard = {
            '1st': None,
            '2nd': None,
            '3rd': None,
            '4th': None,
            '5th': None
        }
        self.assertEqual(self.competition.leaderboard, expected_leaderboard) # check if it matches the expected output 
    
  
    def test_update_leaderboard2(self):
        """
        Test updating the leaderboard with a very large race time.
        """
        
        race_results = [
            (self.runners[0], 15.0),
            (self.runners[1], 1e10),  
            (self.runners[2], 19.7)
        ]
    
        self.competition.update_leaderboard(race_results)

    def test_update_leaderboard3(self):
        """
        Test updating the leaderboard when a runner does not finish (DNF) the race.
        """
        race_results = [
            (self.runners[0], 20.0),
            (self.runners[1], 'DNF'),  
            (self.runners[2], 19.0),
            (self.runners[3], 4.0),
            (self.runners[4], 8.0)
        ]
    
        self.competition.update_leaderboard(race_results)
        
    def test_print_leaderboard1(self):
        """
        Test printing the leaderboard with some points.
        """
        race_results = [
            (self.runners[0], 8.0),
            (self.runners[1], 7.0),
            (self.runners[2], 6.0)
        ]
        self.competition.update_leaderboard(race_results)
        self.competition.print_leaderboard()

    def test_print_leaderboard2(self):
        """
        Test printing the leaderboard with duplicate points.
        """
        race_results = [
            (self.runners[0], 1.0),
            (self.runners[1], 1.0),
            (self.runners[2], 14.0)
        ]
        self.competition.update_leaderboard(race_results)
        self.competition.print_leaderboard()
        
        
    def test_print_leaderboard3(self):
        """
        Test printing the leaderboard with points for all runners.
        """
        race_results = [
            (self.runners[0], 13.4),
            (self.runners[1], 7.5),
            (self.runners[2], 6.7),
            (self.runners[3], 3.8),
            (self.runners[4], 18.0)
    ]
        self.competition.update_leaderboard(race_results)
        self.competition.print_leaderboard()


    def test_init1(self):
        """
        Testing competion by increaseing Max.Rounds
        """
        
        self.distances_short = [2.5, 3.7, 1.5, 6.5, 3.4]
        self.distances_marathon =[5.3, 3.9, 4.3, 7.6, 2.7]
        Competition.MAX_ROUNDS = 5
        run_comp = Competition(self.runners, 5, self.distances_short, self.distances_marathon)
        self.assertEqual(run_comp.rounds, 5)


    def test_init_2(self):
        """ 
        Testing invalid values and types for distance, rounds, distances_marathon and distances_short
        """
        with self.assertRaises(CustomTypeError):
            Competition("5", 3, self.distances_short, self.distances_marathon)
        
        with self.assertRaises(CustomValueError):
            Competition(self.runners, -3, self.distances_short, self.distances_marathon)
    
        with self.assertRaises(CustomTypeError):
            Competition(self.runners, 3, 5, self.distances_marathon)
        

    def test_init_3(self):
        """ 
        Testing invalid values and types for distance, rounds, distances_marathon and distances_short
        """
        with self.assertRaises(CustomTypeError):
            Competition(self.runners, 3, [0.5, '2', 1.2], self.distances_marathon)
       
        with self.assertRaises(CustomValueError):
            Competition(self.runners, 0, self.distances_short, self.distances_marathon)
    
        with self.assertRaises(CustomValueError):
            Competition(self.runners, 3, [1.5], [2.5, 16.0])


if __name__ == '__main__':
    unittest.main()
