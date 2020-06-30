import pytest
from modules.classes import UrinalSession, StallRow, Stall


@pytest.fixture
def mock_stall_obj_list():
    def _mock_stall_obj_list(stall_count):
        return [Stall(stall) for stall in range(stall_count)]
    return _mock_stall_obj_list


@pytest.fixture
def mock_times_stall_obj_list():
    def _set_times(stalls, times):
        for i, stall in enumerate(stalls):
            stall.time = times[i]
    return _set_times


@pytest.fixture
def mock_urinal_session_obj():
    def _mock_urinal_session_obj(cd, cc, ci, sc):
        return UrinalSession(cd, cc, ci, sc)
    return _mock_urinal_session_obj
