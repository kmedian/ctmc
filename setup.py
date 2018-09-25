from setuptools import setup


def read(fname):
    import os
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(name='ctmc',
      version='0.1.0',
      description='Continous Time Markov Chain',
      long_description=read('README.md'),
      long_description_content_type='text/markdown',
      url='http://github.com/kmedian/ctmc',
      author='Ulf Hamster',
      author_email='554c46@gmail.com',
      license='MIT',
      packages=['ctmc'],
      install_requires=['setuptools', 'nose', 'numpy', 'scipy'],
      python_requires='>=3',
      zip_safe=False)
