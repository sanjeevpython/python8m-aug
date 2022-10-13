# sets : Sequence of elements seperated with comma(,) which are declared inside { } which are unordered and will remove the duplicate elements.

a={43,'python',46,12,'12',4.6,(2,86,1),43,'12'}

print(a)

# There is no concept of accessing inside the set..

# Element inside the set should be immutable elments only..

# a={43,'python',46,12,'12',4.6,(2,86,1),43,'12',[1,2,3]} # will thrown the error as we tried to declare mutuable datatype..

# Sets are Mutubale ..

# set methods:

# print(dir(set))

# add,update
# remove,discard,clear,pop

# add  - its for adding a sinlge element into the set.(which is immutable element only.)

# a.add(49)
# print(a)

a.add('django')
# print(a)

# # update - Its for adding multiple elments into the set.

# a.update('django')

# print(a)

a.update([41,48,47],{51,52,53})

print(a)

# remove - Its for removing the specific element from the set..

# a.remove(48)
# print(a)

# # discard - Its for removing the specific element from the set.

# a.discard(41)

# print(a)

# # a.remove('devops')

# print(a.discard('devops'))

# # pop() - It will remove the starting element from the set.

# a.pop()

# print(a)

# clear() -- Its for removing everything and making it as empty set.

# a.clear()
# print(a)

# c={}

# print(type(c))
# empty_set = set()

# print(empty_set)

# print(type(empty_set))

# union(|) - Its for adding 2 sets as single set and removing the duplicates if any..

a={1,3,5,7}
b={2,4,6,7}

# print(a.union(b)) # {1,3,5,7,2,4,6}

# print(a|b)

# intersection(&) - It will return common elements between both the sets..

# print(a.intersection(b))

# print(a&b)

# # difference(-) - 

# print(a.difference(b)) # {1,3,5,7} - {2,4,6,7} = {1,3,5}

# print(b.difference(a)) # {2,4,6,7} - {1,3,5,7} = {2,4,6}

# print(a-b)
# print(b-a)

# # symmetric_difference(^) : removing common element between both the set and combining remaining elmenets as single set..

# print(a.symmetric_difference(b))

# print(a^b)

# print(a)
# print(b)

# a={1,3,5,7}
# b={2,4,6,7}

# a.intersection_update(b)

# print(a)

# a.difference_update(b) # {7}-{2,4,6,7}

# print(a)

# a.symmetric_difference_update(b) # {} - {2,4,6,7}

# print(a)

# frozenset() - Sets which are immutable..

a = frozenset([1,4,6,7])

print(a)

# print(type(a))

a.add(43)