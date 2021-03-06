from setuptools import find_packages
from setuptools import setup

with open('requirements.txt') as f:
    content = f.readlines()
requirements = [x.strip() for x in content if 'git+' not in x]

setup(name='ia_first_package',
      version="1.0",
      description="A test to package sharing",
      packages=find_packages(),
      install_requires=requirements,
      url='https://github.com/iavaq/ia_first_package',
      test_suite='tests',
      # include_package_data: to install data from MANIFEST.in
      include_package_data=True,
      scripts=['scripts/ia_first_package-run'],
      zip_safe=False)
