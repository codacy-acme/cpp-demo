import gc
import tracemalloc

found_objects = gc.get_objects()
print('%d objects before' % len(found_objects))
ref = 'Sarah ' * 512000
found_objects = gc.get_objects()
print('%d objects after' % len(found_objects))
for obj in found_objects[:3]:
    print(repr(obj)[:100])
    
    

tracemalloc.start(5)  # save upto 5 stack frames
time1 = tracemalloc.take_snapshot()
ref = 'Sarah ' * 51200
time2 = tracemalloc.take_snapshot()
stats = time2.compare_to(time1, 'lineno')
for stat in stats[:3]:
    print(stat)
