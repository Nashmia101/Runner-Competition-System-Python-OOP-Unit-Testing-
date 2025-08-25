# Runner-Competition-System-Python-OOP-Unit-Testing-
Python OOP system simulating multi-round runner competitions. Includes runners, short &amp; marathon races, energy management, and leaderboards. Features robust error handling and extensive unit testing.
Runner Competition System
Overview

This project implements a runner competition simulation using Python and Object-Oriented Programming (OOP). It models runners, races (short and marathon), and competitions with multiple rounds. The system validates inputs through custom error handling, simulates races based on speed and energy constraints, and maintains a dynamic leaderboard. Comprehensive unit tests ensure robustness and correctness.

Key Features

Runner Class: Models attributes like age, country, sprint speed, endurance speed, and energy (runner.py).

Race Classes: Abstract base class with ShortRace and MarathonRace specializations (race.py).

Competition Class: Handles multi-round competitions, conducts races, updates leaderboards (competition.py).

Custom Error Handling: Strong validation using custom exceptions (custom_errors.py).

Energy Management: Draining and recovery mechanics during races.

Leaderboard: Dynamic updates based on race results with ordinal ranking.

Command-line Input: Users can enter runner and competition details interactively (task4.py).

Unit Testing: Extensive tests for runner, race, and competition logic (test_runner.py, test_race.py, test_competition.py).

Tools & Techniques

Python (OOP, typing, abc)

Custom Exceptions for error handling

CSV Integration for validating runner countries

Unit Testing (unittest)

Author

Nashmia Shakeel
