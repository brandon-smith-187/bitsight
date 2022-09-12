from setuptools import setup

setup(
    name='bitsight',
    version='0.2.1',
    packages=['bitsight', 'bitsight.api_io', 'bitsight.resources'],
    url='https://github.com/brandon-smith-187/bitsight',
    license='MIT',
    author='Brandon Smith',
    author_email='bcsmith2@gmail.com',
    description='Unofficial Package for BitSight\'s API',
    python_requires='>=3.7',
    install_requires=[
        'requests>=2.28.1',
    ],
)
