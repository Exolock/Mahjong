import numbers

from .informat import parse_command_line, get_options
from .maxpoints import make_one_fan_per_line, add_exclusion_columns, optimal_claimed_fans, score_of_claimed, max_points_of_option
from .identifan import get_fans
from .fannames import get_fan_name


def get_mahjong(sit):
    sit = parse_command_line(sit)
    opts = get_options(sit)

    opts.sort(key=max_points_of_option)
    opts.reverse()

    max_mahjong = opts[0]
    sets = max_mahjong['sets']
    fans = get_fans(max_mahjong)
    point_fans = make_one_fan_per_line(fans)
    exclusion_fans = add_exclusion_columns(point_fans, sets)
    claimed_fans = optimal_claimed_fans(exclusion_fans)
    claimed_fans_data = [[
        point_fans[index][0],
        get_fan_name(point_fans[index][1]),
        [
            [sit['w']] if isinstance(set_index, bool)
            else sets[set_index][1] if isinstance(set_index, numbers.Number)
            else point_fans[index][2]
            for set_index in point_fans[index][2]
        ]
    ] for index in optimal_claimed_fans(exclusion_fans)]
    score = score_of_claimed(exclusion_fans, claimed_fans)

    return {
        'fans': claimed_fans_data,
        'situation': sit,
        'score': score,
        'sets': sets
    }
