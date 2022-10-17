import thread_pool
import time

def test_task_gen(id):
    def test():
        print(f"exec task: {id}")
        time.sleep(3)
        print(f"done task: {id}")

    return test

if __name__ == "__main__":

    print("------ main thread -----")
    
    pool = thread_pool.TPool(3)
    
    pool.enueue_task(test_task_gen(1))
    pool.enueue_task(test_task_gen(2))

    pool.start_pool()

    pool.enueue_task(test_task_gen(3))
    pool.enueue_task(test_task_gen(4))
    pool.enueue_task(test_task_gen(5))
    pool.enueue_task(test_task_gen(6))
    pool.enueue_task(test_task_gen(7))


