import networkx as nx

def build_graph():

    G = nx.Graph()

    G.add_node("Pump P101")

    G.add_node("Bearing Wear")
    G.add_node("Excessive Vibration")
    G.add_node("Inspection Report")

    G.add_edge(
        "Pump P101",
        "Bearing Wear"
    )

    G.add_edge(
        "Pump P101",
        "Excessive Vibration"
    )

    G.add_edge(
        "Pump P101",
        "Inspection Report"
    )

    return G