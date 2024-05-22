# Stroop Task Experiment 

## Overview

This repository contains two Python scripts designed to conduct a Color Identification Stroop Task using the Expyriment library. These experiments are variations of the Stroop Task, a classic psychological experiment that explores cognitive interference and the reaction time of tasks. 

### Script 1: Color Identification Stroop Task - Experimental Group

The first script (`color_identification_experimentalgroup.py`) contains two tasks for the experimental group. 

**Color Identification of Squares Task** : During this task, colored rectangles are displayed and participants have to identify the color of the rectangle. It is a simple task of color recognition to measure basic reaction times without cognitive interference. 

**Color Identification of Words Task** : The second task is a word-color interference task. It involves displaying words that are names of colors (e.g., "red", "green") in a font color that does not match the word itself (e.g., the word "red" shown in blue color). Participants are required to identify the color of the font, not the word itself, which introduces cognitive interference and tests cognitive flexibility.

The experimental group first identifies the color of squares during the first task and then the color of words during the second task. This task order tests the basic cognitive ability to dissociate the meaning of words from their visual appearance.

### Script 2: Color Identification Stroop Task - Control Group

The second script (`color_identification_controlgroup.py`) is for a control group setup. This group first identifies the color of words in a first task and then the color of squares in a second task. 

Tasks are counterbalanced between the two groups to ensure that the difference in performance between the two tasks is not due to a training effect of the previous task. 

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
3. Execute the script by typing `python script_name.py`, replacing `script_name.py` with the name of the script you want to run (`color_identification_experimentalgroup.py` or `color_identification_controlgroup.py`).
4. Follow the on-screen instructions to proceed with the experiment.

## Experiment Procedure

- **Instructions:** Each experiment starts with on-screen instructions explaining the controls to the participant. Keys used are 'q' for red, 'd' for green, 'j' for blue, 'l' for purple. The participant can learn these keys. To facilitate the learning of controls, during both tasks four colored squares are displayed as a legend in the bottom right corner indicating the colors corresponding to the keys in the same order as on the keyboard. Conditions have to remain the same during all experiments and both groups. 
- **Trials:** For the Color Identification of Words Task, one trial is one stimulus, that is to say one pair of word/printed color. In one session, accross all trials, one half of trials are congruent pairs (the word and its printed color match) and the other half of trials are incongruent pairs (the word and its printed color don't match). Each pair is used at least once per experiment session. Trials are shuffled to provide variability and prevent pattern recognition. For the Color Identification of Squares Task, a trial is one colored square. Participants respond by pressing designated keys to identify colors. For now, each script executes 24 trials for the Words Task (with 12 congruents pairs and 12 incongruent pairs for the first task) and 24 trials for the Squares Task. The total number of trials for each task can be modified in the settings at the beginning of each script. 
- **Results:** Reaction times and key presses are logged for analysis.

## Data Collection

A directory is created for each group : experimental_group/results and control_group/results. For each participant, a file is named results_tasktype_participantID is created. For instance, for the first participant of the control group, two files results_tasksquare_1.csv and results_taskswords_1.csv are created in the control_group/results directory. 
For the Color Identification of Squares Task, the color of the square, the key pressed and the reaction time are recorded in a csv file (Color, Key, RT). For the Color Identification of Words Task, the word displayed, the color of the word, the key pressed and the reaction time are recorded in a csv file (Word, Color, Key, RT). 

## Conclusion

These scripts provide a basic framework for conducting and analyzing Stroop Tasks. 


