from __future__ import annotations

import re

# #############################################################################
# ################################ RIDDLE 1 ###################################
# #############################################################################
from itertools import combinations
from typing import Any, Optional

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
from rich import inspect, print

from adventofcode.helper.io import get_day, get_riddle_input, save_riddle_input


def simplify_graph_with_predicate(G: nx.Graph):
    """
    Loop over the graph until all nodes that match the supplied predicate
    have been removed and their incident edges fused.
    """
    g = G.copy()
    node_removal_predicate = lambda node: G.nodes[node]["rate"] == 0

    while any(node_removal_predicate(node) for node in g.nodes):
        g0 = g.copy()
        print("g0")
        for node in g.nodes:
            if node_removal_predicate(node):

                edges_containing_node = g.edges(node)
                dst_to_link = [e[1] for e in edges_containing_node]
                dst_pairs_to_link = list(combinations(dst_to_link, r=2))
                for pair in dst_pairs_to_link:
                    g0.add_edge(pair[0], pair[1])
                    dist = nx.shortest_path_length(
                        g0, pair[0], pair[1], weight="weight"
                    )
                    # get the distance that would result from
                    # removing the current node
                    # the new distance is the sum of the distances
                    new_dist = (
                        nx.shortest_path_length(g0, pair[0], node, weight="weight")
                        + nx.shortest_path_length(g0, node, pair[1], weight="weight")
                        + 1
                    )

                    # print(dist, new_dist)
                    # if new_dist < dist:
                    g0.remove_edge(pair[0], pair[1])
                    g0.add_edge(pair[0], pair[1], weight=new_dist)

                g0.remove_node(node)
                break
        g = g0
    return g


def riddle1(riddle_input: str) -> int | str:
    valves, rates = parsed_input = parse_input(riddle_input)
    # Remove valves that have a rate of zero
    # instead add a new connectivity to the valve that is connected to this valve
    # with an increased edge weight
    G = nx.Graph()
    nodes = [(k, {"rate": v}) for k, v in rates.items()]
    G.add_nodes_from(nodes)
    for k, v in valves.items():
        for valve, _ in v:
            G.add_edge(k, valve, weight=1)
    Gsimple = simplify_graph_with_predicate(G)
    print(G)
    print(Gsimple)
    options = {
        "font_size": 2,
        "node_size": 30,
        "node_color": "white",
        "edgecolors": "black",
        "linewidths": 5,
        "width": 5,
    }
    pos = nx.spring_layout(Gsimple, k=0.15, iterations=20)
    nx.draw_networkx(Gsimple, **options, pos=pos)

    # Set margins for the axes so that nodes aren't clipped
    ax = plt.gca()
    ax.margins(0.20)
    plt.axis("off")
    plt.show()


# #############################################################################
# ################################ RIDDLE 2 ###################################
# #############################################################################
def riddle2(riddle_input: str) -> int | str:

    answer = 0
    return answer


# #############################################################################
# ################################ HELPER #####################################
# #############################################################################


def map_to_int(s: str) -> int:
    int0 = ord(s[0]) - ord("A")
    int1 = ord(s[1]) - ord("A")
    return int0 * 26 + int1


def parse_input(riddle_input: str) -> Optional[Any]:
    valves = {}
    weights = {}
    for i, line in enumerate(riddle_input.splitlines()):
        # Valve QK has flow rate=0; tunnels lead to valves MV, AU
        # Valve KR has flow rate=17; tunnels lead to valves WA, JQ, JY, KI
        # Valve OI has flow rate=5; tunnels lead to valves SU, OX, LW, JH, DK

        # Match the word after "Valve" and before "has", the flow rate,
        # and all valves that are connected to this valve
        # if "valves" in line:
        matches = re.match(
            r"Valve (\w+) has flow rate=(\d+); tunnel[s]? lead[s]? to valve[s]? (\w+(, \w+)*)",
            line,
        )
        if matches:
            id = matches.group(1)
            flowrate = matches.group(2)
            outgoing = matches.group(3).split(", ")
            if matches.group(4):
                outgoing += matches.group(4).split(", ")
            outgoing = [_ for _ in outgoing if _ != ""]
            idint = map_to_int(id)
            outgoingint = [(map_to_int(_), 1) for _ in outgoing]
            valves[idint] = outgoingint
            weights[idint] = int(flowrate)
    return valves, weights


def print_input() -> bool:
    # return True
    return False


def get_example() -> str:
    return """"""


def load() -> str:
    day = get_day(__file__)
    riddle_input = get_riddle_input(day)
    save_riddle_input(day, riddle_input)
    if (example := get_example()) != "":
        riddle_input = example
    if print_input():
        print(riddle_input)
    return riddle_input


if __name__ == "__main__":
    riddle_input = load()
    answer1 = riddle1(riddle_input)
    print(answer1)
    answer2 = riddle2(riddle_input)
    print(answer2)
