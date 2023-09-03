from setuptools import setup, find_namespace_packages

setup(name='a_book',
      version='1.01',
      description='Assistant bot',
      url='https://github.com/OleksaSolo/a_book',
      author='Oleksa Sol',
      author_email='9095945s@gmail.com',
      license='MIT',
      packages=find_namespace_packages(),
      entry_points={'console_scripts': ['a-book = a_book.__main__:when_out']}
)