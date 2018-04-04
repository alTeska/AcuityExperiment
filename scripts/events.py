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


def chain_events(events, log=True, motive_client=None):
    def init_next_event():
        event = events.popleft()
        event.next()
        # if log and motive_client:
        #     event_data = event.gi_frame.f_locals
        #     args = {var: event.gi_frame.f_locals[var]  for var in event.gi_code.co_varnames[:event.gi_code.co_argcount]}
        #     print(event_data, args)
        #
        #     logging.warn('{mot_time}; {fun_name}; {args}'.format(mot_time=motive_client.timestamp_recording, fun_name=event.__name__,
        #                                                            args=args))
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
