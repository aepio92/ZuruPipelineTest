import maya.cmds as cmds
from PySide2 import QtWidgets


class MyDockableWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(MyDockableWindow, self).__init__(parent)
        self.setObjectName("MayaQtWindow")
        self.setWindowTitle("Maya Qt Window")
        self.setMinimumSize(200, 100)

        # Creating layout and widgets
        layout = QtWidgets.QVBoxLayout(self)
        label = QtWidgets.QLabel("QT Window")
        layout.addWidget(label)

        # Adding a button
        button = QtWidgets.QPushButton("Show Selected Objects")
        layout.addWidget(button)

        # Connecting button click to a function
        button.clicked.connect(self.on_button_clicked)

    def on_button_clicked(self):
        selected_objects = cmds.ls(selection=True, long=True)
        if selected_objects:
            print("Selected Objects:")
            for obj in selected_objects:
                print(obj)
        else:
            print("No objects selected.")


def create_dockable_window():
    global dockable_window

    # Checking if the dock exists
    if cmds.dockControl("myDock", exists=True):
        cmds.deleteUI("myDock", control=True)

    # Creating the dock control
    dock_control = cmds.dockControl(
        area='left',
        floating=True,
        content="MayaQtWindow",
        allowedArea=('right', 'left'),
        label="Maya Qt Window",
        width=200
    )

    # Showing the main window
    dockable_window.show()


# Creating an instance of the MyDockableWindow class
dockable_window = MyDockableWindow()

# Calling the function to create the dockable window
create_dockable_window()
