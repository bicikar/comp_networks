import json

MAX_ITER = 16


class Network:
    def __init__(self, ):
        self.nodes = {
        }

    def add_node(self, key):
        if key not in self.nodes:
            self.nodes[key] = Node(key, self)
        else:
            pass

    def add_edge(self, a, b):
        self.nodes[a].add_neighbor(b)
        self.nodes[b].add_neighbor(a)

    def get(self, key):
        if key in self.nodes:
            return self.nodes[key]
        else:
            return None

    def update(self):
        if_update = 0
        for k in self.nodes:
            if_update += self.nodes[k].update()
        return if_update != 0


class Node:
    def __init__(self, key, network):
        self.network = network
        self.key = key
        self.routing_table = {
            key: (0, key)}

    def _update(self, key):
        if_update = False
        node = self.network.get(key)
        for k, v in node.routing_table.items():
            if k not in self.routing_table:
                self.routing_table[k] = (v[0] + 1, node.key)
                if_update = True
            else:
                if self.routing_table[k][0] > v[0] + 1:
                    self.routing_table[k] = (v[0] + 1, node.key)
                    if_update = True
        return if_update

    def update(self):
        neighbors = [k for k, v in self.routing_table.items() if v[0] == 1]
        if_update = 0
        for k in neighbors:
            if_update += self._update(k)
        return if_update != 0

    def add_neighbor(self, key):
        self.routing_table[key] = (1, key)

    def query(self, name):
        pass


if __name__ == "__main__":
    net = Network()

    networks = json.load(open('network.json'))
    for addr, con in networks.items():
        net.add_node(addr)
        for el in con:
            net.add_node(el)
            net.add_edge(addr, el)

    step = 1
    while net.update() and MAX_ITER > 0:
        for k in net.nodes:
            print(f'Simulation step {step} of router {k}:')
            print(
                f'{"[Source IP]":20} {"[Destination IP]":20} {"[Next Hop]":20} {"Metric":20}')
            for addr, val in net.get(k).routing_table.items():
                if addr != k:
                    print(
                        f'{k:20} {addr:20} {val[1]:20} {val[0]}')
            print()
        step += 1
        MAX_ITER -= 1

    for k in net.nodes:
        print(f'Final state of router {k}:')
        print(
            f'{"[Source IP]":20} {"[Destination IP]":20} {"[Next Hop]":20} {"Metric":20}')
        for addr, val in net.get(k).routing_table.items():
            if addr != k:
                print(
                    f'{k:20} {addr:20} {val[1]:20} {val[0]}')
        print()
