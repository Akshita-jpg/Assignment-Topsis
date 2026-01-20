from setuptools import setup, find_packages

setup(
    name="topsisAkshita",
    version="1.0.0",
    author="Akshita",
    description="TOPSIS implementation as a Python package",
    packages=find_packages(),
    install_requires=["pandas", "numpy"],
    entry_points={
        'console_scripts': [
            'topsis=topsis.topsis:main'
        ]
    },
)
