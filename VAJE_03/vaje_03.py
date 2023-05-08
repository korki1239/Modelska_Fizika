import spacy
import nltk
from tqdm.notebook import tqdm
import networkx as nx
import re #regular expression

#1 Naložimo besedilo
book=open("GOT.txt").read()

#2 Čiščenje besedila
book=re.sub(r"“","",book)
book=re.sub(r"”","",book)

#3 Diskretizacija besedila
stavki=nltk.sent_tokenize(book)
print(f"Stevilo stavkov v besedilu je {len(stavki)}")

nlp=spacy.load("en_core_web_sm")

liki={}

N=int(0.1*len(stavki))

for s in tqdm(range(N)):
    doc=nlp(stavki[s])
    for ent in doc.ents:
        if ent.label_=="PERSON":
            oseba=ent.text
            if oseba not in liki:
                liki[oseba]=[]
            liki[oseba].append(s)
            
for oseba in liki:
    print(oseba,liki[oseba])
    
G=nx.Graph()
for oseba in liki:
    G.add_node(oseba)

print(f"Število oseb = {len(G)}")

nodes=G.nodes()