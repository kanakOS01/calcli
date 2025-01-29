from setuptools import setup

setup(
    name="calcli",
    version="1.0",
    packages=["calcli"],
    entry_points={
        "console_scripts": ["calcli = calcli.__main__:main"],
    },
    description="A CLI calculator using argparse",
    author="Kanak Tanwar",
    url="https://github.com/kanakOS01/calcli.git",
    python_requires=">=3.6",
)
