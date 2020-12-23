import numpy as np
import distance
from collections import defaultdict


def search(dic, v):
    for key, value in dic.items():
        for k in value:
            if v == k:
                return key
    return None


def clustering(file, threshold):
    with open(file) as namesFile:
        strings = namesFile.readlines()
        strings = [item.lower() for item in strings]
        strings = [item.replace('\n', '') for item in strings]
        lev_similarity = np.array([[distance.levenshtein(w1,w2) for w1 in strings] for w2 in strings])
        clusters = defaultdict(list)
        numb = list(range(len(strings)))
    for i in range(0, len(strings)):
        for j in range(0, i):
            if j != i and lev_similarity[i][j] <= threshold:
                key = search(clusters, strings[j])
                if key is not None:
                    clusters[key].append(strings[i])
                    numb.remove(i)
                    break
        if i in numb:
            clusters[strings[i]].append(strings[i])
            numb.remove(i)
    return clusters


if __name__ == "__main__":
    ans = clustering('filename', 8)
    for cluster in ans.keys():
        print(ans[cluster])
