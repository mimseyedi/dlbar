from setuptools import setup
from pathlib import Path
from importlib import import_module


HERE = Path(__file__).parent
README = (HERE / "README.md").read_text()

install_requires = ['requests']
dependency_links = ['requests']

setup(
 name = 'dlbar',
 description = 'dlbar is a simple terminal progress bar for downloading and displaying download progress.',
 version = import_module('dlbar').__version__,
 packages = ['dlbar'],
 install_requires = install_requires,
 python_requires='>=3.10',
 author="mimseyedi",
 keyword=["dlbar", "Python", "CLI", "download", "progressbar"],
 long_description=README,
 long_description_content_type="text/markdown",
 license='MIT',
 url='https://github.com/mimseyedi/dlbar',
 dependency_links=dependency_links,
 author_email='mim.seyedi@gmail.com',
 classifiers=[
        "License :: OSI Approved :: MIT License",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Topic :: Utilities"
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ]
)