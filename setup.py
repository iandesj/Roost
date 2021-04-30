from setuptools import setup

setup(name='roost',
      version='0.1',
      description='The greatest deployment tool for mono repos',
      url='http://github.com/iandesj/roost',
      author='Ian DesJardins',
      author_email='ian.d.desjardins@gmail.com',
      license='MIT',
      packages=['roost'],
      zip_safe=False,
      entry_points={
        'console_scripts': [
            'roost=roost.roost:main'
        ]
      })
