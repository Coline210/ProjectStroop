import expyriment
import random  

# Control Block 

# Define the colors
couleurs = {"rouge": (255, 0, 0), "vert": (0, 255, 0), "bleu": (0, 0, 255), "purple": (128, 0, 128)}

# Create the experiment
exp = expyriment.design.Experiment(name="Stroop Task")
expyriment.control.initialize(exp)

# Define a function to display a stimulus and wait for a response
def afficher_stimulus(couleur):
    stimulus = expyriment.stimuli.Rectangle(size=(100, 100), colour=couleur)
    stimulus.preload()
    stimulus.present()
    exp.clock.reset_stopwatch()
    key, rt = exp.keyboard.wait(keys=[expyriment.misc.constants.K_q, expyriment.misc.constants.K_d, expyriment.misc.constants.K_j, expyriment.misc.constants.K_l])
    return key, rt

# Prepare the experiment
expyriment.control.start()

# Instruction
instructions = expyriment.stimuli.TextLine(text="Appuyez sur 'q' for red, 'd' for green, 'j' for blue, 'l' for purple", text_colour=(255, 255, 255))
instructions.present()
exp.keyboard.wait()

# Repeat the experiment 5 times
for i in range(5):
    couleurs_list = list(couleurs.values())  # Get the list of colors
    random.shuffle(couleurs_list)  # Shuffle the order of colors
    for couleur in couleurs_list:
        key, rt = afficher_stimulus(couleur)
        # Find the name of the color for the printout
        nom_couleur = [k for k, v in couleurs.items() if v == couleur][0]
        print(f"Couleur: {nom_couleur}, Touche: {key}, RT: {rt}")

# End of the experiment
expyriment.control.end()