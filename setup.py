from setuptools import setup, find_packages
setup(name='logs',
      version='0.1',
      url='https://github.com/FaserGer853/Logs',
      license='MIT',
      author='Joooai',
      author_email='funnycartoonsyt@gmail.com',
      description='Just a basic Logs python module',
      packages=find_packages(exclude=['tests']),
      long_description=open('README.md').read(),
      zip_safe=False,
      setup_requires=['nose'],
      test_suite='nose.collector')
