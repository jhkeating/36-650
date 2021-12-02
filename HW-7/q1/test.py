from queue import Queue
import pytest

def test_queue():
    '''
    Unit testing for the queue implementation found in queue.py

    Coverage report can be found in htmlcov/index.html 
    (we have 100% code coverage )
    '''

    q = Queue()
    assert q.size() == 0, "Empty queue does not have size 0 but it should"
    
    vals = [15,16,17,18]
    for v in vals: q.enqueue(v)
    assert q.size() == 4, "After 4 values are enqueued, the queue does not have size 4 but it should"
    assert q.dequeue() == 15, "The value returned from dequeue is not 15 but it should be"
    assert q.size() == 3, "After 1 value is dequeued, the queue does not have size 3 but it should"
    for i in range(3): q.dequeue()
    assert q.size() == 0, "After all 4 values enqueued are dequeued, the queue does not have size 0 but it should"
    
    try:
        q.dequeue()
    except IndexError as error:
        print("Exception caught when trying to dequeue from empty queue: " + str(error))
        return None