from setuptools import find_packages, setup


def get_long_description():
    """Read in the README.md for use as the package's long description.

    Returns:
        long description (str)
    """
    with open("README.md", "r") as readme:
        long_description = readme.read()
    return long_description


setup(
    name="jupyter-notebook-service",
    version="0.3.0",
    description="Simple flask app",
    long_description=get_long_description(),
    packages=find_packages(exclude=("tests*",)),
    include_package_data=True,
    python_requires=", ".join(["~= 3.7.12",]),
    install_requires=["Flask", "gevent", "gunicorn", "prometheus-client",],
    tests_require=["black", "pytest", "pytest-cov",],
)
