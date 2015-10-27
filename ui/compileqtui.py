import os


def setup_resource():
    os.system('pyrcc5 key-resource.qrc -o key-resource_rc.py')


def setup_ui():
    os.system('pyuic5 -x keyboard-ui.ui -o keyboard_ui.py')


# setup_resource()
setup_ui()
