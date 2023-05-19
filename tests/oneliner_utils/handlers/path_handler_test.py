from pathlib import Path

import pytest

from unified_io import join_path


# FIXTURES =====================================================================
@pytest.fixture
def x():
    return "black"


@pytest.fixture
def y():
    return "sabbath"


@pytest.fixture
def z():
    return "doom"


# TESTS ========================================================================
def test_join_path(x, y, z):
    joined = join_path(x, y, z)
    assert joined == Path("black/sabbath/doom")
