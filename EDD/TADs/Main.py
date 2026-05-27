from FixedSet import FixedSet
from FixedQueue import FixedQueue

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


fixedSet()