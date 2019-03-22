import networkx as nx
import pandas as pd

def read_data(file_name):
    data = pd.read_csv(file_name)
    return data

def create_directed_graph(data):
    graph = nx.from_pandas_edgelist(data, "FROM_NODE", 
                                    "TO_NODE", "VALUE",  
                                    create_using=nx.DiGraph())
    return graph

def get_simple_cycles(directed_graph):
    cycles = nx.simple_cycles(directed_graph)

    return cycles

def get_max_transaction_cycle(directed_graph, simple_cycles):

    max_sum_transaction_sc = 0
    
    for sc in simple_cycles:

        # store sum of transactions for the given simple cycle
        sum_transaction_sc = 0

        # make a list of from nodes
        node_from_list = sc

        # make a list of to nodes
        node_to_list = sc[1:] + sc[:1]

        # make a list of edges in the cycle
        edges = []

        for node_from, node_to in zip(node_from_list, node_to_list):
            edges.append((node_from, node_to))

        # get the sum of transactions
        for node_from, node_to in edges:
            transaction_value = directed_graph[node_from][node_to]["VALUE"]
            sum_transaction_sc += transaction_value

        # store the best cycle
        if sum_transaction_sc > max_sum_transaction_sc:
            max_sum_transaction_sc = sum_transaction_sc
            max_sum_transaction_edges = edges

    return max_sum_transaction_sc, max_sum_transaction_edges

def main():
    
    # name of the data file
    file_name = "data_Problem2 (1).csv"

    # read the data
    data = read_data(file_name)

    # create a directed graph from the data
    directed_graph = create_directed_graph(data)

    # get the simple cycles
    simple_cycles = get_simple_cycles(directed_graph)
    
    # get the cycle which has maximum transaction sum
    best_sum, best_edges = get_max_transaction_cycle(directed_graph, simple_cycles)

    print("edges of simple cycle with maximum transaction value:", best_edges)
    print("max transaction value:", best_sum)
    

if __name__ == "__main__":
    main()
