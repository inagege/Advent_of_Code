class MappingOfNumbers:

    def __init__(self, array_mapping: list[list[list[int]]]):
        self.destination_range_start: list[list[int]] = []
        self.source_range_start: list[list[int]] = []
        self.range_length: list[list[int]] = []

        for mapping_id, mapping in enumerate(array_mapping):
            self.destination_range_start.append(mapping[0])
            self.source_range_start.append(mapping[1])
            self.range_length.append(mapping[2])

    def mapp_seed(self, seed: list[int]):
        mapped_seeds = []
        for element in seed:
            for index_maps, maps in enumerate(self.source_range_start):
                new = False
                for k, source in enumerate(maps):
                    if element in range(source, source + self.range_length[index_maps][k]) and not new:
                        element = self.destination_range_start[index_maps][k] + element - source
                        new = True
            mapped_seeds.append(element)

        return mapped_seeds


with open('input') as f:
    lines = f.readlines()

i = -1
all_mapping: list[list[list[int]]] = []

seeds = lines.pop(0)
seeds = seeds.split(':')[1]
seeds = seeds.split('\n')[0]
seeds = seeds.split(' ')[1:]
seeds = [int(element) for element in seeds]

for line in lines:
    if line[0].isalpha():
        i = i + 1
        all_mapping.append([[], [], []])
    else:
        if line[0].isdigit():
            without_new_line = line.split('\n')[0]
            temp = without_new_line.split(' ')
            for i_e, element in enumerate(temp):
                all_mapping[i][i_e].append(int(element))


print(min(MappingOfNumbers(all_mapping).mapp_seed(seeds)))

