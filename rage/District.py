from rage.Office import Office
from rage.Werehouse import Werehouse
from rage.Rezidential import Rezidential
import webbrowser
from tkinter import *
from tkinter import messagebox
off = Office()
were = Werehouse()
resid = Rezidential()


print(off.info_office(),off.num_rooms(),off.people(),off.size_office())
print(were.info_werehouse(), were.num_rooms(), were.people(), were.size_werehouse())
print(resid.info_rezidential_(), resid.num_rooms(), resid.people(), resid.size_residential())


