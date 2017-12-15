"""Tests for CPU profiler method: GetCmdMpstat"""
from tests.profilers.lepvTestCase import LepvTestCase

__author__    = "Copyright (c) 2017, LEP>"
__copyright__ = "Licensed under GPLv2 or later."

import unittest
from ddt import ddt, file_data

from modules.profilers.cpu.CPUProfiler import CPUProfiler

@ddt
class GetCmdMpstatTestCase(LepvTestCase):

    def setUp(self):
        self.profiler = CPUProfiler('')
        self.functor = self.profiler.get_irq

    @file_data("unittests.json")
    def test(self, kernel, os, cpu, note, lepdResult, expected, expectedMatchType):
        self.describe(kernel, os, cpu, note, expectedMatchType, expected)

        actual = self.functor(lepdResult)
        self.validate(expected, actual, expectedMatchType)


if __name__ == '__main__':
    unittest.main()
