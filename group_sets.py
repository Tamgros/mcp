
from collections import defaultdict

# Disjoint Set (Union-Find) implementation
class DisjointSet:
    def __init__(self):
        self.parent = {}

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.parent[root_y] = root_x

    def add(self, x):
        if x not in self.parent:
            self.parent[x] = x

def merge_separate_sets_with_total_counts(*arrays_list):
    ds = DisjointSet()
    element_to_set = {}
    element_counts = defaultdict(int)

    # Flatten input: extract sets from nested lists
    all_sets = []
    for array in arrays_list:
        for sublist in array:  # Handle nested lists
            if isinstance(sublist, list):
                all_sets.extend(sublist)
            else:
                all_sets.append(sublist)

    # Add elements to the disjoint set and merge overlapping sets
    for s in all_sets:
        first_elem = list(s)[0]  # Pick a representative element for merging
        for elem in s:
            ds.add(elem)
            ds.union(first_elem, elem)
            element_to_set[elem] = s
            element_counts[elem] += 1  # Count occurrences of each element

    # Group by connected components
    merged_groups = defaultdict(set)
    total_counts = defaultdict(int)

    for elem in element_to_set:
        root = ds.find(elem)
        merged_groups[root].update(element_to_set[elem])
        total_counts[root] += element_counts[elem]

    # Convert to list and include total occurrence count for the set
    result = [(group, sum(element_counts[elem] for elem in group)) for group in merged_groups.values()]

    return result

# Example input arrays
array1 = [{1, 2}, {3, 4, 6}, {7}, {8, 10}]
array2 = [{2, 4}, {9}, {7, 8}]
array3 = [{11, 12}, {13, 14}]
array4 = [{1, 2},{2, 4}, {12, 15}, {16}]

# Compute merged sets with total occurrence counts
merged_separated_sets_with_total_counts = merge_separate_sets_with_total_counts(array1, array2, array3, array4)
merged_separated_sets_with_total_counts