from consolemenu import *
from consolemenu.items import *


def init_menu():
    menu = ConsoleMenu("matplotlib: Visualization with Python")

    plot1_item = CommandItem("Plot1", "python src/plots/plot1.py")
    gender_alloc_item = CommandItem("Gender Allocation", "python src/plots/gender_alloc.py")
    men_smoker_alloc_item = CommandItem("Men Smoker Allocation", "python src/plots/men_smoker.py")

    menu.append_item(plot1_item)
    menu.append_item(gender_alloc_item)
    menu.append_item(men_smoker_alloc_item)

    menu.show()
    menu.join()


if __name__ == "__main__":
    print("""                                                                               
           db        .g8^^^bgd       db      `7MM^^^Yp, 
          ;MM:     .dP'     `M      ;MM:       MM    Yb 
         ,V^MM.    dM'       `     ,V^MM.      MM    dP 
        ,M  `MM    MM             ,M  `MM      MM^^^bg. 
        AbmmmqMA   MM.            AbmmmqMA     MM    `Y 
       A'     VML  `Mb.     ,'   A'     VML    MM    ,9 
     .AMA.   .AMMA.  `"bmmmd'  .AMA.   .AMMA..JMMmmmd9                                                                     
    """)

    init_menu()
