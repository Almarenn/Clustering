import numpy as np
import distance
import sys
from collections import defaultdict

def search(dic, v):
    for key, value in dic.items():
        for k in value:
            if v == k:
                return key
    return None


def get_strings_list(file):
    with open(file) as namesFile:
        strings = namesFile.readlines()
        strings = [item.lower() for item in strings]
        strings = [item.replace('\n', '') for item in strings]
    return strings

#calculate levenshtein edit distance between every 2 strings, and store it in the matrix
def get_lev_similarity_matrix(strings):
    return np.array([[distance.levenshtein(w1,w2) for w1 in strings] for w2 in strings])


def create_strings_group_dict(lev_similarity,strings):
    clusters = defaultdict(list)
    numb = list(range(len(strings))) #list of all strings indexes
    for i in range(0, len(strings)):
        for j in range(0, i):
            #string i and j have edit distance <= threshold
            if j != i and lev_similarity[i][j] <= threshold:
                key = search(clusters, strings[j]) # find if there's already exiting list that contain string j
                if key is not None:
                    clusters[key].append(strings[i]) # add string i to the list
                    numb.remove(i)
                    break
        # no exiting list was found, create a new one with string i as the key
        if i in numb:
            clusters[strings[i]].append(strings[i])
            numb.remove(i)
    return clusters
  
    
def clustering(file, threshold):
    strings = get_strings_list(file)
    lev_similarity = get_lev_similarity_matrix(strings)
    return create_strings_group_dict(lev_similarity,strings)


def main(file_apth, threshold):
    ans = clustering(file_path, threshold)
    for cluster in ans.keys():
        print(ans[cluster])

        
if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])

