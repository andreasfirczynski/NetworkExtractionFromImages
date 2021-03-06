import unittest
import sys, os
from _alg import *
from pipeline import Pipeline
from _category import Category
from ext_loader import ExtensionLoader
import demjson
import collections

__author__ = {'Dennis Groß': 'gdennis91@googlemail.com'}


class ParserTests(unittest.TestCase):

    def test_report_pip_simple(self):
        alg = AlgSimple()

        should_list = [["type", "preprocessing"], ["store_image", False], ["int_slider1", 5],
                      ["float_slider1", 5.0]]
        should_be = ("simple alg", collections.OrderedDict(should_list))

        was = alg.report_pip()

        self.assertEqual(demjson.encode(was), demjson.encode(should_be))

    def test_report_pip_hard(self):
        alg = AlgHard()

        list = [["type", "preprocessing"], ["store_image", False], ["int_slider1", 5],
                ["int_slider2", 5], ["int_slider3", 5], ["int_slider4", 5],
                ["float_slider1", 5.0], ["float_slider2", 5.0],
                ["checkbox1", True], ["drop_down1", "drop_down1"],
                ["drop_down2", "drop_down2"]]

        should_dic = collections.OrderedDict(list)

        w_name, w_dic = alg.report_pip()

        was = demjson.encode({w_name: w_dic})
        should_be = demjson.encode({"hard alg": should_dic})

        self.assertEqual(was, should_be)

    def test_save_pipeline_easy(self):

        extloader = ExtensionLoader()
        pipeline = Pipeline(extloader.cats_container)

        pipeline.new_category(0)
        pipeline.new_category(1)
        pipeline.new_category(2)
        pipeline.new_category(3)

        pipeline.change_category("Segmentation", 0)
        pipeline.change_category("Segmentation", 1)
        pipeline.change_category("Segmentation", 2)
        pipeline.change_category("Segmentation", 3)

        pipeline.change_algorithm("Adaptive Threshold", 0)
        pipeline.change_algorithm("Adaptive Threshold", 1)
        pipeline.change_algorithm("Adaptive Threshold", 2)
        pipeline.change_algorithm("Adaptive Threshold", 3)

        pipeline.save_pipeline_json("test", os.path.abspath("../test_assets/"))

    def test_save_pipeline_order(self):

        extloader = ExtensionLoader()
        pipeline = Pipeline(extloader.cats_container)

        pipeline.new_category(0)
        pipeline.new_category(1)
        pipeline.new_category(2)
        pipeline.new_category(3)

        pipeline.change_category("Preprocessing", 0)
        pipeline.change_category("Segmentation", 1)
        pipeline.change_category("Graph detection", 2)
        pipeline.change_category("Graph filtering", 3)

        pipeline.change_algorithm("Bilateral Filter", 0)
        pipeline.change_algorithm("Adaptive Threshold", 1)
        pipeline.change_algorithm("Guo Hall Thinning", 2)
        pipeline.change_algorithm("Keep only largest connected component", 3)

        pipeline.save_pipeline_json("test_order", os.path.abspath("../test_assets/"))

    def test_load_json_easy(self):
        extloader = ExtensionLoader()
        pipeline = Pipeline(extloader.cats_container)

        pipeline.load_pipeline_json(os.path.abspath('../test_assets/test.json'))

    def test_load_json_hard(self):
        extloader = ExtensionLoader()
        pipeline = Pipeline(extloader.cats_container)

        pipeline.load_pipeline_json(os.path.abspath('../test_assets/test_order.json'))

    def test_load_json_non_default(self):
        extloader = ExtensionLoader()
        pipeline = Pipeline(extloader.cats_container)

        pipeline.load_pipeline_json(os.path.abspath('../test_assets/test_order_non_default.json'))
        print('test')

class AlgHard(Algorithm):

    def process(self, input_data):
        print("i was called")

    def __init__(self):
        super(AlgHard, self).__init__()

        self.name = "hard alg"
        self.parent = "preprocessing"

        self.int_slider1 = IntegerSlider("int_slider1", 0, 10, 1, 5)
        self.integer_sliders.append(self.int_slider1)

        self.int_slider2 = IntegerSlider("int_slider2", 0, 10, 1, 5)
        self.integer_sliders.append(self.int_slider2)

        self.int_slider3 = IntegerSlider("int_slider3", 0, 10, 1, 5)
        self.integer_sliders.append(self.int_slider3)

        self.int_slider4 = IntegerSlider("int_slider4", 0, 10, 1, 5)
        self.integer_sliders.append(self.int_slider4)

        self.float_slider1 = FloatSlider("float_slider1", 0.0, 10.0, 1.0, 5.0)
        self.float_sliders.append(self.float_slider1)

        self.float_slider2 = FloatSlider("float_slider2", 0.0, 10.0, 1.0, 5.0)
        self.float_sliders.append(self.float_slider2)

        self.drop_down1 = DropDown("drop_down1", {"eins", "zwei", "drei"})
        self.drop_downs.append(self.drop_down1)

        self.drop_down2 = DropDown("drop_down2", {"eins", "zwei", "drei"})
        self.drop_downs.append(self.drop_down2)

        self.checkbox1 = CheckBox("checkbox1", True)
        self.checkboxes.append(self.checkbox1)


class AlgSimple(Algorithm):

    def __init__(self):
        super(AlgSimple, self).__init__()

        self.name = "simple alg"
        self.parent = "preprocessing"
        self.int_slider1 = IntegerSlider("int_slider1", 0, 10, 1, 5)
        self.integer_sliders.append(self.int_slider1)
        self.float_slider1 = FloatSlider("float_slider1", 0.0, 10.0, 1.0, 5.0)
        self.float_sliders.append(self.float_slider1)

    def process(self, input_data):
        print("i was sucessfully processed")