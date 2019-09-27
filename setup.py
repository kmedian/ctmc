from setuptools import setup


def read(fname):
    import os
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(name='ctmc',
      version='0.1.3',
      description='Continous Time Markov Chain',
      long_description=read('README.md'),
      long_description_content_type='text/markdown',
      url='http://github.com/kmedian/ctmc',
      author='Ulf Hamster',
      author_email='554c46@gmail.com',
      license='MIT',
      packages=['ctmc'],
      install_requires=[
          'setuptools>=40.0.0',
          'nose>=1.3.7',
          'numpy>=1.14.5',
          'scipy>=1.1.0',
          'scikit-learn>=0.19.2'],
      python_requires='>=3.6',
      zip_safe=False)
