import pandas as pd
import networkx as nx
import matplotlib as plt
import random

circlesF = open("0.circles","r")
edgesF = open("0.edges","r")
featsF = open("0.feat","r")
featnamesF = open("0.featnames","r")

G = nx.Graph()

#Getting every circle in the network:
circles = []
for circle in circlesF:
    circles.append(int(circle))

# There are 147 colors.
colors = ['aliceblue', 'antiquewhite', 'aqua', 'aquamarine', 'azure', 'beige', 'bisque', 'black',
 'blanchedalmond', 'blue', 'blueviolet', 'brown', 'burlywood', 'cadetblue', 'chartreuse', 'chocolate',
  'coral', 'cornflowerblue', 'cornsilk', 'crimson', 'cyan', 'darkblue', 'darkcyan', 'darkgoldenrod', 
  'darkgray', 'darkgreen', 'darkgrey', 'darkkhaki', 'darkmagenta', 'darkolivegreen', 'darkorange', 
  'darkorchid', 'darkred', 'darksalmon', 'darkseagreen', 'darkslateblue', 'darkslategray', 
  'darkslategrey', 'darkturquoise', 'darkviolet', 'deeppink', 'deepskyblue', 'dimgray', 'dimgrey',
   'dodgerblue', 'firebrick', 'floralwhite', 'forestgreen', 'fuchsia', 'gainsboro', 'ghostwhite',
    'gold', 'goldenrod', 'gray', 'green', 'greenyellow', 'grey', 'honeydew', 'hotpink', 'indianred', 
    'indigo', 'ivory', 'khaki', 'lavender', 'lavenderblush', 'lawngreen', 'lemonchiffon', 'lightblue',
     'lightcoral', 'lightcyan', 'lightgoldenrodyellow', 'lightgray', 'lightgreen', 'lightgrey', 
     'lightpink', 'lightsalmon', 'lightseagreen', 'lightskyblue', 'lightslategray', 'lightslategrey', 
     'lightsteelblue', 'lightyellow', 'lime', 'limegreen', 'linen', 'magenta', 'maroon', 
     'mediumaquamarine', 'mediumblue', 'mediumorchid', 'mediumpurple', 'mediumseagreen', 
     'mediumslateblue', 'mediumspringgreen', 'mediumturquoise', 'mediumvioletred', 'midnightblue',
      'mintcream', 'mistyrose', 'moccasin', 'navajowhite', 'navy', 'oldlace', 'olive', 'olivedrab',
       'orange', 'orangered', 'orchid', 'palegoldenrod', 'palegreen', 'paleturquoise', 'palevioletred', 
       'papayawhip', 'peachpuff', 'peru', 'pink', 'plum', 'powderblue', 'purple', 'rebeccapurple', 'red',
        'rosybrown', 'royalblue', 'saddlebrown', 'salmon', 'sandybrown', 'seagreen', 'seashell', 'sienna',
         'silver', 'skyblue', 'slateblue', 'slategray', 'slategrey', 'snow', 'springgreen', 'steelblue', 'tan', 'teal', 'thistle', 'tomato', 'turquoise', 'violet', 'wheat', 'white', 'whitesmoke','yellow', 'yellowgreen']

i = 1

for line in featsF:
    G.add_node(i,color=random.choice(colors))
    i += 1


for line in edgesF:
    words = line.split()
    e1 = int(words[0])
    e2 = int(words[1])
    G.add_edge(e1,e2)

popularity = [0] * nx.number_of_edges(G)

for line in edgesF:
    words = line.split()
    e1 = int(words[0])
    e2 = int(words[1])
    popularity[e1] += 1
    popularity[e2] += 1

pos = nx.spring_layout(G,k=1)  # positions for all nodes

# nodes
#options = {"node_size": 200, "alpha": 0.5}
#nx.draw_networkx_nodes(G, pos, nodelist=[1, 2, 3], node_color="r", **options)
#nx.draw_networkx_nodes(G, pos, nodelist=[4, 5, 6, 7], node_color="b", **options)

#val_map = {}
#node_color=values

#Define array of node sizes!!

labels = {}
for g in G.nodes():
    labels[g] = g

nx.draw_networkx(G,
                 pos=pos,
                 label="Social CirclesF",
                 labels=labels,
                 with_labels=True,
                 font_size=8,
                 width=1.0,
                 #font_color='white',
                 node_color=[nx.get_node_attributes(G,'color')[g] for g in G.nodes()],
                 )

plt.show()


induced_subgraph(G, nbunch)