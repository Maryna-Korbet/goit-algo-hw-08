# There are several network cables of different lengths, they must be combined twice into one cable, 
# using connectors, in the order that will lead to the lowest costs. The costs of connecting two cables 
# are equal to the sum of their lengths, and the total costs are equal to the sum of connecting all cables.
# The task is to find an order of association that minimizes the total costs.

import heapq

def order_of_unification(cables): 
    # Create Min Heap
    heapq.heapify(cables)
    total_cost = 0

    while len(cables) > 1:
        # Get the smallest two cables
        min1 = heapq.heappop(cables)
        min2 = heapq.heappop(cables)

        # Add the sum of the lengths of the smallest two cables
        cost = min1 + min2
        total_cost += cost

        # Add the new cable to the heap
        heapq.heappush(cables, cost)

    return total_cost

#Test  
cables = [1, 2, 3, 4]
print(f"Total cost:", order_of_unification(cables)) 
