import networkit as nk

G = nk.graphio.EdgeListReader("\t", 0).read("./MIT8.edgelist")

print(G)