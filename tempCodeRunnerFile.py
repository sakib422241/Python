class Graph:
    def __init__(self):
        self.edges={"Arad":["Zerind","Timisoara","Sibiu"],"Zerind":["Oradea"],"Oradea":["Sibiu"],"Timisoara":["Lugoj"],"Lugoj":["Mehadia"],"Mehadia":["Dobreta"],"Dobreta":["Craiova"],"Sibiu":["Fagaras","RimnicuVilcea"],"Craiova":["RimnicuVilcea","Pitesti"],"RimnicuVilcea":["Craiova","Pitesti"],"Fagaras":["Bucharest"],"Pitesti":["Bucharest"],"Bucharest":["Giurgiu","Urziceni"],"Urziceni":["Hirsova","Vaslui"],"Hirsova":["Eforie"],"Vaslui":["Lasi"],"Lasi":["Neamt"]}
        self.weights={"AradZerind":75,"ZerindOradea":71,"AradTimisoara":118,"TimisoaraLugoj":111,"LugojMehadia":70,"MehadiaDobreta":75,"AradSibiu":140,"OradeaSibiu":151,"DobretaCraiova":120,"CraiovaRimnicuVilcea":146,"CraiovaPitesti":138,"SibiuFagaras":99,"SibiuRimnicuVilcea":80,"RimnicuVilceaPitesti":97,"RimnicuVilceaCraiova":146,"FagarasBucharest":211,"PitestiBucharest":101,"BucharestGiurgiu":90,"BucharestUrziceni":85,"UrziceniHirsova":98,"HirsovaEforie":86,"UrziceniVaslui":142,"VasluiLasi":92,"LasiNeamt":87}
    def neighbors(self,node):
        return self.edges[node]
    def get_cost(self,from_node,to_node):
        return self.weights[(from_node + to_node)]
def ucs(graph, start, goal):
    global total_cost
    visited = set()
    path=[]
    queue = PriorityQueue()
    queue.put((0, start))
    while queue:
        cost, node = queue.get()
        if node not in visited:
            visited.add(node)
            if node == goal:
                return visited
            for i in graph.neighbors(node):
                if i not in visited:
                    total_cost = cost + graph.get_cost(node, i)
                    queue.put((total_cost, I)
                    )
graph=Graph()
s=ucs(graph,"Arad","Bucharest")
print(s)