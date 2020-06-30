from etiquette import get_lowest_exposure, print_stalls, run_cycles, initialise
from tests.fixtures.classes import *


def test_get_lowest_exposure(mock_stall_obj_list):
    exposures = [3, 4, 2, 5, 1]
    stalls = mock_stall_obj_list(len(exposures))
    stall_row = StallRow()
    for i, stall in enumerate(stalls):
        stall.exposure = exposures[i]
    lowest = get_lowest_exposure()
    assert False
