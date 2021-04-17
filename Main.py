from component.Tugas import *

Tugas('12', 'wqe', 'ewq', '213')
Tugas('12', 'wqe', 'ewq', '215')

for tugas in Tugas.list_tugas:
    print(tugas.id, tugas.topik_tugas)

