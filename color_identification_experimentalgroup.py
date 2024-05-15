import expyriment
import random
import csv
import os

# Configuration and settings
colors = {"red": (255, 0, 0), "green": (0, 255, 0), "blue": (0, 0, 255), "purple": (128, 0, 128)}
total_trials = 24  # Define the total number of trials for each task

# Create the experiment
exp = expyriment.design.Experiment(name="Color Identification Stroop Task - Experimental Group")
expyriment.control.initialize(exp)

def display_square(color):
    """Displays a colored square and waits for a response."""
    stimulus = expyriment.stimuli.Rectangle(size=(100, 100), colour=color)
    stimulus.preload()
    stimulus.present()
    exp.clock.reset_stopwatch()
    key, rt = exp.keyboard.wait(keys=[expyriment.misc.constants.K_q, expyriment.misc.constants.K_d, expyriment.misc.constants.K_j, expyriment.misc.constants.K_l])
    return key, rt

def display_word(word, print_color):
    """Displays a word in a color and waits for a response."""
    stimulus = expyriment.stimuli.TextLine(text=word, text_colour=print_color, text_size=40)
    stimulus.preload()
    stimulus.present()
    exp.clock.reset_stopwatch()
    key, rt = exp.keyboard.wait(keys=[expyriment.misc.constants.K_q, expyriment.misc.constants.K_d, expyriment.misc.constants.K_j, expyriment.misc.constants.K_l])
    return key, rt

def save_results_squares(results, task, participant_id, group="experimental_group"):
    """Saves the results of Task Squares to a CSV file."""
    directory = os.path.join(group, "results")
    os.makedirs(directory, exist_ok=True)
    results_path = os.path.join(directory, f"results_task{task}_{participant_id}.csv")
 
    with open(results_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Color", "Key", "RT"])
        writer.writerows(results)
    
    print(f"Results saved to: {results_path}")

def save_results_words(results, task, participant_id, group="experimental_group"):
    """Saves the results of Task Words to a CSV file."""
    directory = os.path.join(group, "results")
    os.makedirs(directory, exist_ok=True)
    results_path = os.path.join(directory, f"results_task{task}_{participant_id}.csv")
 
    with open(results_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Word", "Color", "Key", "RT"])
        writer.writerows(results)
    
    print(f"Results saved to: {results_path}")

# Prepare congruent and incongruent pairs
congruent_pairs = [(word, colors[word]) for word in colors]
incongruent_pairs = [(word, color) for word in colors for color in colors.values() if color != colors[word]]
random.shuffle(incongruent_pairs) 

# Select exactly half congruent and half incongruent for the given number of trials
half_trials = total_trials // 2
selected_congruent = congruent_pairs * (half_trials // len(congruent_pairs)) + congruent_pairs[:half_trials % len(congruent_pairs)]
selected_incongruent = incongruent_pairs[:half_trials]

# Combine and shuffle the selected pairs for all trials
trials_pairs = selected_congruent + selected_incongruent
random.shuffle(trials_pairs)

# Prepare the experiment
expyriment.control.start()

# Use subject number as participant ID
participant_id = exp.subject

# General instructions 
general_instructions = expyriment.stimuli.TextBox(
    text="Welcome to the Color Identification Stroop Task.\nYou will be asked to identify the color in two different tasks.\nPlease follow the instructions for each task carefully.\nPress any key to continue.",
    size=(700, 200), position=None, text_size=24, text_colour=(255, 255, 255), background_colour=(0, 0, 0))
general_instructions.present()
exp.keyboard.wait()

# Instructions for the first task 
tasksquares_instructions = expyriment.stimuli.TextBox(
    text="Task 1: Press the key corresponding to the color of the square that appears on the screen.\nPress 'q' for red, 'd' for green, 'j' for blue, 'l' for purple.\nWhen you are ready, press any key to start.",
    size=(700, 200), position=None, text_size=24, text_colour=(255, 255, 255), background_colour=(0, 0, 0))
tasksquares_instructions.present()
exp.keyboard.wait()

# Task 1: Color Identification of the Square
results_tasksquares = []
color_list = list(colors.values()) * (total_trials // len(colors)) + list(colors.values())[:total_trials % len(colors)]
random.shuffle(color_list)
for color in color_list:
    key, rt = display_square(color)
    color_name = [k for k, v in colors.items() if v == color][0]
    results_tasksquares.append([color_name, key, rt])

# Save results of Task 1
save_results_squares(results_tasksquares, 'squares', participant_id)

# Instructions for the second task 
taskwords_instructions = expyriment.stimuli.TextBox(
    text="Task 2: Press the key corresponding to the color of the word displayed, not the text of the word itself.\nPress 'q' for red, 'd' for green, 'j' for blue, 'l' for purple.\nWhen you are ready, press any key to start.",
    size=(700, 200), position=None, text_size=24, text_colour=(255, 255, 255), background_colour=(0, 0, 0))
taskwords_instructions.present()
exp.keyboard.wait()

# Task 2: Color Identification of the Words
results_taskwords = []
for word, color in trials_pairs:
        key, rt = display_word(word, color)
        color_name = [k for k, v in colors.items() if v == color][0]
        results_taskwords.append([word, color_name, key, rt])

# Save results of Task 2
save_results_words(results_taskwords, 'words', participant_id)

# End of the experiment
expyriment.control.end()