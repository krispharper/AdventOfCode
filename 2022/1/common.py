from common.input_data import parse_input


def sum_row_groups(rows: list[str]) -> list[int]:
    results = []
    current_number = 0

    for row in rows:
        if not row:
            results.append(current_number)
            current_number = 0
            continue

        current_number += int(row)

    results.append(current_number)

    return results


def get_top_groups(limit: int) -> int:
    groups = sum_row_groups(parse_input(__file__))
    return sum(sorted(groups)[-limit:])
