from setuptools import setup, find_packages

# run this: python3 setup.py sdist bdist_wheel
setup(
    name='ft_package',
    version='0.0.1',
    author='Ijon Tan',
    license='MIT',
    author_email="ijontan@gmail.com",
    description="A simple test package",
    url="https://github.com/ijontan/python_dataScience_0",
    packages=find_packages(),
)
