from tests.fixtures.classes import *


@pytest.mark.parametrize(
    "dur, exp", [(20, [70, 50, 115, 15]), (30, [46, 33, 76, 10])]
)
def test_set_exposure(dur, exp, mock_stall_obj_list, set_times_stall_obj_list):
    """
    Test that exposure is correctly calculated based on neighbouring stalls'
    times. Including first and last stalls, as these are calculated differntly
    than stalls with two neighbours.
    """
    times = (7, 14, 3, 9)
    stalls = mock_stall_obj_list(len(times))
    set_times_stall_obj_list(stalls, times)
    for i, stall in enumerate(stalls):
        stall.set_exposure(dur, stalls)
        assert int(stall.exposure) == exp[i]


@pytest.mark.parametrize("time_now, time_new", [(5, 4), (0, 0)])
def test_decrememt_time(set_times_stall_obj_list, time_now, time_new):
    """
    Test that time property of Stall object has either been decremented by 1,
    if it initially was >1, or otherwise remains at initial value.
    """
    stall = Stall(0)
    set_times_stall_obj_list([stall], [time_now])
    stall.decrememt_time()
    assert stall.time == time_new


@pytest.mark.parametrize("time_now, time_new", [
    (0, 20), pytest.param(1, 20, marks=pytest.mark.xfail)
])
def test_add_occupant(time_now, time_new):
    """
    Test that time prop of Stall object has been set to provided duration,
    provided that the value was already zero. add_occupant() should never be
    called when time is >0, so also included failing test when time >0.
    """
    stall = Stall(0)
    stall.time = time_now
    stall.add_occupant(time_new)
    assert stall.time == time_new
