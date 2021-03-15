# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name="OpenFisca-France-Local",
    version="0.0.3",
    description="Extension OpenFisca pour nos partenariats avec les collectivités territoriales",
    license="http://www.fsf.org/licensing/licenses/agpl-3.0.html",
    author="",
    packages=find_packages(),
    include_package_data=True,
    install_requires = [
        'Openfisca-Core @ git+https://github.com/mes-aides/openfisca-core.git@m1#egg=Openfisca-Core[web-api]',
        'openfisca-France @ git+https://github.com/mes-aides/openfisca-france.git@m1#egg=openfisca-France'
        ],
    extras_require = {
        'test': [
            'nose',
            ],
        'excel-reader': [
            'pandas >= 1.2.3',
            'xlrd == 1.2.0'
            ]
        },
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
    ],
    scripts=['openfisca_france_local/scripts/openfisca_local_test']
)
