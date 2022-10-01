
def manage_thread(serial_port: int):
    if type(serial_port) is not int:
        raise ValueError("serial_port must be an integer")
    connection_info = serial_port
    return connection_info


def parse_data(input: str):
    parsed = {input: 'you did it!'}
    return parsed


def do_another_thing():
    pass


def fail_at_a_thing():
    pass
