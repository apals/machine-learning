import dectrees_py.monkdata as m
import dectrees_py.dtree as dtree
# import dectrees_py.drawtree as drawtree
import random

monks = [m.monk1, m.monk2, m.monk3]

for monk in monks:
    print(dtree.entropy(monk))

print('--------------- THE MOST POWERFUL DELIMITER OF 2016 -----------------')

for monk in monks:
    for attr in m.attributes:
        print(str(attr) + ": " + str(dtree.averageGain(monk, attr)))

print('--------------- THE SECOND MOST POWERFUL DELIMITER OF 2016 -----------------')

t = dtree.buildTree(m.monk1, m.attributes)
print(dtree.check(t, m.monk1))
print(dtree.check(t, m.monk1test))

t = dtree.buildTree(m.monk2, m.attributes)
print(dtree.check(t, m.monk2))
print(dtree.check(t, m.monk2test))

t = dtree.buildTree(m.monk3, m.attributes)
print(dtree.check(t, m.monk3))
print(dtree.check(t, m.monk3test))

print('--------------- THE THIRD MOST POWERFUL DELIMITER OF 2016 -----------------')


def partition(data, fraction):
    ldata = list(data)
    random.shuffle(ldata)
    breakPoint = int(len(ldata) * fraction)
    return ldata[:breakPoint], ldata[breakPoint:]


monk1train, monk1val = partition(m.monk1, 0.6)

prune_tree = dtree.buildTree(monk1train, m.attributes)
prune_tree_performance = dtree.check(prune_tree, monk1val)
allPrunedTrees = dtree.allPruned(prune_tree)

while True:
    oldStuff = prune_tree_performance
    for pruned_tree in allPrunedTrees:
        newPerformance = dtree.check(pruned_tree, monk1val)
        if prune_tree_performance < newPerformance:
            prune_tree = pruned_tree
            prune_tree_performance = newPerformance
    if prune_tree_performance == oldStuff:
        break


print(prune_tree)
print(prune_tree_performance)

            # drawtree.drawTree(prune_tree)
