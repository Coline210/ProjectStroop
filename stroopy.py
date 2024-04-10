import expyriment
import random  

# Définir les couleurs et les mots
couleurs = {"rouge": (255, 0, 0), "vert": (0, 255, 0), "bleu": (0, 0, 255)}
mots = ["rouge", "vert", "bleu"]

# Créer l'expérience
exp = expyriment.design.Experiment(name="Stroop Task")
expyriment.control.initialize(exp)

# Définir une fonction pour afficher un stimulus et attendre une réponse
def afficher_stimulus(mot, couleur_impression):
    stimulus = expyriment.stimuli.TextLine(text=mot, text_colour=couleur_impression)
    stimulus.preload()
    stimulus.present()
    exp.clock.reset_stopwatch()
    key, rt = exp.keyboard.wait(keys=[expyriment.misc.constants.K_r, expyriment.misc.constants.K_g, expyriment.misc.constants.K_b])
    return key, rt

# Préparer l'expérience
expyriment.control.start()

# Instruction
instructions = expyriment.stimuli.TextLine(text="Appuyez sur 'r' for red, 'g' for green, 'b' for blue", text_colour=(255, 255, 255))
instructions.present()
exp.keyboard.wait()

random.shuffle(mots)  # Mélange l'ordre des mots
for mot in mots:
    couleurs_possibles = [v for k, v in couleurs.items() if k != mot]  # Exclut la couleur correspondant au mot
    couleur_impression = random.choice(couleurs_possibles)  # Sélectionne une couleur aléatoire parmi les couleurs possibles
    key, rt = afficher_stimulus(mot, couleur_impression)
    # Trouver le nom de la couleur pour l'impression
    nom_couleur = [k for k, v in couleurs.items() if v == couleur_impression][0]
    print(f"Mot: {mot}, Couleur: {nom_couleur}, Touche: {key}, RT: {rt}")

# Fin de l'expérience
expyriment.control.end()
