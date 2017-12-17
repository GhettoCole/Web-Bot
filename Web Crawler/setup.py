from setuptools import set, find_packages

setup(
        name="WEB BOT",
        version="0.0.1",
        url="https://www.github.com/GhettoCole/Web-Bot/",
        license="GNU",
        author="Given Lepita",
        packages=find_packages(),
        install_requires=[
            "prettytable", "bs4", "requests",
        ],
        entry_points={},
        extras_require={},
)
