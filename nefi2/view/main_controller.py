# -*- coding: utf-8 -*-
"""
This is nefi's main view. Currently we deployed all controls of the
GUI in the MainView.ui. Static changes to the GUI should always been
done by the Qt designer since this reduces the amount of code dramatically.
To draw the complete UI the controllers are invoked and the draw_ui function is
called
"""
from PyQt5 import QtCore, QtGui, QtWidgets, uic
import sys, os, sys
import qdarkstyle
from PyQt5.QtGui import QIcon, QPixmap
# cus widgets
import PyQt5.QtWidgets
from PyQt5.QtCore import Qt, pyqtSignal, pyqtSlot, QObject, QEvent
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QBoxLayout, QGroupBox, QSpinBox, QDoubleSpinBox, QSlider, QLabel, QWidget, QHBoxLayout, QVBoxLayout, \
    QStackedWidget, QComboBox, QSizePolicy, QToolButton

__authors__ = {"Dennis Groß": "gdennis91@googlemail.com",
               "Philipp Reichert": "prei@me.com"}

base, form = uic.loadUiType("./view/MainView.ui")


class MainView(base, form):
    def __init__(self, pipeline, parent=None):

        super(base, self).__init__(parent)
        self.setupUi(self)
        self.pipeline = pipeline
        self.pip_widgets = []
        self.default_pips = []

        self.draw_ui()
        self.connect_ui()

    def register_observers(self):
        pass

    def connect_ui(self):
        """
        This function connects the ui using signals from the
        ui elements and its method counterparts.
        """
        self.input_btn.clicked.connect(self.set_input_url)
        self.output_btn.clicked.connect(self.set_output_url)
        self.save_btn.clicked.connect(self.save_pipeline)
        self.load_favorite_pipelines()
        self.fav_pips_combo_box.activated.connect(self.select_default_pip)
        self.run_btn.clicked.connect(self.run)
        self.delete_btn.clicked.connect(self.trash_pipeline)
        self.add_btn.clicked.connect(lambda: self.add_pipe_entry_new())

    def draw_ui(self):
        """
        This function draws all additional UI elements. If you want the
        application to display any additional things like a button you can
        either add it in the QtDesigner or declare it here.
        """

        # *TODO* Create these ones with Qt Designer and put them into select_cat_alg_vbox_layout. I failed
        self.ComboxCategories = QComboBox()
        self.stackedWidgetComboxesAlgorithms = QStackedWidget()
        self.select_cat_alg_vbox_layout.addWidget(self.ComboxCategories)
        self.select_cat_alg_vbox_layout.addWidget(self.stackedWidgetComboxesAlgorithms)
        self.ComboxCategories.hide()


        """
        This function is concerned with drawing all non static elements  into the
        GUI.
        """
        """self.set_pip_title("A. Junius2")

        self.set_preset(["A.Junius", "test", "test", "test"])


        self.add_pip_entry("../assets/images/P.png", "Preprocessing - adaptive trehsold watershed")
        self.add_pip_entry("../assets/images/P.png", "Preprocessing - adaptive trehsold watershed")
        self.add_pip_entry("../assets/images/P.png", "Preprocessing - adaptive trehsold watershed")
        self.add_pip_entry("../assets/images/P.png", "Preprocessing - adaptive trehsold watershed")
        self.add_pip_entry("../assets/images/P.png", "Preprocessing - adaptive trehsold watershed")
        self.add_pip_entry("../assets/images/P.png", "Preprocessing - adaptive trehsold watershed")
        self.add_pip_entry("../assets/images/P.png", "Preprocessing - adaptive trehsold watershed")
        self.add_cat_image("../assets/images/seg_fav.jpeg", "Preprocessing")
        self.add_cat_image("../assets/images/wing.jpeg", "Preprocessing")
        self.add_cat_image("../assets/images/wing.jpeg", "Preprocessing")
        self.add_cat_image("../assets/images/wing.jpeg", "Preprocessing")
        self.add_cat_image("../assets/images/wing.jpeg", "Preprocessing")
        self.add_cat_image("../assets/images/wing.jpeg", "Preprocessing")
        self.add_cat_image("../assets/images/wing.jpeg", "Preprocessing")

        self.main_image_label.setPixmap(QtGui.QPixmap("wing.jpeg"))

        category_combo_box = ComboBoxWidget("type")
        category_combo_box.add_item("Preprocessing", "../assets/images/P.png")
        category_combo_box.add_item("Segmentation", "../assets/images/S.png")
        category_combo_box.add_item("Graph Detection", "../assets/images/D.png")
        category_combo_box.add_item("Graph Filtering", "../assets/images/F.png")

        alg_combo_box = ComboBoxWidget("algorithm")
        alg_combo_box.add_item("Otsus")
        alg_combo_box.add_item("Guo Hall")
        alg_combo_box.add_item("Adaptive Treshold")

        slider_1 = SliderWidget("slider1das", 0, 10, 1, 4, True)
        slider_2 = SliderWidget("slider1", 0, 10, 2, 4, False)
        slider_3 = SliderWidget("sliderböadsad", 0, 10, 1, 4, True)
        slider_4 = SliderWidget("sliderböadsad", 0, 10, 1, 4, True)
        slider_5 = SliderWidget("sliderböadsad", 0, 10, 1, 4, True)
        checkbox_1 = CheckBoxWidget("checkbox1", True)

        self.setting_widget_vbox_layout.addWidget(category_combo_box)
        self.setting_widget_vbox_layout.addWidget(alg_combo_box)
        self.setting_widget_vbox_layout.addWidget(slider_1)
        self.setting_widget_vbox_layout.addWidget(slider_2)
        self.setting_widget_vbox_layout.addWidget(slider_3)
        self.setting_widget_vbox_layout.addWidget(slider_4)
        self.setting_widget_vbox_layout.addWidget(slider_5)
        self.setting_widget_vbox_layout.addWidget(checkbox_1)
        self.setting_widget_vbox_layout.setAlignment(Qt.AlignTop)"""

    def set_pip_title(self, title):
        """
        Sets the title of the current selected pipeline in the ui.

        Args:
            | *title*: the title of the pipeline
            | *label_ref*: the reference to the label.
        """
        self.current_pip_label.setText(title)

    def load_dark_theme(self, application):
        """
        This function is called to load the white theme with
        all its icons for the buttons and the css file.
        Args:
            application: the cureent app instance
        """
        # load buttons
        pixmap_icon = QtGui.QPixmap("./assets/images/add_white.png")
        q_icon = QtGui.QIcon(pixmap_icon)
        self.add_btn.setIcon(q_icon)

        pixmap_icon = QtGui.QPixmap("./assets/images/trash_white.png")
        q_icon = QtGui.QIcon(pixmap_icon)
        self.delete_btn.setIcon(q_icon)

        pixmap_icon = QtGui.QPixmap("./assets/images/diskette_white.png")
        q_icon = QtGui.QIcon(pixmap_icon)
        self.save_btn.setIcon(q_icon)

        pixmap_icon = QtGui.QPixmap("./assets/images/up-arrow_white.png")
        q_icon = QtGui.QIcon(pixmap_icon)
        self.input_btn.setIcon(q_icon)

        pixmap_icon = QtGui.QPixmap("./assets/images/folder_white.png")
        q_icon = QtGui.QIcon(pixmap_icon)
        self.output_btn.setIcon(q_icon)

    @pyqtSlot(int)
    def select_default_pip(self, index):
        """
        This is the slot for the Pipeline combobox in the ui
        Args:
            index: index of the option currently selected
        """

        # delete current pipeline

        self.trash_pipeline()

        # get url and name
        name, url = self.default_pips[index - 1]

        # parse the json in the model
        self.pipeline.load_pipeline_json(url)

        print("PARSER" + str(self.pipeline.executed_cats[0].active_algorithm))
        print("PARSER" + str(self.pipeline.executed_cats[1].active_algorithm))

        # set the title
        self.set_pip_title(name)

        # Create an entry in the pipeline widget for every step in the pipeline
        for i in range(0, len(self.pipeline.executed_cats)):
            self.add_pipe_entry_new(i)
            self.scroll_down_pip()

            """for widget in alg_widgets:
                self.setting_widget_vbox_layout.addWidget(widget)"""

    def trash_pipeline(self):
        """
        This method clears the complete pipeline while users clicked the trash
        button.
        """
        # remove all entries in the pipeline list

        while self.pip_widget_vbox_layout.count():
            child = self.pip_widget_vbox_layout.takeAt(0)
            child.widget().deleteLater()

        while self.stackedWidget_Settings.currentWidget() is not None:
            self.stackedWidget_Settings.removeWidget(self.stackedWidget_Settings.currentWidget())
            self.settings_collapsable.setTitle("")

        # remove the pipeline name
        self.set_pip_title("")

        # remove all entries int the executed_cats of the model pipeline
        del self.pipeline.executed_cats[:]

        # remove all widgets
        del self.pip_widgets[:]

        # remove category algorith dropdown
        self.remove_cat_alg_dropdown()

        # remove all entries from the pipeline model

        del self.pipeline.executed_cats[:]

    @pyqtSlot()
    def run(self):
        """
        This method runs the the pipeline by calling the process methode
        in pipeline
        """

        self.pipeline.process()

    @pyqtSlot()
    def set_input_url(self):
        """
        This method sets the url for the input image in the pipeline.
        """
        url = QtWidgets.QFileDialog.getOpenFileNames()
        if url[0]:
            print(url[0])
            print(url[0][0])
            self.lineEdit.setText(url[0][0])
            self.pipeline.set_input(url[0][0])


    @pyqtSlot()
    def set_output_url(self):
        """
        This method sets the url for the output folder in the pipeline.
        Args:
            url: the url to the output folder a user selected in the ui
        """
        url = QtWidgets.QFileDialog.getExistingDirectory()
        if url:
            print(url)
            print(url)
            self.custom_line_edit.setText(url)
            self.pipeline.set_output_dir(url)

    def load_favorite_pipelines(self):
        """
        Scans the directory for default pipelines to display all available items
        """
        self.fav_pips_combo_box.addItem("Please Select")

        # scan the directory for default pipelines
        for file in os.listdir("./_default_pipelines"):
            if file.endswith(".json"):
                name = file.split(".")[0]
                url = os.path.abspath("./_default_pipelines" + "/" + file)
                self.default_pips.append([name, url])
                self.fav_pips_combo_box.addItem(name)

    @pyqtSlot()
    def save_pipeline(self):
        """
        Saves the pipeline as a json at the users file system.
        """
        url = str(QtWidgets.QFileDialog.getSaveFileName()[0])

        split_list = url.split("/")
        name = split_list[len(split_list) - 1].split(".")[0]
        del split_list[len(split_list) - 1]
        url = url.replace(name, "")
        self.pipeline.save_pipeline_json(name, url)

    @pyqtSlot(int)
    def remove_pip_entry(self, pipe_entry_widget, settings_widget, cat=None):
        """
        Removes the pip entry at the given position in the ui
        Args:
            pipeline_index (object):
            settings_widget:
            position: position at which the pip entry gets removed
        """

        # remove pipeline entry widget from ui
        self.pip_widget_vbox_layout.removeWidget(pipe_entry_widget)
        pipe_entry_widget.deleteLater()

        # remove it settings widgets from ui
        if settings_widget is not None:
            if self.stackedWidget_Settings.currentWidget() == settings_widget:
                self.stackedWidget_Settings.hide()
                self.remove_cat_alg_dropdown()
                self.settings_collapsable.setTitle("Settings")

            self.stackedWidget_Settings.removeWidget(settings_widget)

        # remove in model
        if cat is not None:
            print("Remove entry at pos " + str(self.pipeline.get_index(cat)) + " " + str(cat))
            self.pipeline.delete_category(self.pipeline.get_index(cat))

    def change_pip_entry_alg(self, position, new_category, new_algorithm, pipe_entry_widget, settings_widget):
        """
        Changes the selected algorithm of the pipeline entry at the position.
        Afterwards create all widgets for this algorithm instance
        Args:
            position: the position of the pipeline entry
            algorithm: the selected algorithm for this category
        """
        print("Position to be changed:" + str(position))
        print("Pipeline length: " + str(len(self.pipeline.executed_cats)))

        old_cat = self.pipeline.executed_cats[position]
        old_alg = old_cat.active_algorithm
        print("Old Cat found in pipeline: " + str(old_cat))
        print("Old Alg: found in pipeline:" + str(old_alg))

        print("New Category given:" + str(new_category))
        print("New Algorithm given:" + str(new_algorithm))

        # set in model
        self.pipeline.change_category(new_category, position)
        self.pipeline.change_algorithm(new_algorithm, position)

        new_cat = self.pipeline.executed_cats[position]
        new_alg = new_cat.active_algorithm

        # change settings widgets
        self.remove_pip_entry(pipe_entry_widget, settings_widget)
        (new_pipe_entry_widget, new_settings_widget) = self.add_pipe_entry_new(position)

        self.stackedWidget_Settings.show()
        self.stackedWidget_Settings.setCurrentIndex(position)
        self.settings_collapsable.setTitle(new_alg.get_name() + " Settings")

        self.remove_cat_alg_dropdown()
        self.create_cat_alg_dropdown(position, new_pipe_entry_widget, new_settings_widget)
        self.set_cat_alg_dropdown(new_cat, new_alg)


        print("New Cat found in pipeline: " + str(new_cat))
        print("New Alg found in pipeline: " + str(new_alg))


    def load_settings_widgets_from_pipeline_groupbox(self, position):
        """
        Extracts all widgets from a single algorithm and returns a QBoxLayout
        Args:
            alg: the alg instance we extract from

        Returns: a QBoxLayout containing all widgets for this particular alg.

        """

        alg = self.pipeline.executed_cats[position].active_algorithm

        print("alg " + str(alg))
        print("cat " + str(self.pipeline.executed_cats[position]))

        empty_flag = True

        groupOfSliders = QGroupBox()
        sp = QSizePolicy()
        sp.setVerticalPolicy(QSizePolicy.Preferred)
        # groupOfSliders.setSizePolicy(sp)
        groupOfSliderssLayout = QBoxLayout(QBoxLayout.TopToBottom)
        groupOfSliderssLayout.setContentsMargins(0, -0, -0, 0)
        groupOfSliderssLayout.setAlignment(Qt.AlignTop)
        groupOfSliderssLayout.setSpacing(0)

        print("Build Slider @ "+ str(position))

        # create integer sliders
        for slider in alg.integer_sliders:
            empty_flag = False
            print("slider.value " + str(slider.value))
            print("slider " + str(slider))
            #print(alg.get_name() + ": add slider (int).")
            groupOfSliderssLayout.addWidget(
                SliderWidget(slider.name, slider.lower, slider.upper, slider.step_size, slider.value,
                             slider.set_value, False))

        # create float sliders
        for slider in alg.float_sliders:
            empty_flag = False
            #print(alg.get_name() + ": add slider (float).")
            groupOfSliderssLayout.addWidget(
                SliderWidget(slider.name, slider.lower, slider.upper, slider.step_size, slider.value,
                             slider.set_value, True), 0, Qt.AlignTop)

        # create checkboxes
        for checkbox in alg.checkboxes:
            empty_flag = False
            #print(alg.get_name() + ": add checkbox.")
            groupOfSliderssLayout.addWidget(CheckBoxWidget(checkbox.name, checkbox.value, checkbox.set_value), 0,
                                            Qt.AlignTop)

        # create dropdowns
        for combobox in alg.drop_downs:
            empty_flag = False
            #print(alg.get_name() + ": add combobox.")
            groupOfSliderssLayout.addWidget(
                ComboBoxWidget(combobox.name, combobox.options, combobox.set_value, combobox.value), 0, Qt.AlignTop)

        if empty_flag:
            label = QLabel()
            label.setText("This algorithm has no Settings.")
            groupOfSliderssLayout.addWidget(label, 0, Qt.AlignHCenter)

        groupOfSliders.setLayout(groupOfSliderssLayout)

        return groupOfSliders

    def create_cat_alg_dropdown(self, cat_position, pipe_entry_widget, settings_widget):

        """
        Args:
            last_cat (object):
        """
        layout = self.select_cat_alg_vbox_layout
        cat = self.pipeline.executed_cats[cat_position]

        last_cat = None

        # Show only allowed categories in dropdown
        if len(self.pipeline.executed_cats) > 1:
            last_cat = self.pipeline.executed_cats[cat_position - 1]

        # Combobox for selecting Category
        self.ComboxCategories.show()
        self.ComboxCategories.setFixedHeight(30)
        self.ComboxCategories.addItem("<Please Select Category>")

        self.stackedWidgetComboxesAlgorithms = QStackedWidget()
        self.stackedWidgetComboxesAlgorithms.setFixedHeight(30)
        self.stackedWidgetComboxesAlgorithms.hide()

        def setCurrentIndexCat(index):
            #print("Set Cat")
            if self.ComboxCategories.currentIndex() == 0:
                self.stackedWidgetComboxesAlgorithms.hide()
            else:
                self.stackedWidgetComboxesAlgorithms.show()
                self.stackedWidgetComboxesAlgorithms.setCurrentIndex(index - 1)

        for category_name in self.pipeline.report_available_cats(last_cat):

            # Add Category to combobox
            self.ComboxCategories.addItem(category_name)
            tmp1 = QComboBox()
            tmp1.addItem("<Please Select Algorithm>")
            tmp1.setFixedHeight(30)
            category = self.pipeline.get_category(category_name)
            #self.current_index = -1

            def setCurrentIndexAlg(index):
                if self.ComboxCategories.currentIndex() == 0 or self.stackedWidgetComboxesAlgorithms.currentWidget().currentIndex() == 0:
                    pass
                else: #self.current_index != index:
                    self.change_pip_entry_alg(self.pipeline.get_index(cat), self.ComboxCategories.currentText(),
                                              self.stackedWidgetComboxesAlgorithms.currentWidget().currentText(),
                                              pipe_entry_widget, settings_widget)
                    #self.current_index = index

            tmp1.activated.connect(setCurrentIndexAlg)

            for algorithm_name in self.pipeline.get_all_algorithm_list(category):
                tmp1.addItem(algorithm_name)

            self.stackedWidgetComboxesAlgorithms.addWidget(tmp1)

        layout.addWidget(self.ComboxCategories)
        layout.addWidget(self.stackedWidgetComboxesAlgorithms)

        self.ComboxCategories.activated.connect(setCurrentIndexCat)

    def set_cat_alg_dropdown(self, category, algorithm):

        indexC = self.ComboxCategories.findText(category.get_name())
        #print("IndexC " + str(indexC))
        self.ComboxCategories.setCurrentIndex(indexC)
        self.stackedWidgetComboxesAlgorithms.show()
        self.stackedWidgetComboxesAlgorithms.setCurrentIndex(indexC - 1)
        indexA = self.stackedWidgetComboxesAlgorithms.currentWidget().findText(algorithm.get_name())
        #print("IndexA " + str(indexA))
        self.stackedWidgetComboxesAlgorithms.currentWidget().setCurrentIndex(indexA)

    def remove_cat_alg_dropdown(self):

        """

        Returns:
            object:
        """
        self.ComboxCategories.clear()

        while self.stackedWidgetComboxesAlgorithms.currentWidget() is not None:
            self.stackedWidgetComboxesAlgorithms.removeWidget(self.stackedWidgetComboxesAlgorithms.currentWidget())

        while self.select_cat_alg_vbox_layout.count():
            child = self.select_cat_alg_vbox_layout.takeAt(0)
            child.widget().hide()

    def scroll_down_pip(self):
        self.pip_scroll.verticalScrollBar().setSliderPosition(self.pip_scroll.verticalScrollBar().maximum())

    def add_pipe_entry_new(self, position=None):
        """
            Creates a entry in the ui pipeline with a given position in pipeline.
            It also creates the corresponding settings widget.
            """
        # create an widget that displays the pip entry in the ui and connect the remove button

        pip_main_widget = QWidget()
        pip_main_widget.setFixedHeight(70)
        pip_main_widget.setFixedWidth(300)
        pip_main_layout = QHBoxLayout()
        pip_main_widget.setLayout(pip_main_layout)

        new_marker = False

        if position is None:
            position = len(self.pipeline.executed_cats)
            cat = self.pipeline.new_category(position)
            label = "<Click to specify new step>"
            icon = None
            new_marker = True
        else:
            cat = self.pipeline.executed_cats[position]
            alg = cat.active_algorithm
            label = alg.get_name()
            icon = cat.get_icon()
            new_marker = False

        pixmap = QPixmap(icon)
        pixmap_scaled_keeping_aspec = pixmap.scaled(30, 30, QtCore.Qt.KeepAspectRatio)
        pixmap_label = QtWidgets.QLabel()
        pixmap_label.setPixmap(pixmap_scaled_keeping_aspec)

        pip_up_down = QWidget()
        pip_up_down.setFixedHeight(70)
        pip_up_down_layout = QVBoxLayout()
        pip_up_down.setLayout(pip_up_down_layout)

        up_btn = QToolButton()
        dw_btn = QToolButton()

        up_btn.setArrowType(Qt.UpArrow)
        up_btn.setFixedHeight(25)
        dw_btn.setArrowType(Qt.DownArrow)
        dw_btn.setFixedHeight(25)

        pip_up_down_layout.addWidget(up_btn)
        pip_up_down_layout.addWidget(dw_btn)

        string_label = QLabel()
        string_label.setText(label)
        string_label.setFixedWidth(210)

        btn = QtWidgets.QPushButton()
        btn.setFixedSize(20, 20)

        pixmap_icon = QtGui.QPixmap("./assets/images/delete_x_white.png")
        q_icon = QtGui.QIcon(pixmap_icon)
        btn.setIcon(q_icon)

        pip_main_layout.addWidget(pip_up_down, Qt.AlignVCenter)
        pip_main_layout.addWidget(pixmap_label, Qt.AlignVCenter)
        pip_main_layout.addWidget(string_label, Qt.AlignLeft)
        pip_main_layout.addWidget(btn, Qt.AlignVCenter)

        self.pip_widget_vbox_layout.insertWidget(position, pip_main_widget)

        # Create the corresponding settings widget and connect it
        self.settings_collapsable.setTitle("Settings")
        self.stackedWidget_Settings.hide()
        settings_main_widget = None
        if not new_marker:
            settings_main_widget = self.load_settings_widgets_from_pipeline_groupbox(position)
            self.stackedWidget_Settings.insertWidget(position, settings_main_widget)

        def show_settings():
            # Set background color while widget is selected. Doesn't work because of theme? *TODO*
            p = pip_main_widget.palette()
            p.setColor(pip_main_widget.backgroundRole(), Qt.red)
            pip_main_widget.setPalette(p)

            if not new_marker:
                self.stackedWidget_Settings.show()
                self.stackedWidget_Settings.setCurrentIndex(self.pipeline.get_index(cat))
                self.settings_collapsable.setTitle(alg.get_name() + " Settings")
            else:
                self.stackedWidget_Settings.hide()

            # Create drop down for cats and algs
            self.remove_cat_alg_dropdown()
            self.create_cat_alg_dropdown(self.pipeline.get_index(cat), pip_main_widget, settings_main_widget)

            if not new_marker:
                self.set_cat_alg_dropdown(cat, alg)

        # Connect Button to remove step from pipeline
        def delete_button_clicked():
            self.remove_cat_alg_dropdown()
            self.remove_pip_entry(pip_main_widget, settings_main_widget, cat)

        self.clickable(pixmap_label).connect(show_settings)
        self.clickable(string_label).connect(show_settings)
        btn.clicked.connect(delete_button_clicked)


        return (pip_main_widget, settings_main_widget)



    def add_pip_entry_empty(self):
        """
        Creates an blank entry in the ui pipeline since the user still needs to specify
        a type and an algorithm of the category.
        It also creates the corresponding settings widget.
        """
        # create an widget that displays the pip entry in the ui and connect the remove button
        pip_main_widget = QWidget()
        pip_main_widget.setFixedHeight(70)
        pip_main_widget.setFixedWidth(300)
        pip_main_layout = QHBoxLayout()
        pip_main_widget.setLayout(pip_main_layout)

        label = "<Click to specify new step>"
        icon = None

        pixmap = QPixmap(icon)
        pixmap_scaled_keeping_aspec = pixmap.scaled(30, 30, QtCore.Qt.KeepAspectRatio)
        pixmap_label = QtWidgets.QLabel()
        pixmap_label.setPixmap(pixmap_scaled_keeping_aspec)

        pip_up_down = QWidget()
        pip_up_down.setFixedHeight(70)
        pip_up_down_layout = QVBoxLayout()
        pip_up_down.setLayout(pip_up_down_layout)

        up_btn = QToolButton()
        dw_btn = QToolButton()

        up_btn.setArrowType(Qt.UpArrow)
        up_btn.setFixedHeight(25)
        dw_btn.setArrowType(Qt.DownArrow)
        dw_btn.setFixedHeight(25)

        pip_up_down_layout.addWidget(up_btn)
        pip_up_down_layout.addWidget(dw_btn)

        string_label = QLabel()
        string_label.setText(label)
        string_label.setFixedWidth(210)

        btn = QtWidgets.QPushButton()
        btn.setFixedSize(20, 20)

        pixmap_icon = QtGui.QPixmap("./assets/images/delete_x_white.png")
        q_icon = QtGui.QIcon(pixmap_icon)
        btn.setIcon(q_icon)

        pip_main_layout.addWidget(pip_up_down, Qt.AlignVCenter)
        pip_main_layout.addWidget(pixmap_label, Qt.AlignVCenter)
        pip_main_layout.addWidget(string_label, Qt.AlignLeft)
        pip_main_layout.addWidget(btn, Qt.AlignVCenter)

        cat_position = len(self.pipeline.executed_cats)

        self.pip_widget_vbox_layout.insertWidget(cat_position, pip_main_widget)
        index = self.pip_widget_vbox_layout.indexOf(pip_main_widget)
        #print(index)

        # Create the corresponding empty settings widget and connect it
        # settings = self.load_widgets_from_cat_groupbox(cat_position) *TODO* EMPTY

        self.settings_collapsable.setTitle("Settings")
        self.stackedWidget_Settings.hide()

        # Add new step to pipeline
        new_category = self.pipeline.new_category(cat_position)

        print("Create new entry " + str(new_category))
        print("Pipeline length: " + str(len(self.pipeline.executed_cats)) + ".")

        settings_main_widget = None

        # Connect pipeline entry with corresponding settings widget
        def show_settings():
            #print("click")
            self.stackedWidget_Settings.show()

            self.remove_cat_alg_dropdown()

            # Create drop down for cats and algs
            self.create_cat_alg_dropdown(self.pipeline.get_index(new_category), pip_main_widget, settings_main_widget)
            self.stackedWidget_Settings.hide()

        # Connect Button to remove step from pipeline
        def delete_button_clicked():
            self.remove_cat_alg_dropdown()
            self.remove_pip_entry(pip_main_widget, settings_main_widget, new_category)

        self.clickable(pixmap_label).connect(show_settings)
        self.clickable(string_label).connect(show_settings)
        btn.clicked.connect(delete_button_clicked)

        self.scroll_down_pip()

    def add_pip_entry(self, cat_position):
        """
        Creates a entry in the ui pipeline with a given position in pipeline.
        It also creates the corresponding settings widget.
        """
        # create an widget that displays the pip entry in the ui and connect the remove button

        pip_main_widget = QWidget()
        pip_main_widget.setFixedHeight(70)
        pip_main_widget.setFixedWidth(300)
        pip_main_layout = QHBoxLayout()
        pip_main_widget.setLayout(pip_main_layout)

        cat = self.pipeline.executed_cats[cat_position]
        alg = cat.active_algorithm
        label = alg.get_name()
        icon = cat.get_icon()

        pixmap = QPixmap(icon)
        pixmap_scaled_keeping_aspec = pixmap.scaled(30, 30, QtCore.Qt.KeepAspectRatio)
        pixmap_label = QtWidgets.QLabel()
        pixmap_label.setPixmap(pixmap_scaled_keeping_aspec)

        pip_up_down = QWidget()
        pip_up_down.setFixedHeight(70)
        pip_up_down_layout = QVBoxLayout()
        pip_up_down.setLayout(pip_up_down_layout)

        up_btn = QToolButton()
        dw_btn = QToolButton()

        up_btn.setArrowType(Qt.UpArrow)
        up_btn.setFixedHeight(25)
        dw_btn.setArrowType(Qt.DownArrow)
        dw_btn.setFixedHeight(25)

        pip_up_down_layout.addWidget(up_btn)
        pip_up_down_layout.addWidget(dw_btn)

        string_label = QLabel()
        string_label.setText(label)
        string_label.setFixedWidth(210)

        btn = QtWidgets.QPushButton()
        btn.setFixedSize(20, 20)

        pixmap_icon = QtGui.QPixmap("./assets/images/delete_x_white.png")
        q_icon = QtGui.QIcon(pixmap_icon)
        btn.setIcon(q_icon)

        pip_main_layout.addWidget(pip_up_down, Qt.AlignVCenter)
        pip_main_layout.addWidget(pixmap_label, Qt.AlignVCenter)
        pip_main_layout.addWidget(string_label, Qt.AlignLeft)
        pip_main_layout.addWidget(btn, Qt.AlignVCenter)

        self.pip_widget_vbox_layout.insertWidget(cat_position, pip_main_widget)
        index = self.pip_widget_vbox_layout.indexOf(pip_main_widget)
        #print(index)

        # Create the corresponding settings widget and connect it
        settings_main_widget = self.load_settings_widgets_from_pipeline_groupbox(cat_position)

        self.settings_collapsable.setTitle("Settings")
        self.stackedWidget_Settings.hide()
        self.stackedWidget_Settings.insertWidget(cat_position, settings_main_widget)

        #print("Read from pipeline entry " + str(cat))
        #print("Pipeline length: " + str(len(self.pipeline.executed_cats)) + ".")

        def show_settings():
            # Set background color while widget is selected. Doesn't work because of theme? *TODO*
            p = pip_main_widget.palette()
            p.setColor(pip_main_widget.backgroundRole(), Qt.red)
            pip_main_widget.setPalette(p)

            self.stackedWidget_Settings.show()
            self.stackedWidget_Settings.setCurrentIndex(self.pipeline.get_index(cat))
            self.settings_collapsable.setTitle(alg.get_name() + " Settings")

            self.remove_cat_alg_dropdown()

            # Create drop down for cats and algs
            self.create_cat_alg_dropdown(self.pipeline.get_index(cat), pip_main_widget, settings_main_widget)
            #print(cat)
            #print(alg)
            self.set_cat_alg_dropdown(cat, alg)

        # Connect Button to remove step from pipeline
        def delete_button_clicked():
            self.remove_pip_entry(pip_main_widget, settings_main_widget, cat)

        self.clickable(pixmap_label).connect(show_settings)
        self.clickable(string_label).connect(show_settings)
        btn.clicked.connect(delete_button_clicked)

        return (pip_main_widget, settings_main_widget)

    # https://wiki.python.org/moin/PyQt/Making%20non-clickable%20widgets%20clickable
    def clickable(self, widget):
        """
        Convert any widget to a clickable widget.
        """

        class Filter(QObject):

            clicked = pyqtSignal()

            def eventFilter(self, obj, event):

                if obj == widget:
                    if event.type() == QEvent.MouseButtonPress:
                        if obj.rect().contains(event.pos()):
                            self.clicked.emit()
                            # The developer can opt for .emit(obj) to get the object within the slot.
                            return True

                return False

        filter = Filter(widget)
        widget.installEventFilter(filter)
        return filter.clicked

class LeftCustomWidget(QWidget):
    """
    this widget is used in the left panel of the GUI. All intermediate
    result images are packed into a LeftCustomWidget and appended to the
    according vbox_layout of the Mainview.ui
    """

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.main_image_label = parent
        self.pixmap = None

    def set_image_label(self, image_label):
        """
        puts the image label at its place

        Args:
            | *image_label*: the string label of the image e.g. "preprocessing"
        """
        self.main_image_label = image_label

    def set_pixmap(self, pixmap):
        """
        puts the image pixmap on its place

        Args:
            | *pixmap*: the url to the intermediate result
        """
        self.pixmap = pixmap

    def mousePressEvent(self, event):
        """
        this events sets the self.pixmap from this custom widget
        into the middle panel of the GUI. Or more general: by clicking
        on this widget the users wants to see this picture in the big display
        area of the middle.

        Args:
            | *event*: the mouse press event
        """
        if event.button() == QtCore.Qt.LeftButton:
            self.main_image_label.setPixmap(QtGui.QPixmap(self.pixmap))


class PipCustomWidget(QWidget):
    """
    This Widget is used for the entry's in the pipeline of thr right
    GUI panel.
    """

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.main_image_label = parent
        self.pixmap = None

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.main_image_label.setPixmap(QtGui.QPixmap(self.pixmap))


class ComboBoxWidget(QGroupBox):
    """
    This is the combobox widget as it is shown in the settings
    panel of the GUI. It gets initialized with a name
    With self.valueChanged on can connect a pyqt slot with the
    combobox pyqtSignal.
    """

    def __init__(self, name, options, slot=None, default=None):
        super(ComboBoxWidget, self).__init__()
        self.activated = pyqtSignal()

        # ComboBox itself
        self.combobox = QtWidgets.QComboBox()
        self.combobox.orientationCombo = PyQt5.QtWidgets.QComboBox()
        self.combobox.setFixedWidth(220)

        # Label
        self.label = QtWidgets.QLabel()
        self.label.setText(name + ": ")

        self.SingleCheckBoxLayout = QBoxLayout(QBoxLayout.LeftToRight)
        self.SingleCheckBoxLayout.addWidget(self.label)
        self.SingleCheckBoxLayout.addWidget(self.combobox, Qt.AlignRight)
        self.setLayout(self.SingleCheckBoxLayout)
        self.setFixedHeight(70)
        self.setFlat(True)

        # options
        for i in options:
            self.add_item(i)

        if default is not None:
            index = self.combobox.findText(default)
            if index != -1:
                self.combobox.setCurrentIndex(index)

        if slot is not None:
            self.combobox.activated.connect(slot)


    def add_item(self, option, image=None):
        """

        Args:
            | *option*: A string option refers to an entry which can be selected in the combobox later.
            | *image*: An optional icon that can be shown combobox.
        """
        if image is None:
            self.combobox.addItem(option)
        else:
            self.combobox.addItem(QIcon(image), option)


class CheckBoxWidget(QGroupBox):
    """
    Thi sis the checkbox widget as it is shown in the GUI.
    The name is the displayed in fron of the checkbox in the GUI and
    the default value is of type boolean.
    With self.valueChanged on can connect a pyqt slot with the
    checkbox pyqtSignal.
    """

    def __init__(self, name, default, slot):
        super(CheckBoxWidget, self).__init__()
        self.stateChanged = pyqtSignal()

        # CheckBox itself
        self.checkbox = PyQt5.QtWidgets.QCheckBox()
        self.checkbox.setChecked(default)

        # Label
        self.label = PyQt5.QtWidgets.QLabel()
        self.label.setText(name + ": ")

        self.SingleCheckBoxLayout = PyQt5.QtWidgets.QGridLayout()
        self.SingleCheckBoxLayout.setAlignment(Qt.AlignLeft)
        self.SingleCheckBoxLayout.addWidget(self.label, 0, 0)
        self.SingleCheckBoxLayout.addWidget(self.checkbox, 0, 1)
        self.setLayout(self.SingleCheckBoxLayout)
        self.setFixedHeight(70)
        self.setFlat(True)

        self.checkbox.stateChanged.connect(slot)


class SliderWidget(QGroupBox):
    """
    This is a combined widget for a slider in the GUI. It
    contains several input fields and a slider itself. By setting
    the constructor value, the complete widget is connected in itself.
    The name will be displayed in front of the widget. lower and upper
    refer to the sliders range, step_size tells the distance of each step
    and default is the preset value in the GUI.
    The float_flag determines whether the slider should represent float values or not.
    Set float_flag to true if you want to store float values.
    With self.valueChanged on can connect a pyqt slot with the
    float slider pyqtSignal.
    A SliderWidget is built by a Slider, a QLabel and either a DoubleTextfield or an IntegerTextfield.
    """

    def __init__(self, name, lower, upper, step_size, default, slot, float_flag):
        super(SliderWidget, self).__init__()
        self.valueChanged = pyqtSignal()
        self.internal_steps = abs(upper - lower) / step_size

        print("Default " + str(default))

        def to_internal_coordinate(value):
            return (self.internal_steps / (upper - lower)) * (value - lower)

        def to_external_coordinate(value):
            return lower + (value * (upper - lower)) / self.internal_steps

        # Slider itself
        self.slider = \
            Slider(0, self.internal_steps, 1, to_internal_coordinate(default)).slider

        # Textfield
        if float_flag:
            self.textfield = \
                DoubleTextfield(lower, upper, step_size, default).textfield
        else:
            self.textfield = \
                IntegerTextfield(lower, upper, step_size, default).textfield

        # Label
        self.label = QLabel()
        self.label.setText(name + ": ")

        # Connect Textfield with Slider
        def textfield_value_changed(value):
            self.slider.setValue(to_internal_coordinate(value))

        def slider_value_changed(value):
            self.textfield.setValue(to_external_coordinate(value))

        self.textfield.valueChanged.connect(textfield_value_changed)
        self.slider.valueChanged.connect(slider_value_changed)

        self.SingleSlidersLayout = QBoxLayout(QBoxLayout.LeftToRight)
        self.SingleSlidersLayout.addWidget(self.label)
        self.SingleSlidersLayout.addWidget(self.slider)
        self.SingleSlidersLayout.addWidget(self.textfield)
        self.setLayout(self.SingleSlidersLayout)
        self.setFixedHeight(70)
        self.setFlat(True)

        self.textfield.valueChanged.connect(lambda : slot(self.textfield.value()))

        #self.textfield.setValue(default)


class IntegerTextfield(QSpinBox):
    """
    A customized QSpinBox that is used by the SliderWidget to allow users to enter integer values.
    """

    def __init__(self, lower, upper, step_size, default):
        super(IntegerTextfield, self).__init__()

        # Textfield
        self.textfield = QSpinBox()

        self.textfield.setRange(lower, upper)
        self.textfield.setSingleStep(step_size)
        self.textfield.setValue(default)
        self.textfield.setFixedWidth(75)


class DoubleTextfield(QDoubleSpinBox):
    """
    A customized QDoubleSpinBox that is used by the SliderWidget to allow users to enter float values.
    """

    def __init__(self, lower, upper, step_size, default):
        super(DoubleTextfield, self).__init__()

        # Textfield
        self.textfield = QDoubleSpinBox()

        self.textfield.setRange(lower, upper)
        self.textfield.setSingleStep(step_size)
        self.textfield.setValue(default)
        self.textfield.setFixedWidth(75)


class Slider(QSlider):
    """
    A customized QSlider that is used by the SliderWidget to allow users to change a certain setting.
    """

    def __init__(self, lower, upper, step_size, default):
        super(Slider, self).__init__()

        self.slider = QSlider(Qt.Horizontal)

        self.slider.setFocusPolicy(Qt.StrongFocus)
        self.slider.setTickPosition(QSlider.TicksBothSides)
        self.slider.setTickInterval(step_size)

        self.slider.setRange(lower, upper)
        self.slider.setSingleStep(step_size)
        self.slider.setValue(default)
        self.slider.setPageStep(step_size)


if __name__ == '__main__':
    pass
