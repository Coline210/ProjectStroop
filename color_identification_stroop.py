import expyriment
import random

# Définir les couleurs
couleurs = {"rouge": (255, 0, 0), "vert": (0, 255, 0), "bleu": (0, 0, 255), "purple": (128, 0, 128)}

# Créer l'expérience
exp = expyriment.design.Experiment(name="Stroop Task Combined")
expyriment.control.initialize(exp)

# Définir une fonction pour afficher un carré de couleur et attendre une réponse
def afficher_carré(couleur):
    stimulus = expyriment.stimuli.Rectangle(size=(100, 100), colour=couleur)
    stimulus.preload()
    stimulus.present()
    exp.clock.reset_stopwatch()
    key, rt = exp.keyboard.wait(keys=[expyriment.misc.constants.K_q, expyriment.misc.constants.K_d, expyriment.misc.constants.K_j, expyriment.misc.constants.K_l])
    return key, rt

# Définir une fonction pour afficher un mot coloré et attendre une réponse
def afficher_mot(mot, couleur_impression):
    stimulus = expyriment.stimuli.TextLine(text=mot, text_colour=couleur_impression)
    stimulus.preload()
    stimulus.present()
    exp.clock.reset_stopwatch()
    key, rt = exp.keyboard.wait(keys=[expyriment.misc.constants.K_q, expyriment.misc.constants.K_d, expyriment.misc.constants.K_j, expyriment.misc.constants.K_l])
    return key, rt

# Préparer l'expérience
expyriment.control.start()

# Instruction générale
instructions = expyriment.stimuli.TextLine(text="Appuyez sur 'q' pour rouge, 'd' pour vert, 'j' pour bleu, 'l' pour violet", text_colour=(255, 255, 255))
instructions.present()
exp.keyboard.wait()

# Tâche 1: Identification de la couleur du carré
for i in range(10):  # 10 essais pour la tâche des carrés
    couleurs_list = list(couleurs.values())
    random.shuffle(couleurs_list)
    for couleur in couleurs_list:
        key, rt = afficher_carré(couleur)
        nom_couleur = [k for k, v in couleurs.items() if v == couleur][0]
        print(f"Couleur: {nom_couleur}, Touche: {key}, RT: {rt}")

# Tâche 2: Identification de la couleur des mots
mots = ["rouge", "vert", "bleu", "purple"]
for i in range(5):  # 5 essais pour la tâche des mots
    random.shuffle(mots)
    for mot in mots:
        couleurs_possibles = [v for k, v in couleurs.items() if k != mot]
        couleur_impression = random.choice(couleurs_possibles)
        key, rt = afficher_mot(mot, couleur_impression)
        nom_couleur = [k for k, v in couleurs.items() if v == couleur_impression][0]
        print(f"Mot: {mot}, Couleur: {nom_couleur}, Touche: {key}, RT: {rt}")

# Fin de l'expérience
expyriment.control.end()
