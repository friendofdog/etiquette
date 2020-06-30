from tests.fixtures.classes import *


def test_set_exposure(mock_stall_obj_list, mock_times_stall_obj_list):
    """
    Test that exposure is correctly calculated based on neighbouring stalls'
    times. Including first and last stalls, as these are calculated differntly
    than stalls with two neighbours.
    """
    times = [7, 14, 3, 9]
    duration = 20
    exposures = [70, 50, 115, 15]
    stalls = mock_stall_obj_list(len(times))
    mock_times_stall_obj_list(stalls, times)
    for i, stall in enumerate(stalls):
        stall.set_exposure(duration, stalls)
        assert int(stall.exposure) == exposures[i]


@pytest.mark.parametrize("time, time_new", [
    (5, 4),
    (0, 0)
])
def test_decrememt_time(mock_times_stall_obj_list, time, time_new):
    """
    Test that time property of Stall object has either been decremented by 1,
    if it initially was >1, or otherwise remains at initial value.
    """
    stall = Stall(0)
    mock_times_stall_obj_list([stall], [time])
    stall.decrememt_time()
    assert stall.time == time_new


@pytest.mark.parametrize("time, time_new", [
    (0, 20),
    pytest.param(1, 20, marks=pytest.mark.xfail)
])
def test_add_occupant(time, time_new):
    """
    Test that time prop of Stall object has been set to provided duration,
    provided that the value was already zero. add_occupant() should never be
    called when time is >0, so also included failing test when time >0.
    """
    stall = Stall(0)
    stall.time = time
    stall.add_occupant(time_new)
    assert stall.time == time_new


def test_update_occupancy(mock_stall_obj_list, mock_times_stall_obj_list):
    """
    Test that stall row occupancy is being updated to reflect stalls with a
    time of >0.
    """
    times = [2, 0, 3, 0, 4]
    occupied = [0, 2, 4]
    stalls = mock_stall_obj_list(len(times))
    mock_times_stall_obj_list(stalls, times)
    stall_row = StallRow()
    stall_row.update_occupancy(stalls)
    assert stall_row.occupancy == occupied


@pytest.mark.parametrize("occupancy, interval, queue_new", [
    ([0, 1, 2, 3, 4], True, 1),
    ([0, 1, 2], True, 0),
    ([0, 1, 2, 3, 4], False, 0),
    ([0, 1, 2], False, 0)
])
def test_incrememt_queue(occupancy, interval, queue_new):
    """
    Tests that stall row occupancy increases by 1 in there is an interval and
    the row has not reached maximum occupancy. Testing all four conditions.
    """
    stall_row = StallRow()
    stall_count = 5
    stall_row.incrememt_queue(interval, occupancy, stall_count)
    assert stall_row.queued == queue_new


@pytest.mark.parametrize("queue, queue_new", [
    (1, 0),
    (0, 0)
])
def test_decrememt_queue(queue, queue_new):
    """
    Test that queued decreases by 1, if queue is already >0. Queued should
    never be a negative value.
    """
    stall_row = StallRow()
    stall_row.queued = queue
    stall_row.decrememt_queue()
    assert stall_row.queued == queue_new
