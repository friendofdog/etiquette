import pytest
from modules.classes import Stall


@pytest.fixture
def mock_stall_obj_list():
    def _mock_stall_obj_list(stall_count):
        return [Stall(stall) for stall in range(stall_count)]
    return _mock_stall_obj_list


@pytest.fixture
def set_times_stall_obj_list():
    def _set_times(stalls, times):
        for i, stall in enumerate(stalls):
            stall.time = times[i]
    return _set_times
