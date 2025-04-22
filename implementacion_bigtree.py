from bigtree import Node, print_tree

# Nodo raíz
futbol = Node("Fútbol")

uefa = Node("UEFA", parent=futbol)
conmebol = Node("CONMEBOL", parent=futbol)

espana = Node("España", parent=uefa)
inglaterra = Node("Inglaterra", parent=uefa)

colombia = Node("Colombia", parent=conmebol)
argentina = Node("Argentina", parent=conmebol)

Node("Real Madrid", parent=espana)
Node("FC Barcelona", parent=espana)

Node("Manchester City", parent=inglaterra)
Node("Liverpool", parent=inglaterra)

Node("Atletico Bucaramanga", parent=colombia)
Node("Atletico Nacional", parent=colombia)

Node("Boca Juniors", parent=argentina)
Node("River Plate", parent=argentina)

print_tree(futbol)
