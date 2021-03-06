# -*- coding: utf-8 -*-
"""
This class represents the algorithm Connected component filter
"""
import networkx as nx
import operator as op
from _alg import Algorithm, IntegerSlider, DropDown
from _utility import check_operator, draw_graph


__authors__ = {"Martino Bruni": "bruni.martino92@gmail.com"}


class AlgBody(Algorithm):
    """
    Connected component filter algorithm implementation
    """

    def __init__(self):
        """
        Connected component object constructor.

        Instance vars:
            | *name* : name of the algorithm
            | *parent* : name of the appropriated category
            | *compnt_size* : A threshold value for the size of
             the connected components
            | *operator* : A logical python operator.
             See python module operator

        """
        Algorithm.__init__(self)
        self.name = "Connected component filter"
        self.parent = "Graph filtering"
        self.compnt_size = IntegerSlider("Component Size", 0.0, 20.0, 1.0, 10)
        self.integer_sliders.append(self.compnt_size)
        self.operator = DropDown("Operator", {"Strictly smaller",
                                              "Smaller or equal",
                                              "Equal",
                                              "Greater or equal",
                                              "Strictly greater"})
        self.drop_downs.append(self.operator)

    def process(self, input_data):

        """
        Implements a filter which filters a graph for connected components
        according to a threshold value.
        To decide whether or not a connected component is removed the component
        size and the threshold value are used together in a logical operation.

        Example: Remove all connected components of size strictly
         smaller than 3
        Example: Remove all connected components of size greater or equal to 5
        Example: Remove all connected components of size exaclty 7

        Args:
            | *input_data* : A list which contains the image and the graph
        Raises:
            | *KeyError* : Filtering failed because the
             threshold connected component size is negative
        Returns:
            | *graph* : A filtered networkx graph

        """
        try:
            if self.compnt_size.value < 0:
                raise ArithmeticError("Connected_Components_Filter: Filtering \
                                      failed because the threshold connected \
                                      component size is negative:",
                                      self.compnt_size.value)

            self.operator.value = check_operator(self.operator)
            connected_components = sorted(
                list(nx.connected_component_subgraphs(input_data[1])),
                key=lambda graph: graph.number_of_nodes())
            to_be_removed = [subgraph for subgraph in connected_components
                             if self.operator.value(subgraph.number_of_nodes(),
                                                    self.compnt_size.value)]

            for subgraph in to_be_removed:
                input_data[1].remove_nodes_from(subgraph)
            print ('discarding a total of', len(to_be_removed),
                   'connected components ...')
        except ArithmeticError as ex:
            print ('Exception caught in', ex)

        self.result['img'] = input_data[0]
        self.result['graph'] = input_data[1]


if __name__ == '__main__':
    pass
