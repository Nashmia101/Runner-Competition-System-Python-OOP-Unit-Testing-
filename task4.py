from competition import Competition
from runner import Runner
from custom_errors import CustomTypeError, CustomValueError, CustomAttributeError
from race import Race, ShortRace, MarathonRace


def create_runner(runner_name: str, runner_age: str, runner_country: str, sprint_speed: str, endurance_speed: str)-> Runner:
    """
    Create a runner object.
    Changes to the appropriate type
    Args:
    runner_name (str): The name of the runner.
    runner_age (str): The age of the runner.
    runner_country (str): The country of the runner.
    sprint_speed (str): The sprint speed of the runner.
    endurance_speed (str): The endurance speed of the runner.
    
    Returns:
    Runner: Runner object.
    """
    try:
        # Try to convert input values to appropriate types unless an error is raised
        runner_name=str(runner_name)
        runner_age=int(runner_age)
        sprint_speed=float(sprint_speed)
        endurance_speed=float(endurance_speed)
        # Create and return the Runner object
        return Runner(runner_name.strip(), runner_age, runner_country.strip(), sprint_speed, endurance_speed)
    # give exception when an error of any kind is raised
    except (CustomTypeError, CustomValueError,ValueError) as e:
        print(f"Error creating runner: {e}")

def create_competition(runners: list, rounds: str, distances_short: list, distances_long: list)-> Competition:
    """
    Creates a competition object.
    changes to the appropriate type
    
    Args:
    runners (list): List of Runner objects participating in the competition.
    rounds (str): Number of rounds in the competition.
    distances_short (list): List of distances for short races.
    distances_long (list): List of distances for long races.
    
    Returns:
    Competition: Competition object.
    """
    try:
        # Try to convert input values to appropriate types unless an error is raised
        rounds=int(rounds)
        for i in range(len(distances_short)):
            distances_short[i]=float(distances_short[i]) # converting every single given distance into float
        for i in range(len(distances_long)):
            distances_long[i]=float(distances_long[i])
        # Create and return the Competition object
        return Competition(runners, rounds, distances_short, distances_long)
    # give exception when an error of any kind is raised
    except (CustomTypeError, CustomValueError,ValueError) as e:
        print(f"Error creating competition: {e}")
    

def runner_information()-> list:
    """
    takes information about runners from user's given input.
    Returns:
    list: List of Runner objects.
    """
    runners = []
    while True: # run loop until user decides to quit 
        runner_info=input("Enter the runner's information like name,age,country,sprint speed and endurance speed please make sure that the entry is seperated by backlash or if you want to quit please enter 'q'")
        if runner_info.lower()=='q': # if user has entered q it means they want to quit adding runners
            break
        else:
            runner_length=len(runner_info.split('/')) #split the input for different fields for length
            if runner_length==5: # check if number of entered fields meets the given brief
                runner_name, runner_age, runner_country, sprint_speed, endurance_speed=runner_info.split('/')#split the input for different fields
                runner=create_runner(runner_name, runner_age, runner_country, sprint_speed, endurance_speed) #call create_runner function
                runners.append(runner)  # append runner into runners list 
            else:
                print("ERROR : Incorrect number of fields: Please enter all the fields") # gives error when there are incorrect number of fields
    return runners

def competition_information(runners)-> Competition:
    """
    takes information about the competition from user's given input.
    
    Args:
    runners (list): List of Runner objects.
    
    Returns:
    Competition: The Competition object created with information.
    """
    # takes input from user regarding competition details
    comp_info=input("Enter the competition information like no of rounds,distances for short races and distances for long races, please make sure that entries are seperated by backlash and distances are seperated by comma")
    comp_length=len(comp_info.split('/')) 
    if comp_length==3: # checks if the number of fields meets the given brief
        rounds, distances_short, distances_long = comp_info.split('/') #split the input for different fields
        distances_short=distances_short.split(',') # splits the distances by comma
        distances_short=list(distances_short)     # create list of distances
        distances_long= distances_long.split(',')
        distances_long=list(distances_long)
        competition_info=create_competition(runners,rounds, distances_short, distances_long) #call create_competition function 
    else:
        print("ERROR : Incorrect number of fields:Please enter all the fields") # give error if there are incorrect number of fields
    return competition_info

def main():
        runners=runner_information() # call runner_information function 
        if len(runners)==0: #if no runners are provided then program will end as there will be no competition
            print("No runners provided so no competition will take place.")
            exit()
        while True: 
            try:
                comp=competition_information(runners) # calling competition_information
                comp.conduct_competition() #conducting competition
                comp.print_leaderboard() # print final leaderboard
                break # break the loop if the competition has been runned successfully 
            except (AttributeError) as e: # give exception if an error occurs 
                continue # repeat the loop if an error occurs so that user enters competition details again

if __name__ == '__main__':
    main()

