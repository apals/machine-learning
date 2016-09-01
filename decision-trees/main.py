import dectrees_py.monkdata as m
import dectrees_py.dtree as dtree

monks = [m.monk1, m.monk2, m.monk3]

for monk in monks:
    print(dtree.entropy(monk))


print('--------------- THE MOST POWERFUL DELIMITER OF 2016 -----------------')


for monk in monks:
    for attr in m.attributes:
        print(str(attr) + ": " + str(dtree.averageGain(monk, attr)))


print('--------------- THE SECOND MOST POWERFUL DELIMITER OF 2016 -----------------')

t=dtree.buildTree(m.monk1, m.attributes)
print(dtree.check(t, m.monk1))
print(dtree.check(t, m.monk1test))

t=dtree.buildTree(m.monk2, m.attributes)
print(dtree.check(t, m.monk2))
print(dtree.check(t, m.monk2test))

t=dtree.buildTree(m.monk3, m.attributes)
print(dtree.check(t, m.monk3))
print(dtree.check(t, m.monk3test))