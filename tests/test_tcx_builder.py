import unittest
from lib.tcx_builder import TCXBuilder

class TCXBuilderTests(unittest.TestCase):
    def test_empty_out_should_raise_error(self):
        tcx_obj = TCXBuilder()
        with self.assertRaises(MalformedTCXException):
            tcx_obj.out()

    def test_new_creates_elements(self):
        tcx_obj = TCXBuilder()
        tcx_obj.new()
        self.assertEquals(tcx_obj.out(), "")

    def test_new_creates_running_sport(self):
        tcx_obj = TCXBuilder()
        tcx_obj.new("Running")
        self.assertEquals(tcx_obj.out(), "")

    def test_new_covers_unknown_sport(self):
        tcx_obj = TCXBuilder()
        tcx_obj.new("Unknown")
        self.assertEquals(tcx_obj.out(), "")

    def test_set_new_id(self):
        tcx_obj = TCXBuilder()
        tcx_obj.new()
        tcx_obj.setId("NewID")
        self.assertEquals(tcx_obj.out(), "NewID")


