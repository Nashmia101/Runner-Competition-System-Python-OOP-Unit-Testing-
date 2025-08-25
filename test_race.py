import unittest
from custom_errors import CustomValueError,CustomTypeError, RunnerAlreadyExistsError, RunnerDoesntExistError,RaceIsFullError
from race import Race, ShortRace, MarathonRace
from runner import Runner
import math

class TestRaces(unittest.TestCase):

    def test_init(self):
        # Test successful initialization for short race
        short_race = ShortRace(0.5, [])
        self.assertEqual(short_race.race_type, 'short')
        self.assertEqual(short_race.distance, 0.5)
        self.assertEqual(short_race.runners, [])
        self.assertEqual(short_race.maximum_participants, 8)
        self.assertEqual(short_race.time_multiplier, 1.2)
        
        # Test successful initialization for marathon
        marathon_race = MarathonRace(42.0, [])
        self.assertEqual(marathon_race.race_type, 'long')
        self.assertEqual(marathon_race.distance, 42)
        self.assertEqual(marathon_race.runners, [])
        self.assertEqual(marathon_race.maximum_participants, 16)
        self.assertEqual(marathon_race.energy_per_km, 100)
    
    def test_add_runner(self):
        # Create a short race and a runner
        short_race = ShortRace(0.5, [])
        runner = Runner('Lauren', 20, 'Australia', 2.4, 2.4)
        
        # Test adding a new runner
        short_race.add_runner(runner)
        self.assertIn(runner, short_race.runners)
        
        # Test exceeding maximum participants
        for i in range(short_race.maximum_participants - 1):
            short_race.add_runner(Runner(f'Runner {i}', 10, 'Azerbaijan', 3.2, 2.2))
    
    def test_remove_runner(self):
        # Create a short race and a runner
        short_race = ShortRace(5.0, [])
        runner = Runner('Yaakov', 20, 'Switzerland', 2.4, 2.4)
        short_race.add_runner(runner)
        
        # Test removing an existing runner
        short_race.remove_runner(runner)
        self.assertNotIn(runner, short_race.runners)
    
    def test_conduct_race_short(self):
        # Create a short race and runners
        short_race = ShortRace(5.0, [])
        runner1 = Runner('John', 10, 'Australia', 2.8, 2.8)
        runner2 = Runner('Jane', 12, 'Australia', 4.2, 4.5)
        short_race.add_runner(runner1)
        short_race.add_runner(runner2)
        
        # Conduct the race and get the results
        results = short_race.conduct_race()
        
        # Check the results
        self.assertIsInstance(results, list, f"Results returned from short race's conduct race should be a list")
        list_of_racer_names = [x.name for x in [y[0] for y in results]]
        self.assertIn("John", list_of_racer_names, f"Runner John expected in results but not found")
        self.assertIn("Jane", list_of_racer_names, f"Runner Jane expected in results but not found")
        
    def test_conduct_race_marathon(self):
        # Create a marathon race and runners
        marathon = MarathonRace(42.0, [])
        runner1 = Runner('John', 10, 'Australia', 2.8, 2.8)
        runner2 = Runner('Jane', 12, 'Australia', 3.2, 5.2)
        marathon.add_runner(runner1)
        marathon.add_runner(runner2)
        
        # Conduct the race and get the results
        results = marathon.conduct_race()
        
        # Check the results
        self.assertIsInstance(results, list, f"Results returned from short race's conduct race should be a list")
        list_of_racer_names = [x.name for x in [y[0] for y in results]]
        self.assertIn("John", list_of_racer_names, f"Runner John expected in results but not found")
        self.assertIn("Jane", list_of_racer_names, f"Runner Jane expected in results but not found")
    
    def test_dnf_handling(self):
        # Create a marathon race and runners
        marathon = MarathonRace(42.0, [])
        runner1 = Runner('John', 10, 'Australia', 2.8, 2.8)
        runner2 = Runner('Jane', 12, 'Australia', 4.2, 4.5)
        marathon.add_runner(runner1)
        marathon.add_runner(runner2)
        
        # Conduct the race and get the results
        results = marathon.conduct_race()
        
        # Both runners should run out of energy and get 'DNF'
        self.assertIsInstance(results, list, f"Results returned from short race's conduct race should be a list")
        list_of_racer_times = [y[1] for y in results]
        self.assertIn("DNF", list_of_racer_times, f"Runner John should DNF but didn't")

    def test_shortRace_class_1(self):
        """
        Test the initialization of a ShortRace instance with default parameters.
        """
        short_race = ShortRace(4.5, None)
        self.assertEqual(short_race.race_type, 'short')
        self.assertEqual(short_race.distance, 4.5)
        self.assertEqual(short_race.runners, [])
        self.assertEqual(short_race.maximum_participants, 8)
        self.assertEqual(short_race.time_multiplier, 1.2)

    def test_longRace_class_2(self):
        """
        Test the initialization of a MarathonRace instance with default parameters.
        """
        Marathon_race = MarathonRace(220.98, None)
        self.assertEqual(Marathon_race.race_type, 'long')
        self.assertEqual(Marathon_race.distance, 220.98)
        self.assertEqual(Marathon_race.runners, [])
        self.assertEqual(Marathon_race.maximum_participants, 16)
        self.assertEqual(Marathon_race.energy_per_km, 100)

    def test_longRace_class_3(self):
        """
        Test the initialization of a MarathonRace instance with a list of runners.
        """
        eli = Runner('Elijah', 18, 'Australia', 5.8, 4.4)
        rup = Runner('Rupert', 23, 'Australia', 2.3, 1.9)
        Marathon_race = MarathonRace(1056.45,[eli,rup])
        self.assertEqual(Marathon_race.race_type, 'long')
        self.assertEqual(Marathon_race.distance, 1056.45)
        self.assertEqual(Marathon_race.runners,[eli,rup])
        self.assertEqual(Marathon_race.maximum_participants, 16)
        self.assertEqual(Marathon_race.energy_per_km, 100)

    def test_shortRace_class_4(self):
        """
        Test the initialization of a ShortRace instance with a list of runners.
        """
        eli = Runner('Elijah', 18, 'Australia', 5.8, 4.4)
        rup = Runner('Rupert', 23, 'Canada', 2.3, 1.9)
        cha = Runner('Charli', 33, 'France', 3.5, 5.3)
        pet = Runner('Peter', 27, 'Aruba', 4.2, 3.4)
        short_race = ShortRace(554.7,[eli,rup,pet,cha])
        self.assertEqual(short_race.race_type, 'short')
        self.assertEqual(short_race.distance, 554.7)
        self.assertEqual(short_race.runners,[eli,rup,pet,cha])
        self.assertEqual(short_race.maximum_participants, 8)
        self.assertEqual(short_race.time_multiplier, 1.2)

    def test_shortRace_class_5(self):
        """
        Test the initialization of a ShortRace instance with an empty list of runners.
        """
        short_race = ShortRace(0.78,[])
        self.assertEqual(short_race.race_type, 'short')
        self.assertEqual(short_race.distance, 0.78)
        self.assertEqual(short_race.runners,[])
        self.assertEqual(short_race.maximum_participants, 8)
        self.assertEqual(short_race.time_multiplier, 1.2)

    def test_shortRace_class_6(self):
        """
        Test the initialization of a MarathonRace instance with an empty list of runners and zero distance.
        """
        Marathon_race = MarathonRace(0.8,[])
        self.assertEqual(Marathon_race.race_type, 'long')
        self.assertEqual(Marathon_race.distance, 0.8)
        self.assertEqual(Marathon_race.runners,[])
        self.assertEqual(Marathon_race.maximum_participants, 16)
        self.assertEqual(Marathon_race.energy_per_km, 100)
        
    def test_add_runner_1(self):
        """
        Test adding a new runner to a MarathonRace.
        """
        eli = Runner('Elijah', 18, 'Australia', 5.8, 4.4)
        rup = Runner('Rupert', 23, 'Canada', 2.3, 1.9)
        Marathon_race = MarathonRace(3.45, [eli,rup])
        runner = Runner('Charli', 53, 'Chile', 3.7, 1.9)
        Marathon_race.add_runner(runner)
        self.assertIn(runner, Marathon_race.runners)

    
    def test_add_runner_2(self):
        """
        Test adding a duplicate runner to a ShortRace.
        """
        short_race = ShortRace(0.5, [])
        runner = Runner('Lauren', 20, 'Australia', 2.4, 2.4)
        short_race.add_runner(runner)
        with self.assertRaises(RunnerAlreadyExistsError):
            short_race.add_runner(runner)

    def test_add_runner_3(self):
        """
        Test adding a runner to a full ShortRace.
        """
        short_race = ShortRace(0.5, [])
        for i in range(short_race.maximum_participants):
            short_race.add_runner(Runner(f'Runner {i}', 10, 'Azerbaijan', 3.2, 2.2))
        new_runner = Runner('Peter', 25, 'Aruba', 3.3, 4.1)
        with self.assertRaises(RaceIsFullError):
             short_race.add_runner(new_runner)
            
    def test_add_runner_4(self):
        """
        Test adding a runner to a ShortRace that is already full.
        """
        runners=[Runner('Elijah', 18, 'Australia', 5.8, 4.4)]
        Marathon_race = ShortRace(0.5, runners)
        for i in range(len(runners),Marathon_race.maximum_participants):
            Marathon_race.add_runner(Runner(f'Runner {i}', 10, 'Azerbaijan', 3.2, 2.2))
        new_runner = Runner('Peter', 25, 'Aruba', 3.3, 4.1)
        with self.assertRaises(RaceIsFullError):
             Marathon_race.add_runner(new_runner)

    def test_remove_runner_1(self):
        """
        Test removing a runner from a ShortRace.
        """
        short_race = ShortRace(42.5, [])
        eli = Runner('Elijah', 18, 'Australia', 5.8, 4.4)
        short_race.add_runner(eli)
        short_race.remove_runner(eli)
        self.assertEqual(len(short_race.runners), 0)

    def test_remove_runner_2(self):
        """
        Test removing multiple runners from a MarathonRace.
        """
        Marathon_race = MarathonRace(1.5, [])
        lau = Runner('Lauren', 20, 'Australia', 2.4, 2.9)
        eli = Runner('Elijah', 26, 'Canada', 4.5, 3.0)
        pet = Runner('Petter', 78, 'Aruba', 4.9, 5.4)
        Marathon_race.add_runner(lau)
        Marathon_race.add_runner(eli)
        Marathon_race.add_runner(pet)

        Marathon_race.remove_runner(lau)
        Marathon_race.remove_runner(eli)
        self.assertEqual(len(Marathon_race.runners), 1)

    def test_remove_runner_3(self):
        """
        Test removing a runner from an empty MarathonRace.
        """
        Marathon_race = MarathonRace(322.90, [])
        eli = Runner('Elijah', 22, 'Australia', 2.6, 4.2)
        with self.assertRaises(RunnerDoesntExistError):
            Marathon_race.remove_runner(eli)

    def test_remove_runner_4(self):
        """
        Test removing a non-existent runner from a ShortRace.
        """
        short_race = ShortRace(45.78, [])
        rup = Runner('Rupert', 20, 'Canada', 3.1, 5.1)
        with self.assertRaises(RunnerDoesntExistError):
            short_race.remove_runner(rup)

    def test_short_race_conduct_1(self):
        """
        Test conducting a ShortRace and verifying results.
        """
        short_race=ShortRace(250.78,[])
        eli = Runner('Elijah', 18, 'Australia', 5.8, 4.4)
        rup = Runner('Rupert', 23, 'Australia', 2.3, 1.9)
        short_race.add_runner(eli) # adding runners
        short_race.add_runner(rup)
        results = short_race.conduct_race() # calling the short race
        expected_result_1=(eli.run_race('short',250.78)*(short_race.time_multiplier))
        expected_result_2=(rup.run_race('short',250.78)*(short_race.time_multiplier)) # calculating expected results
        self.assertEqual(results[0][1], expected_result_1)
        self.assertEqual(results[1][1], expected_result_2) # checking if the results match 

    def test_short_race_conduct_2(self):
        """
        Test conducting a ShortRace with multiple runners and verifying results.
        """
        short_race=ShortRace(999.98,[])
        eli = Runner('Elijah', 18, 'Australia', 5.8, 4.4)
        rup = Runner('Rupert', 23, 'Australia', 2.3, 1.9)
        pet = Runner('Peter', 54, 'Aruba', 4.7, 5.4)
        lau = Runner('Lauren', 67, 'Chile', 2.2, 4.8)
        short_race.add_runner(eli)
        short_race.add_runner(rup)
        short_race.add_runner(pet) # adding runners
        short_race.add_runner(lau)
        results = short_race.conduct_race() # calling short race
        expected_result_1=(eli.run_race('short',999.98)*(short_race.time_multiplier))
        expected_result_2=(rup.run_race('short',999.98)*(short_race.time_multiplier))  # calculating expected results
        expected_result_3=(pet.run_race('short',999.98)*(short_race.time_multiplier))
        expected_result_4=(lau.run_race('short',999.98)*(short_race.time_multiplier))
        self.assertEqual(results[0][1], expected_result_1) # checking if the results match 
        self.assertEqual(results[1][1], expected_result_2)
        self.assertEqual(results[2][1], expected_result_3)
        self.assertEqual(results[3][1], expected_result_4)

    def test_short_race_conduct_3(self):
        """
        Test conducting a ShortRace with no runners.
        """
        short_race = ShortRace(2.5, [])
        results = short_race.conduct_race()
        self.assertEqual(results, [])

    def test_long_race_conduct_1(self):
        """
        Test conducting a MarathonRace and verifying results.
        """
        long_race=MarathonRace(7.5,[])
        eli = Runner('Elijah', 18, 'Australia', 5.4, 4.0)
        rup = Runner('Rupert', 23, 'Aruba', 2.5, 3.0)
        long_race.add_runner(eli)
        long_race.add_runner(rup) # adding runners
        results = long_race.conduct_race() # calling long race
        result_1=(eli.run_race('long',7.5)) # calculating expected results
        result_2=(rup.run_race('long',7.5))
        num_1=0
        num_2=0
        for i in range(math.ceil(7.5)): # adding results for each kilometer
            num_1=result_1+num_1
            num_2=result_2+num_2
        self.assertEqual(results[0][1], num_1) # checking if results match 
        self.assertEqual(results[1][1], num_2)

    def test_long_race_conduct_2(self):
        """
        Test conducting a MarathonRace with multiple runners and verifying results.
        """
        long_race=MarathonRace(9.23,[])
        eli = Runner('Elijah', 18, 'Australia', 5.4, 4.0)
        rup = Runner('Rupert', 23, 'Aruba', 2.5, 3.0)
        pet = Runner('Peter', 54, 'Canada', 3.8, 4.1)
        lau = Runner('Lauren', 67, 'Chile', 3.2, 4.3)
        long_race.add_runner(eli)
        long_race.add_runner(rup)
        long_race.add_runner(pet) # adding runners
        long_race.add_runner(lau)
        results = long_race.conduct_race() # calling the long race
        result_1=(eli.run_race('long',9.23))
        result_2=(rup.run_race('long',9.23))
        result_3=(pet.run_race('long',9.23))  # calculating  expected results
        result_4=(lau.run_race('long',9.23)) 
        num_1=0
        num_2=0
        num_3=0
        num_4=0
        for i in range(math.ceil(9.23)):
            num_1=result_1+num_1
            num_2=result_2+num_2      # results of all kilometers together
            num_3=result_3+num_3
            num_4=result_4+num_4
        self.assertEqual(results[0][1], num_1)
        self.assertEqual(results[1][1], num_2)
        self.assertEqual(results[2][1], num_3) # checking if the results match 
        self.assertEqual(results[3][1], num_4)

    def test_long_race_conduct_3(self):
        """
        Test conducting a MarathonRace with no runners.
        """
        long_race = MarathonRace(23.0, [])
        results = long_race.conduct_race()
        self.assertEqual(len(results), 0)

    def test_long_race_conduct_4(self):
        """
        Test conducting a MarathonRace where all runners fail to finish.
        """
        long_race=MarathonRace(36.2,[])
        eli = Runner('Elijah', 18, 'Australia', 2.4, 4.1)
        rup = Runner('Rupert', 23, 'Aruba', 5.2, 3.4)
        lau = Runner('lauren', 36, 'United States', 3.9, 2.7)
        long_race.add_runner(eli)
        long_race.add_runner(rup) # adding runner
        long_race.add_runner(lau)
        results = long_race.conduct_race() # calling the marathon race
        result_1=(eli.run_race('long',36.2))
        result_2=(rup.run_race('long',36.2)) # calculating results
        result_3=(lau.run_race('long',36.2))
        self.assertEqual(results[0][1],'DNF')
        self.assertEqual(results[1][1],'DNF') # checking if results match 
        self.assertEqual(results[2][1],'DNF')

    def test_init1(self):
        """
        Testing if customType error is raised if distance is not a float
        """
        with self.assertRaises(CustomTypeError):
            short_race = ShortRace(9, [])
    def test_init2(self):
        """
        Testing if customValue error is raised if distance is negative value
        """
        with self.assertRaises(CustomValueError):
            short_race = ShortRace(-1.0, [])
    def test_init3(self):
        """
        Testing if customtype error is raised if runners is not list or none
        """
        with self.assertRaises(CustomTypeError):
            short_race = ShortRace(2.5, '9')

    
if __name__ == '__main__':
    unittest.main()

