# -*- coding: utf-8 -*-
# test_realizeNTF.py
# This module provides the tests for the realizeNTF function.
# Copyright 2014 Giuseppe Venturini
# This file is part of python-deltasigma.
#
# python-deltasigma is a 1:1 Python replacement of Richard Schreier's
# MATLAB delta sigma toolbox (aka "delsigma"), upon which it is heavily based.
# The delta sigma toolbox is (c) 2009, Richard Schreier.
#
# python-deltasigma is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# LICENSE file for the licensing terms.

"""This module provides the test class for the realizeNTF() function.
"""

import unittest
import numpy as np
import deltasigma as ds

class TestRealizeNTF(unittest.TestCase):
    """Test class for realizeNTF()"""
    def setUp(self):
        self.orders = (2, 3, 4)
        self.osr = 32
        self.f0s = (0., 0.25)
        self.NG = (-40, -60, -80)
        self.rots = (0, 1)
        self.ING = (-5, -10, -20)
        self.forms = ('FB', 'PFB', 'FF', 'PFF')
        res = {}
        for i in self.orders:
            res.update({i:{}})
            for j in self.f0s:
                res[i].update({j:{}})
                for ng in self.NG:
                    res[i][j].update({ng:{}})
                    for ing in self.ING:
                        res[i][j][ng].update({ing:{}})
                        for rot in self.rots:
                            res[i][j][ng][ing].update({rot:{}})
                            for f in self.forms:
                                res[i][j][ng][ing][rot].update({f:None})
        #  ord f0  NG  ING rot form
        res[2][0.][-40][-5][0]['FB'] = \
            np.array([[0.998394049105901 + 0.0566508844584438j, 0.0 + 0.0j,
                       0.290115301207217 + 0.0j, -0.285423767274711 -
                       0.0519630740936901j],
                      [1.0 + 0.0j, 0.998394049105901 - 0.0566508844584438j,
                       0.0 + 0.0j, -0.917250888321215 + 3.08814715431770e-17j],
                      [0.0 + 0.0j, 1.0 + 0.0j,  0.0 + 0.0j, 0.0 + 0.0j]])
        res[2][0.][-40][-5][0]['PFB'] = \
            np.array([[0.998394049105901 + 0.0566508844584438j, 0.0 + 0.0j,
                       2.56055403177360 + 0.0j,
                       -0.458625444160605 + 2.51914661177164j],
                      [0.0 + 0.0j, 0.998394049105901 - 0.0566508844584438j,
                       0.0 + 0.0j, -0.458625444160610 - 2.51914661177164j],
                      [1.0 + 0.0j, 1.0 + 0.0j, 0.0 + 0.0j, 0.0 + 0.0j]])
        res[2][0.][-40][-5][0]['FF'] = \
            np.array([[0.998394049105901 + 0.0566508844584438j, 0.0 + 0.0j,
                       -1.0 + 0.0j,   1.0 + 0.0j],
                      [1.0 + 0.0j, 0.998394049105901 - 0.0566508844584438j,
                       0.0 + 0.0j,    0.0 + 0.0j],
                      [-0.917250888321215 - 2.06395320364824e-16j,
                       -0.285423767274711 + 0.0519630740936901j, 0.0 + 0.0j,
                       0.0 + 0.0j]])
        res[2][0.][-40][-5][0]['PFF'] = \
            np.array([[0.998394049105901 + 0.0566508844584438j, 0.0 + 0.0j,
                       1.0 + 0.0j, 1.0 + 0.0j],
                      [0.0 + 0.0j, 0.998394049105901 - 0.0566508844584438j,
                       0.0 + 0.0j, 1.0 + 0.0j],
                      [-0.458625444160608 + 2.51914661177164j,
                       -0.458625444160607 - 2.51914661177164j, 0.0 + 0.0j,
                       0.0 + 0.0j]])
        res[2][0.][-40][-10][0]['FB'] = \
            np.array([[0.998394049105901 + 0.0566508844584438j,  0.0 + 0.0j,
                       0.290115301207218 + 0.0j,
                       -0.285423767274711 - 0.0519630740936898j],
                      [1.0 + 0.0j, 0.998394049105901 - 0.0566508844584438j,
                       0.0 + 0.0j, -0.917250888321215 + 1.62469132395870e-16j],
                      [0.0 + 0.0j, 1.0 + 0.0j, 0.0 + 0.0j, 0.0 + 0.0j]])
        res[2][0.][-40][-10][0]['PFB'] = \
            np.array([[0.998394049105901 + 0.0566508844584438j, 0.0 + 0.0j,
                       2.56055403177360 + 0.0j,
                       -0.458625444160606 + 2.51914661177164j],
                      [0.0 + 0.0j, 0.998394049105901 - 0.0566508844584438j,
                       0.0 + 0.0j, -0.458625444160609 - 2.51914661177164j],
                      [1.0 + 0.0j, 1.0 + 0.0j, 0.0 + 0.0j, 0.0 + 0.0j]])

        res[2][0.][-40][-10][0]['FF'] = \
            np.array([[0.998394049105901 + 0.0566508844584438j, 0.0 + 0.0j,
                       -1.0 + 0.0j, 1.0 + 0.0j],
                      [1.0 + 0.0j, 0.998394049105901 -0.0566508844584438j,
                       0.0 + 0.0j, 0.0 + 0.0j],
                      [-0.917250888321215 + 3.39112800347523e-17j,
                       -0.285423767274711 + 0.0519630740936900j, 0.0 + 0.0j,
                       0.0 + 0.0j]])
        res[2][0.][-40][-10][0]['PFF'] = \
            np.array([[0.998394049105901 + 0.0566508844584438j, 0.0 + 0.0j,
                       1.0 + 0.0j, 1.0 + 0.0j],
                      [0.0 + 0.0j, 0.998394049105901 -0.0566508844584438j,
                       0.0 + 0.0j, 1.0 + 0.0j],
                      [-0.458625444160608 +2.51914661177164j,
                       -0.458625444160608 -2.51914661177164j, 0.0 + 0.0j,
                       0.0 + 0.0j]])

        res[2][0.][-40][-20][0]['FB'] = \
            np.array([[0.998394049105901 + 0.0566508844584438j, 0.0 + 0.0j,
                       0.290115301207218 + 0.0j,
                       -0.285423767274711 - 0.0519630740936902j],
                      [1.0 + 0.0j, 0.998394049105901 - 0.0566508844584438j,
                       0.0 + 0.0j, -0.917250888321215 + 1.25834638951827e-16j],
                      [0.0 + 0.0j, 1.0 + 0.0j, 0.0 + 0.0j, 0.0 + 0.0j]])
        res[2][0.][-40][-20][0]['PFB'] = \
            np.array([[0.998394049105901 + 0.0566508844584438j, 0.0 + 0.0j,
                       2.56055403177360 + 0.0j,
                       -0.458625444160607 + 2.51914661177164j],
                      [0.0 + 0.0j, 0.998394049105901 -0.0566508844584438j,
                       0.0 + 0.0j, -0.458625444160608 -2.51914661177164j],
                      [1.0 + 0.0j, 1.0 + 0.0j, 0.0 + 0.0j, 0.0 + 0.0j]])
        res[2][0.][-40][-20][0]['FF'] = \
            np.array([[0.998394049105901 +0.0566508844584438j, 0.0 + 0.0j,
                       -1.0 + 0.0j, 1.0 + 0.0j],
                      [1.0 + 0.0j, 0.998394049105901 - 0.0566508844584438j,
                       0.0 + 0.0j, 0.0 + 0.0j],
                      [-0.917250888321215 + 1.91627025153857e-16j,
                       -0.285423767274710 + 0.0519630740936903j, 0.0 + 0.0j,
                       0.0 + 0.0j]])
        res[2][0.][-40][-20][0]['PFF'] = \
            np.array([[0.998394049105901 + 0.0566508844584438j, 0.0 + 0.0j,
                      1.0 + 0.0j, 1.0 + 0.0j],
                     [0.0 + 0.0j, 0.998394049105901 - 0.0566508844584438j,
                      0.0 + 0.0j, 1.0 + 0.0j],
                     [-0.458625444160605 + 2.51914661177164j,
                      -0.458625444160611 - 2.51914661177164j, 0.0 + 0.0j,
                      0.0 + 0.0j]])

        res[2][0.][-40][-5][1]['FB'] = \
            np.array([[0.998394049105901 + 0.0566508844584438j, 0.0 + 0.0j,
                       0.290115301207217 + 0.0j,
                       0.290115301207217 + 6.93889390390723e-17j],
                      [0.983828726327138 + 0.179111800988996j,
                       0.998394049105901 - 0.0566508844584438j, 0.0 + 0.0j,
                       0.917250888321215 + 6.57660137200134e-17j],
                      [0.0 + 0.0j, -1.0 + 1.22464679914735e-16j, 0.0 + 0.0j,
                       0.0 + 0.0j]])
        res[2][0.][-40][-5][1]['PFB'] = \
            np.array([[0.998394049105901 + 0.0566508844584438j, 0.0 + 0.0j,
                       2.56055403177360 + 0.0j,
                       2.56055403177360 - 5.55111512312578e-17j],
                      [0.0 + 0.0j, 0.998394049105901 - 0.0566508844584438j,
                       0.0 + 0.0j, 2.56055403177361 + 3.88578058618805e-16j],
                      [-0.179111800988996 + 0.983828726327138j,
                       -0.179111800988998 - 0.983828726327138j, 0.0 + 0.0j,
                       0.0 + 0.0j]])
        res[2][0.][-40][-5][1]['FF'] = \
            np.array([[0.998394049105901 + 0.0566508844584438j, 0.0 + 0.0j,
                       -1.0 + 0.0j, 1.0 + 0.0j],
                      [1.0 + 0.0j, 0.998394049105901 - 0.0566508844584438j,
                       0.0 + 0.0j, 0.0 + 0.0j],
                      [-0.917250888321215 + 5.00242553063589e-17j,
                       -0.285423767274711 + 0.0519630740936901j, 0.0 + 0.0j,
                       0.0 + 0.0j]])
        res[2][0.][-40][-5][1]['PFF'] = \
            np.array([[0.998394049105901 + 0.0566508844584438j, 0.0 + 0.0j,
                       1.0 + 0.0j, 1.0 + 0.0j],
                      [0.0 + 0.0j, 0.998394049105901 - 0.0566508844584438j,
                       0.0 + 0.0j, 1.0 + 0.0j],
                      [-0.458625444160606 + 2.51914661177164j,
                       -0.458625444160609 -2.51914661177164j, 0.0 + 0.0j,
                       0.0 + 0.0j]])
        res[2][0.][-40][-10][1]['FB'] = \
            np.array([[0.998394049105901 + 0.0566508844584438j, 0.0 + 0.0j,
                       0.290115301207217 + 0.0j,
                       0.290115301207217 - 6.93889390390723e-18j],
                      [0.983828726327138 + 0.179111800988996j,
                       0.998394049105901 - 0.0566508844584438j, 0.0 + 0.0j,
                       0.917250888321215 + 2.00648216415878e-17j],
                      [0.0 + 0.0j, -1.0 + 1.22464679914735e-16j, 0.0 + 0.0j,
                       0.0 + 0.0j]])
        res[2][0.][-40][-10][1]['PFB'] = \
            np.array([[0.998394049105901 + 0.0566508844584438j, 0.0 + 0.0j,
                       2.56055403177360 + 0.0j,
                       2.56055403177360 - 4.44089209850063e-16j],
                      [0.0 + 0.0j, 0.998394049105901 -0.0566508844584438j,
                       0.0 + 0.0j, 2.56055403177360 + 3.88578058618805e-16j],
                      [-0.179111800988999 + 0.983828726327137j,
                       -0.179111800988996 - 0.983828726327138j, 0.0 + 0.0j,
                       0.0 + 0.0j]])
        res[2][0.][-40][-10][1]['FF'] = \
            np.array([[0.9984+0.0567j,  0.0000+0.j, -1.0000+0.j,  1.0000+0.j],
                      [1.0000+0.j,  0.9984-0.0567j,  0.0000+0.j,  0.0000+0.j],
                      [-0.9173+0.j, -0.2854+0.052j,  0.0000+0.j,  0.0000+0.j]])
        res[2][0.][-40][-10][1]['PFF'] = \
            np.array([[0.9984+0.0567j, 0.0000+0.j, 1.0000+0.j,  1.0000+0.j],
                      [0.0000+0.j, 0.9984-0.0567j, 0.0000+0.j,  1.0000+0.j],
                      [-0.4586+2.5191j, -0.4586-2.5191j,  0.0000+0.j,  0.0000+0.j]])
        res[2][0.][-40][-20][1]['FB'] = \
            np.array([[ 0.9984+0.0567j,  0.0000+0.j,  0.2901+0.j,  0.2901+0.j],
                      [ 0.9838+0.1791j,  0.9984-0.0567j,  0.0000+0.j,  0.9173+0.j],
                      [ 0.0000+0.j, -1.0000+0.j,  0.0000+0.j,  0.0000+0.j]])
        res[2][0.][-40][-20][1]['PFB'] = \
            np.array([[ 0.9984+0.0567j,  0.0000+0.j,  2.5606+0.j,  2.5606+0.j],
                      [ 0.0000+0.j,  0.9984-0.0567j,  0.0000+0.j,  2.5606+0.j],
                      [-0.1791+0.9838j, -0.1791-0.9838j,  0.0000+0.j,  0.0000+0.j]])
        res[2][0.][-40][-20][1]['FF'] = \
            np.array([[ 0.9984+0.0567j,  0.0000+0.j, -1.0000+0.j,  1.0000+0.j],
                      [ 1.0000+0.j,  0.9984-0.0567j,  0.0000+0.j,  0.0000+0.j],
                      [-0.9173+0.j, -0.2854+0.052j,  0.0000+0.j,  0.0000+0.j]])
        res[2][0.][-40][-20][1]['PFF'] = \
            np.array([[ 0.9984+0.0567j,  0.0000+0.j,  1.0000+0.j,  1.0000+0.j],
                      [ 0.0000+0.j,  0.9984-0.0567j,  0.0000+0.j,  1.0000+0.j],
                      [-0.4586+2.5191j, -0.4586-2.5191j,  0.0000+0.j,  0.0000+0.j]])
        res[2][0.][-60][-5][0]['FB'] = \
            np.array([[ 0.9984+0.0567j,  0.0000+0.j,  1.0000+0.j, -0.9936-0.1131j],
                      [ 1.0000+0.j,  0.9984-0.0567j,  0.0000+0.j, -1.9968+0.j],
                      [ 0.0000+0.j,  1.0000+0.j,  0.0000+0.j,  0.0000+0.j]])
        res[2][0.][-60][-5][0]['PFB'] = \
            np.array([[ 0.9984+0.0567j,  0.0000+0.j,  8.8260+0.j, -0.9984+8.7693j],
                      [ 0.0000+0.j,  0.9984-0.0567j,  0.0000+0.j, -0.9984-8.7693j],
                      [ 1.0000+0.j,  1.0000+0.j,  0.0000+0.j,  0.0000+0.j]])
        res[2][0.][-60][-5][0]['FF'] = \
            np.array([[ 0.9984+0.0567j,  0.0000+0.j, -1.0000+0.j,  1.0000+0.j],
                      [ 1.0000+0.j,  0.9984-0.0567j,  0.0000+0.j,  0.0000+0.j],
                      [-1.9968+0.j, -0.9936+0.1131j,  0.0000+0.j,  0.0000+0.j]])
        res[2][0.][-60][-5][0]['PFF'] = \
            np.array([[ 0.9984+0.0567j,  0.0000+0.j,  1.0000+0.j,  1.0000+0.j],
                      [ 0.0000+0.j,  0.9984-0.0567j,  0.0000+0.j,  1.0000+0.j],
                      [-0.9984+8.7693j, -0.9984-8.7693j,  0.0000+0.j,  0.0000+0.j]])
        res[2][0.][-60][-5][1]['FB'] = \
            np.array([[ 0.9984+0.0567j,  0.0000+0.j,  1.0000+0.j,  1.0000+0.j],
                      [ 0.9936+0.1131j,  0.9984-0.0567j,  0.0000+0.j,  1.9968+0.j],
                      [ 0.0000+0.j, -1.0000+0.j,  0.0000+0.j,  0.0000+0.j]])
        res[2][0.][-60][-5][1]['PFB'] = \
            np.array([[ 0.9984+0.0567j,  0.0000+0.j,  8.8260+0.j,  8.8260+0.j],
                      [ 0.0000+0.j,  0.9984-0.0567j,  0.0000+0.j,  8.8260+0.j],
                      [-0.1131+0.9936j, -0.1131-0.9936j,  0.0000+0.j,  0.0000+0.j]])
        res[2][0.][-60][-5][1]['FF'] = \
            np.array([[ 0.9984+0.0567j,  0.0000+0.j, -1.0000+0.j,  1.0000+0.j],
                      [ 1.0000+0.j,  0.9984-0.0567j,  0.0000+0.j,  0.0000+0.j],
                      [-1.9968+0.j, -0.9936+0.1131j,  0.0000+0.j,  0.0000+0.j]])
        res[2][0.][-60][-5][1]['PFF'] = \
            np.array([[ 0.9984+0.0567j,  0.0000+0.j,  1.0000+0.j,  1.0000+0.j],
                      [ 0.0000+0.j,  0.9984-0.0567j,  0.0000+0.j,  1.0000+0.j],
                      [-0.9984+8.7693j, -0.9984-8.7693j,  0.0000+0.j,  0.0000+0.j]])
        res[2][0.][-60][-10][0]['FB'] = \
            np.array([[ 0.9984+0.0567j,  0.0000+0.j,  1.0000+0.j, -0.9936-0.1131j],
                      [ 1.0000+0.j,  0.9984-0.0567j,  0.0000+0.j, -1.9968+0.j],
                      [ 0.0000+0.j,  1.0000+0.j,  0.0000+0.j,  0.0000+0.j]])
        res[2][0.][-60][-10][0]['PFB'] = \
            np.array([[ 0.9984+0.0567j,  0.0000+0.j,  8.8260+0.j, -0.9984+8.7693j],
                      [ 0.0000+0.j,  0.9984-0.0567j,  0.0000+0.j, -0.9984-8.7693j],
                      [ 1.0000+0.j,  1.0000+0.j,  0.0000+0.j,  0.0000+0.j]])
        res[2][0.][-60][-10][0]['FF'] = \
            np.array([[ 0.9984+0.0567j,  0.0000+0.j, -1.0000+0.j,  1.0000+0.j],
                      [ 1.0000+0.j,  0.9984-0.0567j,  0.0000+0.j,  0.0000+0.j],
                      [-1.9968+0.j, -0.9936+0.1131j,  0.0000+0.j,  0.0000+0.j]])
        res[2][0.][-60][-10][0]['PFF'] = \
            np.array([[ 0.9984+0.0567j,  0.0000+0.j,  1.0000+0.j,  1.0000+0.j],
                   [ 0.0000+0.j,  0.9984-0.0567j,  0.0000+0.j,  1.0000+0.j],
                   [-0.9984+8.7693j, -0.9984-8.7693j,  0.0000+0.j,  0.0000+0.j]])
        res[2][0.][-60][-10][1]['FB'] = \
            np.array([[ 0.9984+0.0567j,  0.0000+0.j,  1.0000+0.j,  1.0000+0.j],
                      [ 0.9936+0.1131j,  0.9984-0.0567j,  0.0000+0.j,  1.9968+0.j],
                      [ 0.0000+0.j, -1.0000+0.j,  0.0000+0.j,  0.0000+0.j]])
        res[2][0.][-60][-10][1]['PFB'] = \
            np.array([[ 0.9984+0.0567j,  0.0000+0.j,  8.8260+0.j,  8.8260+0.j],
                      [ 0.0000+0.j,  0.9984-0.0567j,  0.0000+0.j,  8.8260+0.j],
                      [-0.1131+0.9936j, -0.1131-0.9936j,  0.0000+0.j,  0.0000+0.j]])
        res[2][0.][-60][-10][1]['FF'] = \
            np.array([[ 0.9984+0.0567j,  0.0000+0.j, -1.0000+0.j,  1.0000+0.j],
                      [ 1.0000+0.j,  0.9984-0.0567j,  0.0000+0.j,  0.0000+0.j],
                      [-1.9968+0.j, -0.9936+0.1131j,  0.0000+0.j,  0.0000+0.j]])
        res[2][0.][-60][-10][1]['PFF'] = \
            np.array([[ 0.9984+0.0567j,  0.0000+0.j,  1.0000+0.j,  1.0000+0.j],
                      [ 0.0000+0.j,  0.9984-0.0567j,  0.0000+0.j,  1.0000+0.j],
                      [-0.9984+8.7693j, -0.9984-8.7693j,  0.0000+0.j,  0.0000+0.j]])
        res[2][0.25][-40][-10][0]['FB'] = \
            np.array([[-0.0567+0.9984j,  0.0000+0.j,  0.2901+0.j,  0.2854+0.052j],
                      [ 1.0000+0.j,  0.0567+0.9984j,  0.0000+0.j,  0.0000-0.9173j],
                      [ 0.0000+0.j,  1.0000+0.j,  0.0000+0.j,  0.0000+0.j]])
        res[2][0.25][-40][-10][0]['FF'] = \
            np.array([[-0.0567+0.9984j,  0.0000+0.j, -1.0000+0.j,  1.0000+0.j],
                   [ 1.0000+0.j,  0.0567+0.9984j,  0.0000+0.j,  0.0000+0.j],
                   [-0.0000-0.9173j,  0.2854-0.052j,  0.0000+0.j,  0.0000+0.j]])
        res[2][0.25][-40][-10][1]['FB'] = \
            np.array([[-0.0567+0.9984j,  0.0000+0.j,  0.2901+0.j,  0.2901+0.j],
                      [-0.1791+0.9838j,  0.0567+0.9984j,  0.0000+0.j,  0.9173+0.j],
                      [ 0.0000+0.j, -0.0000-1.j,  0.0000+0.j,  0.0000+0.j]])
        res[2][0.25][-40][-10][1]['FF'] = \
            np.array([[-0.0567+0.9984j,  0.0000+0.j, -1.0000+0.j, 1.0000+0.j],
                      [ 1.0000+0.j,  0.0567+0.9984j,  0.0000+0.j, 0.0000+0.j],
                      [-0.0000-0.9173j,  0.2854-0.052j,  0.0000+0.j,  0.0000+0.j]])
        res[3][0][-60][-5][0]['FB'] = \
            np.array([[ 0.9976+0.0694j, 0.0+0.j, 0.0+0.j, 0.0065+0.j, -0.0033-0.0056j],
                      [ 1.0000+0.j,  0.9976-0.0694j,  0.0000+0.j,  0.0000+0.j, -0.0808+0.j],
                      [ 0.0000+0.j,  1.0000+0.j,  1.0000+0.j,  0.0000+0.j, -0.4382+0.j],
                      [ 0.0000+0.j,  0.0000+0.j,  1.0000+0.j,  0.0000+0.j, 0.0+0.j]])
        res[3][0][-60][-5][0]['PFB'] = \
            np.array([[ 0.9976+0.0694j,  0.0000+0.j, 0.0000+0.j,  0.6745+0.j, 0.3608+0.5699j],
                      [ 0.0000+0.j, 0.9976-0.0694j, 0.0000+0.j,  0.0000+0.j, -0.0404-0.0237j],
                      [ 0.0000+0.j, 1.0000+0.j, 1.0000+0.j, 0.0000+0.j, -0.7990-0.5699j],
                      [ 1.0000+0.j, 0.0000+0.j, 1.0000+0.j, 0.0000+0.j, 0.0000+0.j]])
        res[3][0][-60][-5][0]['FF'] = \
            np.array([[ 0.9976+0.0694j, 0.0000+0.j, 0.0000+0.j, -1.0000+0.j, 1.0000+0.j],
                      [ 1.0000+0.j, 0.9976-0.0694j, 0.0000+0.j, 0.0000+0.j, 0.0000+0.j],
                      [ 0.0000+0.j, 1.0000+0.j, 1.0000+0.j,  0.0000+0.j, 0.0000+0.j],
                      [-0.4382+0.j, -0.0819+0.0304j, -0.0056+0.j, 0.0000+0.j, 0.0000+0.j]])

        self.res = res

    def test_realizeQNTF(self):
        """Test function for realizeQNTF()"""
        for i in self.orders:
            if not i in self.res: continue
            for j in self.f0s:
                if not j in self.res[i]: continue
                for ng in self.NG:
                    if not ng in self.res[i][j]: continue
                    for ing in self.ING:
                        if not ing in self.res[i][j][ng]: continue
                        for rot in self.rots:
                            if not rot in self.res[i][j][ng][ing]: continue
                            for f in self.forms:
                                if not f in self.res[i][j][ng][ing][rot]: continue
                                if self.res[i][j][ng][ing][rot][f] is None: continue
                                print("Testing form: %s, order: %d, f0: %f, NG %d ING %d ROT %d" % \
                                      (f, i, j, ng, ing, rot))
                                ntf = ds.synthesizeQNTF(i, self.osr, j, ng, ing)
                                ABCD = ds.realizeQNTF(ntf, f, rot)
                                if not np.allclose(self.res[i][j][ng][ing][rot][f].real,
                                                   ABCD.real, atol=1e-3, rtol=1e-3):
                                    print(ntf)
                                    print(ABCD)
                                    print(self.res[i][j][ng][ing][rot][f])
                                    print(ABCD - self.res[i][j][ng][ing][rot][f])
                                self.assertTrue(np.allclose(self.res[i][j][ng][ing][rot][f].real,
                                                ABCD.real, atol=1e-3, rtol=1e-3))
        return


