from setuptools import setup

APP=["gui.py"]
OPTIONS = {
    "argv_emulation": True,
}

setup(
    app =APP,
    options ={"py2app":OPTIONS},
    setup_requires=["py2app"]
)

#quindi dare il comando python3 setup.py  py2app