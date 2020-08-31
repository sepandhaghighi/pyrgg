
from collections import namedtuple
from decimal import Decimal
import pytest
import random

from pyrgg.functions import (
    get_precision,
    is_float,
    weight_str_to_number,
    convert_bytes,
    filesize,
    time_convert,
    input_filter,
    sign_gen,
    branch_gen,
    edge_gen,
)


@pytest.mark.parametrize("number, expected", [
    (1.2, 1),
    (1.12, 2),
    (1.0002, 4),
    (10, 0),
    (10.1, 1),
    (10.02, 2),
    (10.20, 1),  # or should it be 2?
    (10.234, 3),
    (Decimal('99.9999'), 4),
    ('string', 0),
])
def test_get_precision(number, expected):
    assert expected == get_precision(number)


@pytest.mark.parametrize("number, expected", [
    (1, False),
    (1.2, True),
    (2.0, True),
    (None, False),
    ('1.2', True),  # consider input '1.2' to be a float
    ('text', False),
])
def test_is_float(number, expected):
    assert expected == is_float(number)


@pytest.mark.parametrize("weight_str, expected", [
    ('1', 1),
    ('1.2', 1.2),
])
def test_weight_str_to_number(weight_str, expected):
    assert expected == weight_str_to_number(weight_str)


@pytest.mark.parametrize("number, expected", [
    (200, "200.0 bytes"),
    (1024, "1.0 KB"),
    (1025, "1.0 KB"),
    (1500, "1.5 KB"),
    (2047, "2.0 KB"),
    (2048, "2.0 KB"),
    (6000, "5.9 KB"),
    (80000, "78.1 KB"),
    (1048576, "1.0 MB"),
    (1073741824, "1.0 GB"),
    (1_099_511_627_776, "1.0 TB"),
    (10_995_116_277_760, "10.0 TB"),
    (109_951_162_777_600, "100.0 TB"),
    (1_125_899_906_842_623, "1024.0 TB"),  # just one byte below 1024 TB.
    pytest.param(
        1_125_899_906_842_624, "1024.0 TB",
        marks=pytest.mark.xfail(reason="bug in the function")
    ),
])
def test_convert_bytes(number, expected):
    assert expected == convert_bytes(number)


@pytest.mark.skip(reason="Function just prints and does not return")
def test_filesize(tmpdir):
    p = tmpdir.join("tmp_file.txt")
    p.write("1")
    assert filesize(p) == "1.0 bytes"


class TestTimeConvert:
    @pytest.mark.parametrize("input_string, expected", [
        ("0", "00 days, 00 hour, 00 minutes, 00 seconds"),
        ("0.1", "00 days, 00 hour, 00 minutes, 00 seconds"),
        ("1", "00 days, 00 hour, 00 minutes, 01 seconds"),
        ("33", "00 days, 00 hour, 00 minutes, 33 seconds"),
        ("62", "00 days, 00 hour, 01 minutes, 02 seconds"),
        ("125", "00 days, 00 hour, 02 minutes, 05 seconds"),
        ("3725", "00 days, 01 hour, 02 minutes, 05 seconds"),
        ("15000", "00 days, 04 hour, 10 minutes, 00 seconds"),
        ("90125", "01 days, 01 hour, 02 minutes, 05 seconds"),
        ("176525", "02 days, 01 hour, 02 minutes, 05 seconds"),
    ])
    def test_time_convert_normal(self, input_string, expected):
        assert expected == time_convert(input_string)

    @pytest.mark.parametrize("input_string", [
        "asdfasdfsd", "1 sec", "one minute is 60 sec",
    ])
    def test_time_convert_raises(self, input_string):
        with pytest.raises(ValueError, match='could not convert'):
            time_convert(input_string)


class TestInputFilter:
    Case = namedtuple('Case', ['input_dict', 'expected'])

    case_1 = Case(
        input_dict={
            "file_name": "test",
            "vertices": 5,
            "max_weight": 1000,
            "min_weight": 455,
            "max_edge": -11,
            "min_edge": -45,
            "sign": 5,
            "output_format": 19,
            "direct": 2,
            "self_loop": 2,
            "multigraph": 2,
        },
        expected={
            'file_name': 'test',
            'vertices': 5,
            'max_weight': 1000,
            'min_weight': 455,
            'max_edge': 5,
            'min_edge': 5,
            'sign': 2,
            'output_format': 1,
            "direct": 2,
            "self_loop": 2,
            "multigraph": 2,
        },
    )

    case_2 = Case(
        input_dict={
            "file_name": "test2",
            "vertices": 23,
            "max_weight": 2,
            "min_weight": 80,
            "max_edge": 1,
            "min_edge": 23,
            "sign": 1,
            "output_format": 1,
            "direct": 2,
            "self_loop": 10,
            "multigraph": 10,
        },
        expected={
            'file_name': 'test2',
            'vertices': 23,
            'max_weight': 80,
            'min_weight': 2,
            'max_edge': 23,
            'min_edge': 1,
            'sign': 1,
            'output_format': 1,
            "direct": 2,
            "self_loop": 1,
            "multigraph": 1,
        },
    )

    @pytest.mark.parametrize("case", [
        case_1, case_2
    ])
    def test_input_filter(self, case):
        assert case.expected == input_filter(case.input_dict)


@pytest.mark.parametrize("seed, expected", [
    (0, -1),
    (2, 1),
    (11, -1),
    (9000, -1),
    (42, 1),
    (100500, -1),
    (146, 1),
])
def test_sign_gen(seed, expected):
    random.seed(seed)
    assert expected == sign_gen()


class TestBranchGen:
    Case = namedtuple('Case', ['seed', 'args', 'expected'])

    all_vertices = list(range(1, 41))
    used_vertices = {k: [] for k in all_vertices}

    case_1 = Case(
        seed=2,
        args=(1, 10, 1, 20, 1, 1, 1, 1, all_vertices, used_vertices),
        expected=[
            [4, 25, 18, 3, 30, 34, 2, 26, 14, 11],
            [3, 10, 20, 14, -18, -2, -15, -14, 8, 6],
        ],
    )

    case_2 = Case(
        seed=20,
        args=(1, 4, 1, 20, 2, 1, 1, 1, all_vertices, used_vertices),
        expected=[
            [10, 7, 39, 2],
            [9, 11, 6, 14],
        ],
    )

    @pytest.mark.parametrize(
        "case, description", [
            (case_1, "first case"),
            (case_2, "second case"),
        ]
    )
    def test_branch_gen(self, case, description):
        random.seed(case.seed)
        result = branch_gen(*case.args)
        assert case.expected == result

    def test_missing_args_raises(self):
        with pytest.raises(TypeError):
            branch_gen(40, 1, 20, 1)


class TestEdgeGen:
    Case = namedtuple('Case', ['seed', 'args', 'expected'])

    case_1 = Case(
        seed=2,
        args=(20, 0, 400, 2, 10, 1, 1, 1, 1),
        expected=[
            {
                1: [3, 7],
                2: [20, 6, 14, 17, 1],
                3: [13, 6, 9, 14, 16, 18, 11],
                4: [12, 14, 19, 9, 15, 6, 16],
                5: [20, 16, 18, 7],
                6: [20, 1, 5, 3, 11, 13, 7],
                7: [2, 13, 1, 5, 3, 7, 8, 17],
                8: [2, 5, 18, 17],
                9: [20, 8, 12, 17, 15, 6, 5, 10],
                10: [5, 2, 8, 11, 12, 7, 6, 18, 16, 1],
                11: [4, 5, 8, 10],
                12: [15, 13, 7, 20, 2, 12, 16, 1, 9],
                13: [10, 15, 11, 1, 18, 5, 7],
                14: [3, 17, 13, 18, 14, 6],
                15: [20, 13, 4],
                16: [2, 13, 14, 20, 17, 6, 4, 8, 18],
                17: [3, 19, 4],
                18: [5, 9],
                19: [17, 5, 12, 20],
                20: [15, 12, 17, 14]
            },
            {
                1: [184, -128],
                2: [297, -326, -278, -18, -238],
                3: [-269, 120, 90, 69, 228, -376, -303],
                4: [-82, -335, 250, -256, -236, -249, 166],
                5: [-395, -155, -159, -262],
                6: [174, 381, 294, -302, 386, 136, 30],
                7: [185, 127, 58, 20, -130, 376, 197, 126],
                8: [176, -172, 157, 135],
                9: [242, 338, 12, 265, -263, 174, -310, 358],
                10: [129, 82, 232, 126, -37, 302, -131, -142, 77, -209],
                11: [123, 10, 53, 266],
                12: [-274, 350, -217, 297, -268, 48, -187, 312, -353],
                13: [350, 53, 396, -30, -237, 2, 190],
                14: [386, 59, -366, 385, -62, 62],
                15: [-328, 354, 316],
                16: [-148, -72, -247, -368, -348, -118, -305, -356, 299],
                17: [-90, 213, 348],
                18: [-199, -224],
                19: [-57, -49, 366, -86],
                20: [206, 238, 304, 201],
            },
            113,
        ],
    )

    case_2 = Case(
        seed=11,
        args=(20, 0, 100, 2, 10, 2, 1, 1, 1),
        expected=[
            {
                1: [18, 15, 19, 7, 20, 11, 2, 6, 3],
                2: [20, 15],
                3: [20, 17, 2, 8],
                4: [15, 16],
                5: [17, 10, 1, 4, 12],
                6: [3, 10, 9, 13, 4, 18, 11, 7, 2, 20],
                7: [7, 17, 14, 3, 9],
                8: [11, 10, 1, 5, 12, 3],
                9: [15, 6],
                10: [7, 18, 5, 15, 16, 4, 8, 9, 6, 13],
                11: [2, 8, 11],
                12: [10, 3, 4, 11, 16, 14, 5],
                13: [19, 13, 5, 9, 10, 4, 17, 14, 18],
                14: [20, 14, 4, 2, 11, 16, 9, 10, 13],
                15: [6, 3, 10, 4, 11, 17, 2, 13, 8, 1],
                16: [12, 20, 3, 6, 14, 16],
                17: [19, 20, 1, 13, 11, 2, 15, 10, 18, 8],
                18: [3, 19, 2],
                19: [11, 3, 18, 16],
                20: [19, 13, 1, 4, 5, 3, 11, 10, 20]
            },
            {
                1: [99, 57, 75, 23, 80, 23, 57, 18, 68],
                2: [50, 83],
                3: [1, 8, 4, 30],
                4: [41, 75],
                5: [29, 63, 84, 58, 52],
                6: [90, 40, 65, 3, 72, 13, 13, 49, 2, 0],
                7: [6, 48, 53, 72, 99],
                8: [11, 42, 52, 17, 90, 1],
                9: [62, 87],
                10: [57, 24, 53, 14, 53, 0, 75, 2, 23, 77],
                11: [18, 56, 1],
                12: [49, 9, 26, 1, 47, 58, 75],
                13: [17, 23, 39, 78, 92, 20, 80, 25, 49],
                14: [10, 6, 13, 65, 30, 90, 32, 76, 37],
                15: [92, 16, 61, 35, 26, 2, 34, 57, 7, 22],
                16: [67, 16, 46, 57, 84, 88],
                17: [17, 4, 60, 89, 4, 76, 9, 8, 39, 17],
                18: [57, 47, 94],
                19: [45, 87, 9, 3],
                20: [1, 48, 77, 10, 81, 32, 93, 49, 88],
            },
            125
        ],
    )

    @pytest.mark.parametrize("case, description", [
        (case_1, "first case"),
        (case_2, "second case"),
    ])
    def test_edge_gen(self, case, description):
        random.seed(case.seed)
        result = edge_gen(*case.args)
        assert case.expected == result

    def test_missing_args_raises(self):
        with pytest.raises(TypeError):
            edge_gen(0, 400, 2, 10, 1)
