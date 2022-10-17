import threading


class Task:
    def __init__(self, task=None):
        self.task = task
        self.next = None


class TPool:

    def __init__(self, p_size=1):
        self.pool_size = p_size

        self.mutex_lock = threading.Lock()

        self.task_end = None
        self.task_head = None

        self.task_assigned = 0

    def thread_task_lookup(self):
        while True:
            self.mutex_lock.acquire()
            t = self.dequeue_task()
            self.mutex_lock.release()

            if (t != None):
                t()

    def enueue_task(self, task):
        if self.task_head == None:
            self.task_head = Task(task)
            self.task_end = self.task_head

        else:
            self.task_end.next = Task(task)
            self.task_end = self.task_end.next

    def dequeue_task(self):
        if self.task_head == None:
            return None

        else:
            temp = self.task_head.task

            self.task_head = self.task_head.next

            if self.task_head == None:
                self.task_end = None

            self.task_assigned += 1
            print(f"Task Assigned {self.task_assigned}")
            
            return temp

    def start_pool(self):
        for i in range(self.pool_size):
            t = threading.Thread(target=self.thread_task_lookup)
            print(f'Thread {i}: starting')
            t.start()
