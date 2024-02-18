"""Sample test file

This sample test file provides a rough structure to base tests around.
It is NOT a functioning script.

Tests written using the pytest framework can easily be run together or as a
group. Pytest automatically searches for files and functions within them
prefixed with `test_`.
"""
# These modules aren't included in the default Pipfile
# Add using `pipenv install <module>` if required
import pytest
from faker import Faker

# Initialise Faker class if being used to generate random test data
# https://faker.readthedocs.io/en/latest/index.html
fake = Faker()


def sample_function(dictionary):
    """Basic function to demonstrate Pytest

    Ordinarily functions to test would be imported from another script.

    Parameters
    ----------
    dictionary : dict
        Dictionary with values that can be converted to INTs

    Returns
    -------
    list
        List of INTs
    """
    int_list = []
    for i in dictionary.values():
        int_list.append(int(i))

    return int_list


#############
# Constants #
#############

# Put any constants like sample data paths, initialisation variables etc here
TEST_ITERATIONS = 5


############
# Fixtures #
############

# Fixtures can be used to create setup functions that can be used by several
# tests to prevent having to repeat the setup for each

@pytest.fixture
def optionally_customised_data_sample():
    """Fixture the returns a varibales dictionary

    Fixture that returns a predefined dictionary of variables, or can be
    updated with provided key word arguments.

    This structure is useful for on the fly generation of data formats with
    faked variables.

    Returns
    -------
    dict
        Dictionary with 2 properties, either defaults of INTs as STRs, or
        replaced with optionally passed values.
    """
    def _optionally_customised_data_sample(**kwargs):
        variables = {
            "property_1": "10",
            "property_2": "24",
        }

        variables.update(**kwargs)

        return variables

    return _optionally_customised_data_sample


#########
# Tests #
#########

class TestSample:
    @pytest.mark.parametrize("sample", [
        ["10", "0"],
        ["-20", 3],
        [9473, -211],
    ])
    def test_valid_sample_function(
        self,
        sample,
        optionally_customised_data_sample
    ):
        """Valid test example with defined inputs

        Parameters
        ----------
        sample : list
            List of INTs in INT or STR form
        optionally_customised_data_sample : fixture
            Fixture providing a DICT with 2 keys
        """
        # Replace values with known valid possibilities defined in decorator
        variables = optionally_customised_data_sample(
            property_1=sample[0],
            property_2=sample[1]
        )

        output = sample_function(variables)

        # Check each value in the list is an INT as intended for the function
        for i in output:
            assert isinstance(i, int)

    @pytest.mark.parametrize("repeat", range(TEST_ITERATIONS))
    def test_random_valid_sample_function(
        self,
        repeat,
        optionally_customised_data_sample
    ):
        """Valid test example with faked inputs repeated

        Parameters
        ----------
        repeat : range
            Range based on constant defined, how many times to repeat test
        optionally_customised_data_sample : fixture
            Fixture providing a DICT with 2 keys
        """
        # Replace values in dictionary with faked data known to be valid
        variables = optionally_customised_data_sample(
            property_1=str(fake.random_int()),
            property_2=fake.random_int()
        )

        output = sample_function(variables)

        # Check each value in the list is an INT as intended for the function
        for i in output:
            assert isinstance(i, int)

    @pytest.mark.parametrize("repeat", range(TEST_ITERATIONS))
    def test_random_invalid_sample_function(
        self,
        repeat,
        optionally_customised_data_sample
    ):
        """Invalid test example with faked inputs repeated

        Parameters
        ----------
        repeat : range
            Range based on constant defined, how many times to repeat test
        optionally_customised_data_sample : fixture
            Fixture providing a DICT with 2 keys
        """
        # Replace values in dictionary with faked data known to be invalid
        variables = optionally_customised_data_sample(
            property_1=fake.name(),
            property_2=fake.hex_color()
        )

        # Check function raises a ValueError when called with faked values
        with pytest.raises(ValueError):
            sample_function(variables)
