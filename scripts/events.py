from collections import deque


def update_attribute(var, attr, value):
    dt = yield
    setattr(var, attr, value)


def wait_duration(duration):
    total_time = duration
    curr_time = 0.
    while curr_time < total_time:
        dt = yield
        curr_time += dt


def change_scene_background_color(scene, color):
    dt = yield
    scene.bgColor = color


def chain_events(events):
    def init_next_event():
        event = events.popleft()
        next(event)
        return event

    events = deque(events)
    event = init_next_event()
    while True:
        dt = yield
        try:
            event.send(dt)
        except StopIteration:
            try:
                event = init_next_event()
            except IndexError:
                raise StopIteration
