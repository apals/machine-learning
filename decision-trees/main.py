import dectrees_py.monkdata as m
import dectrees_py.dtree as dtree
import dectrees_py.drawtree as drawtree
import random
import matplotlib.pyplot as plt

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

subsets = []
for i in [0, 1, 2, 3]:  # all values that a5 could be minus since index
    subsets.append(dtree.select(m.monk1, m.attributes[4], m.attributes[4].values[i]))

for subset in subsets:

    print(dtree.bestAttribute(subset, m.attributes))

    print('=============')

print("A5", dtree.mostCommon(subsets[0]),"A4", dtree.mostCommon(subsets[1]),"A6", dtree.mostCommon(subsets[2]),"A1", dtree.mostCommon(subsets[3]))
t = dtree.buildTree(m.monk1, m.attributes, 2)
print(t)
drawtree.drawTree(t)

print('--------------- THE FOURTH MOST POWERFUL DELIMITER OF 2016 -----------------')


def partition(data, fraction):
    ldata = list(data)
    random.shuffle(ldata)
    breakPoint = int(len(ldata) * fraction)
    return ldata[:breakPoint], ldata[breakPoint:]


def prune(tree, maxPerformance, testdata):
    prunedTrees = dtree.allPruned(tree)
    foundNewMax = False
    for pruned_tree in prunedTrees:
        if dtree.check(pruned_tree, testdata) > maxPerformance:
            maxPerformance = dtree.check(pruned_tree, testdata)
            mtree = pruned_tree
            foundNewMax = True

    if foundNewMax:
        return prune(mtree, maxPerformance, testdata)
    else:
        return tree


monk1perf = []
monk3perf = []
frc = [0.3, 0.4, 0.5, 0.6, 0.7, 0.8]
for f in frc:
    monk1train, monk1val = partition(m.monk1, f)
    monk1tree = dtree.buildTree(monk1train, m.attributes)
    monk1tree_pruned = prune(monk1tree, dtree.check(monk1tree, monk1val), monk1val)
    monk1perf.append(dtree.check(monk1tree_pruned, monk1val))

    monk3train, monk3val = partition(m.monk3, f)
    monk3tree = dtree.buildTree(monk3train, m.attributes)
    monk3tree_pruned = prune(monk3tree, dtree.check(monk3tree, monk3val), monk3val)
    monk3perf.append(dtree.check(monk3tree_pruned, monk3val))

    # drawtree.drawTree(monk3tree_pruned)

plt.plot(frc, monk1perf, 'r', label='m1')
plt.plot(frc, monk3perf, 'b', label='m3')
plt.title('Performance vs Fraction')
plt.ylabel('Performance')
plt.xlabel('Fraction')
plt.legend()
plt.show()

print(monk1perf, monk3perf)
# drawtree.drawTree(monk3tree_pruned)
