def shortest_path(graph: dict, A: int, B: int) -> int:
    def _shortest_path(station, visitedStations, depth):
        if station == B:
            return depth

        if station not in graph: # for some reason 4 isnt in the graph for the tests
            # if visitedStations != []:
            #     graph[station] = [visitedStations[-1]]
            # else:
            for k, v in graph.copy().items():
                if station in v:
                    if graph.get(station) == None:
                        graph[station] = [k]
                    else:
                        graph[station].append(k)
        
        nextStations = [s for s in graph[station] if s not in visitedStations]
        if nextStations == []:
            return depth+1

        visitedStations.append(station)
        return min([_shortest_path(n, visitedStations, depth+1) for n in nextStations])
    return _shortest_path(A, [], 0)