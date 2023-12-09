from common.input_data import parse_input, parse_int_str
from .common import main, Race


def _parse_input() -> list[Race]:
    times_str, records_str = parse_input(__file__)

    times = parse_int_str(times_str.split(":")[1])
    records = parse_int_str(records_str.split(":")[1])

    return [Race(t, r) for t, r in zip(times, records)]


if __name__ == "__main__":
    main(_parse_input)
