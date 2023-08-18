from setuptools import setup, Extension

__version__ = '0.0.4'


setup(
    name='binance-decoder',
    version=__version__,
    description='Binance decoder',

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
