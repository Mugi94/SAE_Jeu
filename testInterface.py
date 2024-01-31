from __future__ import annotations
from personnage import Laura, Aurore, Akane, Bob


aurore = Aurore()
laura = Laura()
akane = Akane()
bob = Bob()

aurore.recevoirCoup(35)
print(f"Point de vie avant soin : {aurore.PV}")
laura.lancerCapacite(aurore)
print(f"Point de vie apres soin : {aurore.PV}")

laura.recevoirCoup(50)
print(f"Point de vie avant soin : {laura.PV}")
laura.lancerCapacite(laura)
print(f"Point de vie apres soin : {laura.PV}")

akane.lancerCapacite()
akane.recevoirCoup(15)