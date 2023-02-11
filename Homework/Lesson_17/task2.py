# Task 2
# Implement 2 classes, the first one is the Boss and the second one is the Worker.
# Worker has a property 'boss', and its value must be an instance of Boss.
# You can reassign this value, but you should check whether the new value is Boss. Each Boss has a list of his
# own workers. You should implement a method that allows you to add workers to a Boss. You're not allowed to add
# instances of Boss class to workers list directly via access to attribute, use getters and setters instead!
# You can refactor the existing code.


class Boss:

    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company
        self.workers = []

    def __repr__(self):
        return self.name


class Worker:

    def __init__(self, id_: int, name: str, company: str, boss: Boss):
        self.id = id_
        self.name = name
        self.company = company
        self._boss = boss
        boss.workers.append(self)

    def __repr__(self):
        return self.name

    def get_boss(self):
        return self._boss

    def set_boss(self, new_boss):
        self._boss.workers.remove(self)
        self._boss = new_boss
        new_boss.workers.append(self)


boss_1 = Boss(123, 'Michael Scott', 'Dunder Mifflin')
worker_1 = Worker(456, 'Jim Halpert', boss_1.company, boss_1)

boss_2 = Boss(789, 'Gerry Smith', 'Office Depot')
worker_2 = Worker(1112, 'Pam Morgan', boss_2.company, boss_2)

print(boss_2.workers)
print(boss_1.workers)
