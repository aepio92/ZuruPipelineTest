from setuptools import setup

setup(
    name="pyls",
    version="0.1.0",
    py_modules=["pyls"],

    entry_points={
        "console_scripts": [
            "pyls = pyls:main"
        ]
    },
)