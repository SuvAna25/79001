class Stack:

    def __init__(self):
        self.lst_task = []

    def add_task(self, task: str) -> None:
        self.lst_task.append(task)

    def delete_task(self, task: str) -> None:
        self.lst_task.remove(task)

    def __str__(self) -> str:
        return f'{"; ".join(self.lst_task)}'


class TaskManager:

    def __init__(self, dct_task=None):
        if dct_task is None:
            dct_task = {}
        self.dct_task = dct_task

    def new_task(self, task: str, key: int) -> None:
        if not self.dct_task.get(key):
            self.dct_task[key] = Stack()
            self.dct_task.setdefault(key, []).add_task(task)
        else:
            if task in str(self.dct_task[key]):
                key += 1
                self.dct_task[key] = Stack()
            self.dct_task.setdefault(key, []).add_task(task)

    def remove_task(self, task: str) -> None:
        for key, val in self.dct_task.items():
            if task in str(val):
                self.dct_task[key].delete_task(task)
                break
        else:
            print(f'Задачи - {task} в списке приоритетов нет')

        copy_dct = self.dct_task.copy()
        for key in copy_dct.keys():
            if len(str(copy_dct[key])) == 0:
                self.dct_task.pop(key)

    def __str__(self) -> str:
        return "; \n".join(f'{key}: {val}' for key, val in sorted(self.dct_task.items()))


manager = TaskManager()

manager.remove_task("погулять с собакой")
manager.new_task("сделать уборку", 4)
manager.new_task("помыть посуду", 4)
manager.new_task("отдохнуть", 1)
manager.new_task("поесть", 2)
manager.new_task("сдать ДЗ", 2)
print(manager)
print()
manager.new_task("сделать уборку", 4)
manager.remove_task("отдохнуть")
manager.remove_task("погулять")

print(manager)