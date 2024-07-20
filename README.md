# Calculator_Tkinter

This project is a simple yet functional calculator built using Python's Tkinter library for the GUI and the Pillow library for handling images. It features basic arithmetic operations, including addition, subtraction, multiplication, division, and modulus operations, along with additional functionality for clearing input and undoing the last entry.
## Features

  > Basic Arithmetic Operations: Perform addition, subtraction, multiplication, division, and modulus operations.
   > Undo Functionality: Remove the last entered character with the undo button.
   > Clear Functionality: Clear all input using the AC (All Clear) button.
   > Responsive GUI: The application has a modern look with a dark theme, featuring well-spaced and easy-to-read buttons and display labels.
   > Error Handling: Provides appropriate feedback for invalid inputs and division by zero errors.

## How to Use

   > Start the Application: Run the Starter_Code function to launch the calculator application.
   > Enter Numbers and Operations: Use the numeric and operator buttons to input your calculation.
   > Clear Input: Press the AC button to clear all input.
   > Undo Entry: Use the undo button (represented by an image) to remove the last entered character.
   > Get Result: Press the equal (=) button to display the calculation result.

## Code Overview
### Main Function

  Starter_Code(): Initializes the main window, sets its properties, and starts the Tkinter main loop.

### Calculation Functions

   calculate(no): Evaluates the mathematical expression provided in the string no. Handles replacement of custom operators (like 'x' for multiplication) with standard Python operators.
    Calculations(label, no, Answer, operator): Manages the input and calculation process, updating the display labels accordingly.

### GUI Widgets

  widgets(window, photo): Creates and places all the buttons and labels on the main window, configuring their properties and positioning.

## Dependencies

   > Tkinter: Built-in Python library for creating graphical user interfaces.
   > Pillow: Python Imaging Library (PIL) fork, required for handling the image used in the undo button.
