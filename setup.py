from setuptools import setup

setup(name='gqgmc-prometheus-exporter',
      version='0.1',
      description='GQ GMC geiger counter prometheus exporter',
      url='https://github.com/slashdevsda/gqgmc-prometheus-exporter',
      author='Slashdevsda',
      author_email='',
      license='MIT',
      install_requires=[
        'prometheus-client==0.13.1',
        'pyserial==3.5',
      ],      
      packages=['src'],
      entry_points = {
        'console_scripts': ['gqgmc-prometheus-exporter=src.main:main'],
      }
)
