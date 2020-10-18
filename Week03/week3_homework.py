from threading import Condition, Thread, Semaphore
from time import sleep
from random import choice

result = []


def pickLeftFork(a):
    print(f'哲学家 {a} 拿起左边叉子。')
    result.append([a, 1, 1])
    sleep(1)


def pickRightFork(a):
    print(f'哲学家 {a} 拿起右边叉子。')
    result.append([a, 2, 1])
    sleep(1)

def eat(a):
    print(f'哲学家 {a} 进餐中')
    result.append([a, 0, 3])
    sleep(choice([1, 2]))

def putLeftFork(a):
    print(f'哲学家 {a} 放下左边叉子。')
    result.append([a, 1, 2])
    sleep(1)


def putRightFork(a):
    print(f'哲学家 {a} 放下右边叉子。')
    result.append([a, 2, 2])
    sleep(1)


class DiningPhilosophers:

    def __init__(self):
        self.forks = [Semaphore() for _ in range(5)]

    def wantsToEat(self, philosopher: int, *actions) -> None:
        a, b = self.forks[philosopher], self.forks[(philosopher+1) % 5]
        with a:
            with b:
                list(map(lambda func: func(philosopher), actions))


if __name__ == '__main__':
    threads = []
    act = DiningPhilosophers()
    for i in range(5):
        t = Thread(target=act.wantsToEat, args=(i, pickLeftFork, pickRightFork, eat, putLeftFork, putRightFork))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    print(result)