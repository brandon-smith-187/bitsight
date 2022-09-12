from setuptools import setup

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='bitsight',
    version='0.2.2',
    packages=['bitsight', 'bitsight.api_io', 'bitsight.resources'],
    url='https://github.com/brandon-smith-187/bitsight',
    license='MIT',
    author='Brandon Smith',
    author_email='bcsmith2@gmail.com',
    description='Unofficial Package for BitSight\'s API',
    long_description=long_description,
    long_description_content_type='text/markdown',
    python_requires='>=3.7',
    install_requires=[
        'requests>=2.28.1',
    ],
)
