from distutils.core import setup
setup(
  name = 'artificial-neural-network',
  packages = ['artificial-neural-network'],
  version = '0.1',
  license='gpl-3.0',
  description = 'Easy to use artificial neural network library in Python based from Keras library.',
  author = 'Ivan Dustin Bilon',
  author_email = 'ivan22.dust@gmail.com',
  url = 'https://github.com/ivandustin/neural',
  keywords = ['easy to use', 'artificial neural network', 'beginners'],
  install_requires=[
          'keras',
          'tensorflow',
      ]
)
