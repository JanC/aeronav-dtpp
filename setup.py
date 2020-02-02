from setuptools import setup

setup(
    name='anm-dtpp',
    version='0.1.0',
    packages=['anm_charts', 'anm_charts.lib'],
    entry_points={
        'console_scripts': [
            'anm-dtpp = anm_charts.__main__:cli'
        ]
    }, install_requires=['click', 'requests'])
