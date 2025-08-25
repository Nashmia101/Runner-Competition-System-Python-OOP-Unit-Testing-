import unittest
from custom_errors import CustomValueError,CustomTypeError,CustomAttributeError
from runner import Runner

class TestRunner(unittest.TestCase):
    def test_runner_initialization(self):
        runner = Runner('Elijah', 18, 'Australia', 5.8, 4.4)
        
        # Check the initialization of attributes
        self.assertEqual(runner.name, 'Elijah')
        self.assertEqual(runner.age, 18)
        self.assertEqual(runner.country, 'Australia')
        self.assertEqual(runner.sprint_speed, 5.8)
        self.assertEqual(runner.endurance_speed, 4.4)
        self.assertEqual(runner.energy, 1000)

    def test_init1(self):
        """
        testing invaild name
        """
        with self.assertRaises(CustomTypeError):
            Runner(14, 18, 'Australia', 5.8, 4.4) 
    def test_init2(self):
        """
        Testing for invalid Age
        """
        with self.assertRaises(CustomValueError):
            Runner('Elijah', 3, 'Australia', 5.8, 4.4)
    def test_init3(self):
        """
        Testing for invalid sprint_speed
        """
        with self.assertRaises(CustomValueError):
            Runner('Elijah', 18, 'Atla', 6.8, 4.4)
    
    def test_drain_energy_1(self):
        """
        Test the drain energy method.
        """
        runner = Runner('Elijah', 18, 'Australia', 5.8, 4.4)

        runner.drain_energy(800)
        self.assertEqual(runner.energy, 200)
        runner.drain_energy(50)
        self.assertEqual(runner.energy, 150)
        runner.drain_energy(150)
        self.assertEqual(runner.energy, 0) 

    def test_drain_energy_2(self):
        """
        Test the drain energy method below 0.
        """
        runner = Runner('Elijah', 18, 'Australia', 5.8, 4.4)

        runner.drain_energy(1000)
        self.assertEqual(runner.energy, 0)
        runner.drain_energy(150)
        self.assertEqual(runner.energy, 0)

    def test_drain_energy_3 (self):
        """Tests draining energy with a value greater than max energy."""
        runner = Runner('Elijah', 18, 'Australia', 5.8, 4.4)
        with self.assertRaises(CustomValueError):
            runner.drain_energy(1500)

    def test_drain_energy_4 (self):
        """Tests draining energy with an invalid type."""
        runner = Runner('Elijah', 18, 'Australia', 5.8, 4.4)
        with self.assertRaises(CustomTypeError):
            runner.drain_energy('1500')

    def test_drain_energy_5 (self):
        """Tests draining energy with a negative value."""
        runner = Runner('Elijah', 18, 'Australia', 5.8, 4.4)
        with self.assertRaises(CustomValueError):
            runner.drain_energy(-1)

    def test_recover_energy1(self):
        """
        Test the recover energy method.
        """
        runner = Runner('Elijah', 18, 'Australia', 5.8, 4.4)
        runner.drain_energy(1000)
        runner.recover_energy(500)
        self.assertEqual(runner.energy, 500)
    
    def test_recover_energy2(self):
        """
        Test the recover energy method above max energy.
        """
        runner = Runner('Elijah', 18, 'Australia', 5.8, 4.4)
        runner.drain_energy(0)
        runner.energy = 500
        runner.recover_energy(1000)
        self.assertEqual(runner.energy, 1000)

    def test_recover_energy_3 (self):
        """Tests recovering energy with a negative value."""
        runner = Runner('Elijah', 18, 'Australia', 5.8, 4.4)
        with self.assertRaises(CustomValueError):
            runner.recover_energy(-10)

    def test_recover_energy_4 (self):
        """Tests recovering energy with a value greater than max energy."""
        runner = Runner('Elijah', 18, 'Australia', 5.8, 4.4)
        with self.assertRaises(CustomValueError):
            runner.recover_energy(2500)

    def test_recover_energy_5 (self):
        """Tests recovering energy with an invalid type."""
        runner = Runner('Elijah', 18, 'Australia', 5.8, 4.4)
        with self.assertRaises(CustomTypeError):
            runner.recover_energy('2500')

    
    def test_run_race_1(self):
        """Tests running a long race with a large distance."""
        runner = Runner('Elijah', 18, 'Australia', 3.999, 4.102)
        distance = 399.95
        race_type = 'long'
        calculation = ((distance*1000)/runner.endurance_speed) #calculating expected distance
        expected_value=round(calculation,2)# round off
        self.assertEqual(runner.run_race(race_type, distance), expected_value)
    
    def test_run_race_2(self):
        """Tests running a short race with a large distance."""
        runner = Runner('Elijah', 18, 'Australia', 6.0, 4.102)
        distance = 999.045
        race_type = 'short'
        calculation = ((distance*1000)/runner.sprint_speed) # calculating expected distance
        expected_value=round(calculation,2) # round off
        self.assertEqual(runner.run_race(race_type, distance), expected_value)

    def test_run_race_3(self):
        """Tests running a long race with a very large distance."""
        runner = Runner('Elijah', 18, 'Australia', 3.999, 1.8992)
        distance = 2099.996
        race_type = 'long'
        calculation = ((distance*1000)/runner.endurance_speed) # calculating expected distance
        expected_value=round(calculation,2) # round off
        self.assertEqual(runner.run_race(race_type, distance), expected_value)

    def test_run_race_4 (self):
        """Tests running a race with a negative distance."""
        runner = Runner('Elijah', 18, 'Australia', 5.8, 4.4)
        with self.assertRaises(CustomValueError):
            runner.run_race('short',-1.0)

    def test_run_race_5 (self):
        """Tests running a race with an invalid distance type."""
        runner = Runner('Elijah', 18, 'Australia', 5.8, 4.4)
        with self.assertRaises(CustomTypeError):
            runner.run_race('short',1)

    def test_run_race_7 (self):
        """Tests running a race_type with an invalid value."""
        runner = Runner('Elijah', 18, 'Australia', 5.8, 4.4)
        with self.assertRaises(CustomValueError):
            runner.run_race('huge',1.0)







    
    
       
if __name__ == '__main__':
    unittest.main()

