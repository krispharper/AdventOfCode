from abc import ABC, abstractmethod
from dataclasses import dataclass

from common.input_data import parse_input, parse_int_str


@dataclass(frozen=True)
class Range:
    start: int
    end: int


@dataclass(frozen=True)
class RangeMap:
    source_range: Range
    destination_range: Range


@dataclass(frozen=True)
class CategoryMap:
    source: str
    destination: str
    ranges: list[RangeMap]

    def map_value(self, value: int) -> int:
        for range in self.ranges:
            if range.source_range.start <= value <= range.source_range.end:
                return range.destination_range.start + (value - range.source_range.start)

        return value


class Parser(ABC):
    _START_CATEGORY = "seed"
    _END_CATEGORY = "location"

    def __init__(self):
        self.data = parse_input(__file__)
        self.seeds: list[tuple[int, int]] = self._parse_seeds()
        self.category_maps: dict[str, CategoryMap] = {}

    def parse(self) -> None:
        self._parse_category_maps()

        min_value = 1e20

        for seed, length in self.seeds:
            for offset in range(seed, seed + length):
                min_value = min(min_value, self._process_seed_value(offset))

        print(min_value)

    @abstractmethod
    def _parse_seeds(self) -> list[tuple[int, int]]:
        pass

    def _parse_category_maps(self):
        row_groups = self._parse_row_groups()

        for row_group in row_groups:
            self._parse_category_map(row_group)

    def _parse_row_groups(self) -> list[list[str]]:
        row_groups = []
        row_group = []

        for line in self.data[2:]:
            if not line:
                row_groups.append(row_group)
                row_group = []
            else:
                row_group.append(line)

        row_groups.append(row_group)

        return row_groups

    def _parse_category_map(self, row_group: list[str]) -> None:
        categories_str, _ = row_group[0].split(" ")
        source, _, destination = categories_str.split("-")

        self.category_maps[source] = CategoryMap(
            source=source,
            destination=destination,
            ranges=[Parser._parse_range_map(range_map) for range_map in row_group[1:]],
        )

    @staticmethod
    def _parse_range_map(range_map: str) -> RangeMap:
        destination_start, source_start, length = parse_int_str(range_map)

        return RangeMap(
            source_range=Range(source_start, source_start + length - 1),
            destination_range=Range(destination_start, destination_start + length - 1),
        )

    def _process_seed_value(self, seed: int) -> int:
        current_value = seed
        current_map = self.category_maps[Parser._START_CATEGORY]

        while current_map.destination != Parser._END_CATEGORY:
            current_value = current_map.map_value(current_value)

            # Set new map based on the current destination
            current_map = self.category_maps[current_map.destination]

        current_value = current_map.map_value(current_value)

        return current_value
