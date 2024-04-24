# Stroop Task Experiment 

## Overview

This repository contains two Python scripts designed to conduct a Color Identification Stroop Task using the Expyriment library. These experiments are variations of the Stroop Task, a classic psychological experiment that explores cognitive interference and the reaction time of tasks. These experiments are designed to test cognitive flexibility by asking participants to identify colors under varying conditions.

### Script 1: Color Identification Stroop Task - Experimental Group

The first script (`color_identification_experimentalgroup.py`) contains two tasks for the experimental group. This group first identifies the color of squares during the first task and then the color of words during the second task. 
The first task is a simplified task of color identification of a square. It displays colored rectangles and requiring participants to identify the color of the rectangle. This version reduces linguistic interference and focuses more directly on reaction time and color recognition.
The second task is a word-color interference task. It involves displaying words that are names of colors (e.g., "red", "green") in a font color that does not match the word itself (e.g., the word "red" shown in blue color). Participants are required to identify the color of the font, not the word itself, which introduces cognitive interference and tests cognitive flexibility and attention.

Color Identification of Words: Participants are asked to press a key corresponding to the color in which a word (denoting a different color) is displayed. This task tests the Stroop effect, which measures the ease or difficulty of responding to the color of the word when it is used to spell the name of a different color.
Color Identification of Squares: Participants identify the color of a plain square. This task is generally simpler and is used to measure basic reaction times without cognitive interference.
This order tests the basic cognitive ability to dissociate the meaning of words from their visual appearance.

### Script 2: Color Identification Stroop Task - Control Group

The second script (`color_identification_controlgroup.py`) is for a control group setup. This group first identifies the color of words in a first task and then the color of squares in a second task. Tasks are counterbalanced between two groups in order to provide data on how initial tasks might influence performance on subsequent similar cognitive tasks (it ensures the difference in performance/the effect is not due to a training effect of the previous task). 

## Installation

Before running the scripts, ensure that Python and the necessary packages are installed on your system. Follow these steps to set up your environment:

1. **Install Python:**
   Ensure Python 3 is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Install Expyriment:**
   Expyriment can be installed via pip. Open your command line interface and run:

   `pip install expyriment`
   
## Running the Experiments

To run either of the Stroop Task experiments, follow these steps:

1. Open a terminal or command prompt.
2. Navigate to the directory containing the script you wish to run.
3. Execute the script by typing `python script_name.py`, replacing `script_name.py` with the name of the script you want to run (`color_identification_controlgroup.py` or `color_identification_controlgroup.py`).
4. Follow the on-screen instructions to proceed with the experiment.

## Experiment Procedure

- **Instructions:** Each experiment starts with on-screen instructions explaining the controls to the participant. Keys used are 'q' for red, 'd' for green, 'j' for blue, 'l' for purple. To prepare the experiment, the participant can only learn these keys or colored stickers can be placed on the keys to facilitate the learning of controls (the conditions just have to remain the same during all experiments and both groups). 
- **Trials:** Each script executes 5 cycles of trials where stimuli are presented in a random order. Participants respond by pressing designated keys to identify colors.
- **Results:** Reaction times and key presses are logged for analysis.

## Data Collection

The scripts print the results directly to the console, including the stimuli presented, the participant's response, and the reaction time. 

## Conclusion

These scripts provide a basic framework for conducting and analyzing Stroop Tasks. 


