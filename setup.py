from datetime import datetime
from pathlib import Path
from setuptools import setup, find_packages


BASEDIR = Path(__file__).absolute().parent


def _get_local_file(file_path):
    """Load file in same directory than setup.py."""
    return open(
        BASEDIR.joinpath(file_path), 'r', encoding='utf-8'
    )


def _get_requirements(requirements_file="requirements.txt"):
    """Parse requirements.txt and return list."""
    requirements_file = BASEDIR.joinpath(requirements_file)
    if requirements_file.is_file():
        with open(requirements_file, 'r') as requirements:
            # Ensure deps order
            return [
                line.strip() for line in reversed(requirements.readlines())
                if not line.startswith('#')
            ]
        return []


VERSION = _get_local_file("VERSION").read().strip() or  datetime.today().strftime("%Y.%m.%d")


setup(
    # Project informations
    name='hackathon',
    version=VERSION,
    author='Grympler',
    author_email='grympler@protonmail.com',
    maintainer="Grympler",
    maintainer_email="grympler@protonmail.com",
    url="https://github.com/grympler/hackathon",
    download_url="https://github.com/grympler/hackathon",

    # License and description
    license=_get_local_file("LICENSE").read(),
    description='42',
    long_description=_get_local_file("README.md").read() + "\n",

    # requirements
    install_requires=_get_requirements(),

    # Package, scripts informations
    packages=find_packages(),
    package_data={'': ["*.tar.xz"]},
    include_package_data=True,
    classifiers=[
        'Environment :: Console',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3 :: Only',
        'License :: Other/Proprietary License'
    ],
    # Magic !
    zip_safe=False
)
