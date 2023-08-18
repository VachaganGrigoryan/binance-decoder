from setuptools import setup, Extension
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

__version__ = '0.0.5'


setup(
    name='binance-decoder',
    version=__version__,
    description='Binance decoder',
    long_description=long_description,
    long_description_content_type='text/markdown',

    author='Vachagan Grigoryan',
    author_email='vachagan.grigoryan@outlook.com',
    url='https://github.com/VachaganGrigoryan/binance-decoder',

    setup_requires=['setuptools-golang'],
    extras_require={
        'test': ['pytest'],
    },
    ext_modules=[
        Extension('binance_decoder', ['decoder/binance_decoder.go']),
    ],
    build_golang={'root': 'github.com/VachaganGrigoryan/binance-decoder'},
)
