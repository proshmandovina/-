from dataclasses import dataclass
from typing import List
from collections import defaultdict

@dataclass
class CD:
    cd_id: int
    name: str
    series: str
    library_id: int  # Связь один-ко-многим

@dataclass
class Library:
    library_id: int
    name: str

@dataclass
class CDLibraryLink:
    cd_id: int
    library_id: int  # Связь многие-ко-многим

# Тестовые данные
libraries = [
    Library(library_id=1, name="Альфа"),
    Library(library_id=2, name="Вегас"),
    Library(library_id=3, name="Самса"),
]

cds = [
    CD(cd_id=1, name="популярная песня", series="акустика", library_id=1),
    CD(cd_id=2, name="любимая классика", series="оркестр", library_id=2),
    CD(cd_id=3, name="поп хиты", series="чарты", library_id=1),
    CD(cd_id=4, name="электрические мечты", series="синх", library_id=3),
    CD(cd_id=5, name="чиллибас", series="чиллик", library_id=3),
]

cd_library_links = [
    CDLibraryLink(cd_id=1, library_id=1),
    CDLibraryLink(cd_id=2, library_id=2),
    CDLibraryLink(cd_id=3, library_id=1),
    CDLibraryLink(cd_id=4, library_id=3),
    CDLibraryLink(cd_id=5, library_id=3),
]

# 1. Список всех CD-дисков, заканчивающихся на "ы", и названия их библиотек
print("1. CD-диски, название которых заканчивается на 'ы', и их библиотеки:")
for cd in cds:
    if cd.name.endswith("ы"):  # Проверяем окончание на "ы"
        library_name = next((lib.name for lib in libraries if lib.library_id == cd.library_id), "неизвестен")
        print(f"CD: {cd.name}, Библиотека: {library_name}")

# 2. Список библиотек со средней длиной названия CD-дисков в каждой библиотеке
print("\n2. Список библиотек со средней длиной названия CD-дисков:")
library_lengths = defaultdict(list)
for cd in cds:
    library_lengths[cd.library_id].append(len(cd.name))

avg_library_lengths = []
for library_id, lengths in library_lengths.items():
    avg_length = sum(lengths) / len(lengths)
    library_name = next((lib.name for lib in libraries if lib.library_id == library_id), "Unknown")
    avg_library_lengths.append((library_name, avg_length))

avg_library_lengths.sort(key=lambda x: x[1], reverse=True)  # Сортировка по средней длине
for library_name, avg_length in avg_library_lengths:
    print(f"Библиотека: {library_name}, Средняя длина названия: {avg_length:.2f}")

# 3. Список библиотек с названием на "А" и CD-дисков в них (многие-ко-многим)
print("\n3. Библиотеки с названием на 'А' и CD-диски в них:")
for library in libraries:
    if library.name.startswith("А"):  # Проверяем начало названия на "А"
        linked_cd_ids = [link.cd_id for link in cd_library_links if link.library_id == library.library_id]
        linked_cds = [cd.name for cd in cds if cd.cd_id in linked_cd_ids]
        print(f"Библиотека: {library.name}, CD-диски: {', '.join(linked_cds)}")
