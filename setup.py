from setuptools import setup

setup(
    name='map card maker',
    version='1.0',
    packages=['map_card_maker'],
    entry_points={
        'console_scripts': ['map_card_maker = map_card_maker.__main__:main']
    },
    url='',
    license='MIT License',
    author='pcalg',
    author_email='',
    description='create your own map cards.'
)