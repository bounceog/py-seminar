from consolemenu import *
from consolemenu.items import *


def init_menu():
    menu = ConsoleMenu("matplotlib: Visualization with Python")

    plot1_item = CommandItem("Plot1", "python src/plots/plot1.py")
    plot2_item = CommandItem("Plot2", "python src/plots/plot2.py")
    plot3_item = CommandItem("Plot2", "python src/plots/plot3.py")
    menu.append_item(plot1_item)
    menu.append_item(plot2_item)
    menu.append_item(plot3_item)

    menu.show()


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
