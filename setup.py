import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyjboss", 
    version="0.0.5",
    license="GNU General Public License v3.0",
    author="Rafael Benites Gil",
    author_email="rafaelbgil@gmail.com",
    description="Python client for Jboss and Wildfly api",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rafaelbgil/pyjboss",
    py_modules=['pyjboss'],
    packages=setuptools.find_packages(),
    classifiers=[
	"Development Status :: 3 - Alpha",
	"Programming Language :: Python",
	"Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
	"Programming Language :: Python :: 3.0",
	"Programming Language :: Python :: 3.1",
	"Programming Language :: Python :: 3.2",
	"Programming Language :: Python :: 3.3",
	"Programming Language :: Python :: 3.4",
	"Programming Language :: Python :: 3.5",
	"Programming Language :: Python :: 3.6",
	"Programming Language :: Python :: 3.7",
	"Programming Language :: Python :: 3.8",
	"Programming Language :: Python :: 3.9",
	"License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    install_requires = ['requests'],
    python_requires='>=2.7',
)
