from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='map_motif2_code',
      version='0.1',
      description='Map Motif python module',
      long_description=readme(),
      classifiers=[
      	'Programming Language :: Python :: 3'
      ],
      url='https://github.com/DiscoveryDNA/map_motif2',
      author='Joanne Chen',
      packages=['map_motif2_code'],
      dependency_links=['https://github.com/DiscoveryDNA/map_motif2'],
      scripts=['bin/test_script.py'],
      zip_safe=False)