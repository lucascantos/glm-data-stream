import pytest
from handler import glm_data

def test_glm_data():
    event = {
        'debug': True,
        'path': 'tests/sample/OR_GLM-L2-LCFA_G16_s20211041500000_e20211041500204_c20211041500226.nc'
    }
    assert glm_data(event)