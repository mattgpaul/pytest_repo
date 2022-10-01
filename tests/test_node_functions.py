from node.node_functions import manage_thread, parse_data, do_another_thing, fail_at_a_thing
import pytest
from pytest import mark


@mark.parametrize("test_input, expected", [
    (1, 1),
    (2, 2),
    (12345, 12345),
])
def test_manage_thread_prints_information(test_input, expected):
    assert manage_thread(test_input) == expected
    
    
def test_manage_thread_invalid_input():
    with pytest.raises(ValueError):
        manage_thread(1.234)

    
def test_data_parses_string_into_dictionary(input='a dict key'):
    assert type(parse_data(input)) is dict


@mark.skip(reason='have not implemented this yet')
def test_do_another_thing_skips():
    assert do_another_thing == True   

    
@mark.xfail
def test_fail_at_a_thing():
    assert False


@mark.skip(reason='functionality not implemented yet')
def test_serial_connection(class_connection):
    class_connection.read_data()
    assert True