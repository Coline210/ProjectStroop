import expyriment
import random

# Define colors
colors = {"red": (255, 0, 0), "green": (0, 255, 0), "blue": (0, 0, 255), "purple": (128, 0, 128)}

# Create the experiment
exp = expyriment.design.Experiment(name="Color Identification Stroop Task - Control Group")
expyriment.control.initialize(exp)

# Define a function to display a colored square and wait for a response
def display_square(color):
    stimulus = expyriment.stimuli.Rectangle(size=(100, 100), colour=color)
    stimulus.preload()
    stimulus.present()
    exp.clock.reset_stopwatch()
    key, rt = exp.keyboard.wait(keys=[expyriment.misc.constants.K_q, expyriment.misc.constants.K_d, expyriment.misc.constants.K_j, expyriment.misc.constants.K_l])
    return key, rt

# Define a function to display a colored word and wait for a response
def display_word(word, print_color):
    stimulus = expyriment.stimuli.TextLine(text=word, text_colour=print_color, text_size=40)
    stimulus.preload()
    stimulus.present()
    exp.clock.reset_stopwatch()
    key, rt = exp.keyboard.wait(keys=[expyriment.misc.constants.K_q, expyriment.misc.constants.K_d, expyriment.misc.constants.K_j, expyriment.misc.constants.K_l])
    return key, rt

# Prepare the experiment
expyriment.control.start()

# General instruction
general_instructions = expyriment.stimuli.TextLine(text="Welcome to the Color Identification Stroop Task. \nYou will be asked to identify the color in two different tasks. \nPlease follow the instructions for each task carefully. \nPress any key to continue.",
                                                    text_colour=(255, 255, 255), text_size=30)
general_instructions.present()
exp.keyboard.wait()

# Instructions for the first task (now Word Color Identification)
task1_instructions = expyriment.stimuli.TextLine(text="Task 1: Press the key corresponding to the color of the word displayed, not the text of the word itself. \nPress 'q' for red, 'd' for green, 'j' for blue, 'l' for purple. \nWhen you are ready, press any key to start.",
                                                 text_colour=(255, 255, 255), text_size=30)
task1_instructions.present()
exp.keyboard.wait()

# Task 1: Color Identification of the Words
words = ["red", "green", "blue", "purple"]
for i in range(1):  # 1 trial for the word color task
    random.shuffle(words)
    for word in words:
        possible_colors = [v for k, v in colors.items() if k != word]
        print_color = random.choice(possible_colors)
        key, rt = display_word(word, print_color)
        color_name = [k for k, v in colors.items() if v == print_color][0]
        print(f"Word: {word}, Color: {color_name}, Key: {key}, RT: {rt}")

# Instructions for the second task (now Square Color Identification)
task2_instructions = expyriment.stimuli.TextLine(text="Task 2: Press the key corresponding to the color of the square that appears on the screen. \nPress 'q' for red, 'd' for green, 'j' for blue, 'l' for purple. \nWhen you are ready, press any key to start.",
                                                 text_colour=(255, 255, 255), text_size=30)
task2_instructions.present()
exp.keyboard.wait()

# Task 2: Color Identification of the Square
for i in range(1):  # 1 trial for the square color task
    color_list = list(colors.values())
    random.shuffle(color_list)
    for color in color_list:
        key, rt = display_square(color)
        color_name = [k for k, v in colors.items() if v == color][0]
        print(f"Color: {color_name}, Key: {key}, RT: {rt}")

# End of the experiment
expyriment.control.end()