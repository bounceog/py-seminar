from consolemenu import *
from consolemenu.items import *


def init_menu():
    menu = ConsoleMenu("matplotlib: Visualization with Python")

    gender_alloc_item = CommandItem("Gender Allocation", "python src/plots/gender_alloc.py")
    men_smoker_alloc_item = CommandItem("Men Smoker Allocation", "python src/plots/men_smoker.py")
    female_smoker_alloc_item = CommandItem("Female Smoker Allocation", "python src/plots/female_smoker.py")
    subjective_finding_item = CommandItem("Subjective Finding Smokers", "python src/plots/subjective_finding.py")
    high_blood_pressure_item = CommandItem("High blood pressure Smokers", "python src/plots/high_blood_pressure.py")
    beispiel_item = CommandItem("Angepasstes Beispiel", "python src/plots/bsp.py")
    
    menu.append_item(gender_alloc_item)
    menu.append_item(men_smoker_alloc_item)
    menu.append_item(female_smoker_alloc_item)
    menu.append_item(subjective_finding_item)
    menu.append_item(high_blood_pressure_item)
    menu.append_item(beispiel_item)

    menu.show()
    menu.join()


if __name__ == "__main__":
    init_menu()
