# Stroop Task Experiment 

## Overview

This repository contains two Python scripts designed to conduct variations of the Stroop Task, a classic psychological experiment that explores cognitive interference and the reaction time of tasks. Both scripts are implemented using the Expyriment library, a Python library for cognitive and neuroscientific experiments.

### Script 1: Word-Color Interference Stroop Task

The first script (`word_color_stroop.py`) involves displaying words that are names of colors (e.g., "red", "green") in a font color that does not match the word itself (e.g., the word "red" shown in blue color). Participants are required to identify the color of the font, not the word itself, which introduces cognitive interference and tests cognitive flexibility and attention.

### Script 2: Color Identification Stroop Task

The second script (`color_identification_stroop.py`) simplifies the task by displaying colored rectangles and requiring participants to identify the color of the rectangle. This version reduces linguistic interference and focuses more directly on reaction time and color recognition.

## Installation

Before running the scripts, ensure that Python and the necessary packages are installed on your system. Follow these steps to set up your environment:

1. **Install Python:**
   Ensure Python 3 is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Install Expyriment:**
   Expyriment can be installed via pip. Open your command line interface and run:

   `pip install expyriment`
   
## Usage

To run either of the Stroop Task experiments, follow these steps:

1. Open a terminal or command prompt.
2. Navigate to the directory containing the script you wish to run.
3. Execute the script by typing `python script_name.py`, replacing `script_name.py` with the name of the script you want to run (`word_color_stroop.py` or `color_identification_stroop.py`).
4. Follow the on-screen instructions to proceed with the experiment.

## Experiment Procedure

- **Instructions:** Each experiment starts with on-screen instructions explaining the controls to the participant.
- **Trials:** Each script executes 5 cycles of trials where stimuli are presented in a random order. Participants respond by pressing designated keys to identify colors.
- **Results:** Reaction times and key presses are logged for analysis.

## Data Collection

The scripts print the results directly to the console, including the stimuli presented, the participant's response, and the reaction time. 

## Conclusion

These scripts provide a basic framework for conducting and analyzing Stroop Tasks. 


