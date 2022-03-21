def shortest_path(graph: dict, A: int, B: int) -> int:
    def _shortest_path(station, visitedStations, depth):
        if station == B:
            return depth
        
        nextStations = [s for s in graph[station] if s not in visitedStations]
        if nextStations == []:
            return float("inf") # not able to reach end station

        visitedStations.append(station)
        return min([_shortest_path(n, visitedStations, depth+1) for n in nextStations])

    return _shortest_path(A, [], 0)