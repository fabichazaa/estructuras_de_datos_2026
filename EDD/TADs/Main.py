from FixedSet import FixedSet
from FixedQueue import FixedQueue
from SortedSequence import SortedSequence
from Set import Set
from Dictionary import Dictionary
from SquaredMatrix import SquaredMatrix
from MultiSet import MultiSet
from LinkedList import LinkedList

# Fixed Set
def fixedSet():
    print("------ Set With Capacity ------ ")
    s = FixedSet(20)
    s.insert(5)
    s.insert(8)
    s.insert(15)
    s.insert(19)
    print(s)
    print("Length:", s.len())
    print("5 exists?", s.exists(5))
    print("20 exists?",s.exists(20))

    for i in s:
        print(i)

# Fixed Queue
def fixedQueue():
    print("------ Fixed Queue ------ ")
    fq = FixedQueue(5)
    print("Is empty?", fq.is_empty())
    fq.enqueue(5)
    fq.enqueue(8)
    fq.enqueue(15)
    fq.enqueue(87)
    fq.enqueue(134)
    print(fq)
    print("Length:", fq.len())
    element = fq.dequeue()
    print("Dequeued element:", element)
    element = fq.dequeue()
    print("Dequeued element:", element)
    fq.enqueue(42)
    print(fq)
    print("Length:", fq.len())
    print("Is empty?", fq.is_empty())

# Sorted Sequence
def sortedSequence():
    print("------ Sorted Sequence ------ ")
    ss = SortedSequence()
    ss.insert(5)
    ss.insert(8)
    ss.insert(15)
    ss.insert(19)
    print(ss)
    print("Length:", ss.len())
    ss.delete_first()
    ss.insert(1)
    print(ss)
    print("Length:", ss.len())
    ss.delete_last()
    print(ss)
    print("Length:", ss.len())
    print("Element at index 1:", ss.get_at(1))

# Set
def set():
    print("------ Set ------ ")
    s = Set()
    s.insert(5)
    s.insert(8)
    s.insert(15)
    s.insert(19)
    print(s)
    print("Length:", s.len())
    print("5 exists?", s.exists(5))
    print("20 exists?",s.exists(20))

    for i in s:
        print(i)

# Dictionary
def dictionary():
    print("------ Dictionary ------ ")
    d = Dictionary()
    d.insert("apple", 5)
    d.insert("banana", 8)
    d.insert("orange", 15)
    print(d)
    print("Length:", d.len())
    print("Does 'apple' exist?", d.exists("apple"))
    print("Does 'grape' exist?", d.exists("grape"))
    print("Value for 'banana':", d.get("banana"))
    d.delete("banana")
    print(d)
    print("Length:", d.len())

# Squared Matrix
def squaredMatrix():
    print("------ Squared Matrix ------ ")
    sm = SquaredMatrix(3)
    sm.insert(0, 0, 1)
    sm.insert(0, 1, 2)
    sm.insert(0, 2, 3)
    sm.insert(1, 0, 4)
    sm.insert(1, 1, 5)
    sm.insert(1, 2, 6)
    sm.insert(2, 0, 7)
    sm.insert(2, 1, 8)
    sm.insert(2, 2, 9)
    print(sm)
    print("Element at (1,1):", sm.get(1, 1))
    sm.delete(1, 1)
    print(sm)

# MultiSet
def multiSet():
    print("------ MultiSet ------ ")
    ms = MultiSet()
    ms.insert(5)
    ms.insert(8)
    ms.insert(15)
    ms.insert(5)
    print(ms)
    print("Length (distinct):", ms.len())
    print("Cardinality (total):", ms.cardinal())
    print("Multiplicity of 5:", ms.multiplicity(5))
    print("Multiplicity of 8:", ms.multiplicity(8))
    print("Multiplicity of 15:", ms.multiplicity(15))
    print("Multiplicity of 20:", ms.multiplicity(20))
    ms.delete(5)
    print(ms)
    print("Length (distinct):", ms.len())
    print("Cardinality (total):", ms.cardinal())
    print("Multiplicity of 5:", ms.multiplicity(5))

# Linked List
def linkedList():
    ll = LinkedList()
    ll.insert_last(1)
    ll.insert_last(3)
    ll.insert_last(5)
    ll.insert_first(7)
    print(ll)
    ll.insert_at(4, 2)
    print(ll)
    print("Index of 3: ", ll.index_of(3))
    print("Index of 100: ", ll.index_of(100))
    print("5 exists?", ll.exists(5))
    print("90 exists?", ll.exists(90))
    print("Length: ", ll.len())
    ll.delete_element(5)
    print(ll)

linkedList()