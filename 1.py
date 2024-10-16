import heapq


def min_cost_to_connect_cables(cables):

    heapq.heapify(cables)

    total_cost = 0

    while len(cables) > 1:
        # Два найменших кабелі
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)

        cost = first + second

        total_cost += cost

        # Об'єднаний кабель назад в купу
        heapq.heappush(cables, cost)

    return total_cost


cables = [4, 3, 2, 6, 13, 9, 5, 8]
print(min_cost_to_connect_cables(cables))
