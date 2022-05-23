from xml.dom.minidom import parse
import xml.dom.minidom
import matplotlib.pyplot as plt
import numpy as np

DOMTree = xml.dom.minidom.parse("go_obo.xml")
collection = DOMTree.documentElement
terms = collection.getElementsByTagName("term")  # use the '.getElementsByTagName' to find all 'term'
print("There are", len(terms), "terms")

num_child_nodes = []
num_translation = []
translation = []
dict = {}
for term in terms:
    is_a = term.getElementsByTagName("is_a")  # find the <is_a> in the term
    term_id = term.getElementsByTagName("id")[0].childNodes[0].data  # find the <id> in the term
    defstr = term.getElementsByTagName("defstr")[0].childNodes[0].data.upper()  # find the <defstr> in the term
    # if there are "TRANSLATION" in <defstr>, add the term_id into the translation(a list).
    if defstr.count("TRANSLATION") > 0:
        translation.append(term_id)
    # create a new list for dict[term_id] if it never appears in the dict[key]
    if term_id not in dict:
        dict[term_id] = []
    for i in range(len(is_a)):
        is_a = term.getElementsByTagName("is_a")[i].childNodes[0].data
        if is_a not in dict:
            dict[is_a] = []
        # add all childnodes of is_a(father node) in dict[is_a].
        dict[is_a].append(term_id)
        dict[is_a].append(dict[term_id])


# define a function to turn all lists into strings and store the strings in unfold_list_child_nodes.
# there are a lot of repetition.
def unfold_child_nodes(list):
    for l in list:
        if type(l) == str:
            unfold_list_child_nodes.append(l)
        else:
            unfold_child_nodes(l)


for key, value in dict.items():
    unfold_list_child_nodes = []
    # for each term(dict[key]), list all childnodes including the repetition.
    unfold_child_nodes(value)
    # remove the empty list and repeated elements for each term
    dict[key] = list(set(unfold_list_child_nodes))
    num_child_nodes.append(len(dict[key]))  # store all number of childnodes except 0 in the list(num_child_nodes)
    # store all number of childNodes for the term associated with translation into the list(num_translation)
    if key in translation:
        num_translation.append(len(dict[key]))

# draw two boxplots
plt.boxplot(num_child_nodes, vert=True, whis=1.5, patch_artist=True, showbox=True, showcaps=True, showfliers=False)
plt.title('Distribution of child node number of all GO terms')
plt.xlabel("all terms")
plt.ylabel("Number")
plt.show()
plt.boxplot(num_translation, vert=True, whis=1.5, patch_artist=True, showbox=True, showcaps=True, showfliers=False)
plt.title('Distribution of child node number of terms associated with ‘translation’')
plt.xlabel("all terms associated with ‘translation’")
plt.ylabel("Number")
plt.show()

# calculate the average
average_all = np.average(num_child_nodes)
average_translation = np.average(num_translation)
# compare the average numbers
print(average_all)
print(average_translation)
if average_all > average_translation:
    print("the term contains translation have a smaller number of childNodes on average")
else:
    print("the term contains translation have a greater number of childNodes on average")

