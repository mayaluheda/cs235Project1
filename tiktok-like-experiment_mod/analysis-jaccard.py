import os, csv

files = os.listdir("data")
print(len(files))



files.sort()

pairs = list(zip(files[:20], files[20:40]))

print(pairs[0])

a1, c1 = pairs[-1]


def getAllValues(fn, column):
    with open(f"data/{fn}",  encoding='utf8') as fin:
        dr = csv.DictReader(fin)
        authors = [row[column] for row in dr]
    return authors



def jaccard(lst1, lst2):
    return len(set(lst1).intersection(set(lst2)))/len(set(lst1).union(set(lst2)))

for a1, c1 in pairs:
    authors1 = getAllValues(a1, "music")
    authors2 = getAllValues(c1, "music")
    print(jaccard(authors1, authors2))

