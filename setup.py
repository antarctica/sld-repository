from pathlib import Path
from setuptools import setup, find_packages


def _get_long_description() -> str:
    with open(Path('README.md'), 'r') as readme:
        return readme.read()


def _get_version() -> str:
    if Path('APP_RELEASE.txt').exists():
        with open(Path('APP_RELEASE.txt'), 'r') as version:
            return str(version.read()).strip()

    return 'unknown'


setup(
    name="bas-sld-repository",
    version=_get_version(),
    author="British Antarctic Survey",
    author_email="webapps@bas.ac.uk",
    description="Automated backup of SLDs used to style web map data provided by the BAS Mapping and Geographic "
                "Information Centre (MAGIC).",
    long_description=_get_long_description(),
    long_description_content_type="text/markdown",
    url="https://github.com/antarctica/sld-repository",
    license='Open Government Licence v3.0',
    install_requires=[
        'Flask==1.1.1',
        'geoserver-restconfig==1.0.2',
        'python-dotenv==0.10.3',
        'str2bool==1.1',
        'sentry-sdk[flask]==0.13.4'
    ],
    packages=find_packages(exclude=['tests']),
    package_data={'bas_sld_repository': ['../APP_RELEASE.txt']},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Framework :: Flask",
        "Development Status :: 3 - Alpha",
        "License :: Other/Proprietary License",
        "Operating System :: OS Independent",
        "Intended Audience :: Science/Research"
    ],
)
