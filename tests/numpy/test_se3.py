from pylie import SE3 as G
import numpy as np
import common


def test_wedge_vee():
    common._test_wedge_vee(G)


def test_exp():
    common._test_exp(G)


def test_log():
    common._test_log(G)


def test_exp_log_inverse():
    common._test_exp_log_inverse(G)


def test_odot_wedge():
    common._test_odot_wedge(G)


# def test_group_jacobians():
#     common._test_left_jacobian_inverse(G)
