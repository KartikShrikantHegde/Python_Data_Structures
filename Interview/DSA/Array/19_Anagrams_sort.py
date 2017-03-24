import collections


def ana(strs):
    groups = collections.defaultdict(list)
    for s in strs:
        groups[tuple(sorted(s))].append(str(s))
    print groups
    x = map(sorted, groups.values())
    flattened = [val for sublist in x for val in sublist]
    return flattened


print ana(strs=["dog", "listen", "tip", "enlist", "pit", "god", "man", "top", "pot"])
