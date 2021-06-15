#!/usr/bin/env python

# Copyright 2018 Red Hat Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from setuptools import setup, find_packages
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# Version reading from yacfg/meta.py
# according to (3b) from:
# https://packaging.python.org/guides/single-sourcing-package-version/
meta = {}
meta_file = path.join(this_directory, 'src/yacfg/meta.py')
with open(meta_file, encoding='utf-8') as meta_file:
    exec(meta_file.read(), meta)

setup(
    name="yacfg",
    version='0.9.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    entry_points={
        'console_scripts': [
            'yacfg = yacfg.yacfg_cli:main',
            'yacfg-batch = yacfg_batch.yacfg_batch_cli:main'
        ],
    },
    install_requires=[
        'jinja2==2.11.3',
        'PyYAML==5.4.1',
    ],
    extras_require={
        'color_log': ['colorlog>=5.0.1,<6.0.0', 'colorama>=0.4.4,<0.5.0']
    },
    url='https://github.com/rh-messaging-qe/yacfg',
    license='Apache-2.0',
    author='Zdenek Kraus',
    author_email='zkraus@redhat.com',
    maintainer='Dominik Lenoch',
    maintainer_email='dlenoch@redhat.com',
    description="Template based configuration files generator based on jinja2 and yaml.",
    long_description=long_description,
    long_description_content_type='text/markdown',

    package_data={
        '': ['*'],
        'yacfg': [
            'profiles/_libs/*',
            'profiles/amq_broker/7.2.0/*',
            'profiles/amq_broker/7.2.0/_modules/bootstrap_xml/*',
            'profiles/amq_broker/7.2.0/cluster/*',
            'profiles/amq_broker/7.2.0/ha/*',
            'profiles/amq_broker/7.2.0/performance/*',
            'profiles/amq_broker/7.2.0/security/gssapi/*',
            'profiles/amq_broker/7.2.0/security/gssapi_ldap/*',
            'profiles/amq_broker/7.2.0/security/ssl/*',
            'profiles/amq_broker/7.2.0/store/jdbc/*',
            'profiles/amq_broker/7.4.0/*',
            'profiles/amq_broker/7.4.0/_modules/bootstrap_xml/*',
            'profiles/amq_broker/7.4.0/_modules/broker_xml/store/*',
            'profiles/amq_broker/7.4.0/cluster/*',
            'profiles/amq_broker/7.4.0/ha/*',
            'profiles/amq_broker/7.4.0/performance/*',
            'profiles/amq_broker/7.4.0/security/gssapi/*',
            'profiles/amq_broker/7.4.0/security/gssapi_ldap/*',
            'profiles/amq_broker/7.4.0/store/jdbc/*',
            'profiles/amq_broker/7.6.0/*',
            'profiles/amq_broker/7.6.0/_modules/bootstrap_xml/*',
            'profiles/amq_broker/7.6.0/_modules/broker_xml/store/*',
            'profiles/amq_broker/7.6.0/cluster/*',
            'profiles/amq_broker/7.6.0/ha/*',
            'profiles/amq_broker/7.6.0/performance/*',
            'profiles/amq_broker/7.6.0/security/gssapi/*',
            'profiles/amq_broker/7.6.0/security/gssapi_ldap/*',
            'profiles/amq_broker/7.6.0/store/jdbc/*',
            'profiles/amq_broker/7.7.0/*',
            'profiles/amq_broker/7.7.0/_modules/bootstrap_xml/*',
            'profiles/amq_broker/7.7.0/_modules/broker_xml/store/*',
            'profiles/amq_broker/7.7.0/cluster/*',
            'profiles/amq_broker/7.7.0/ha/*',
            'profiles/amq_broker/7.7.0/performance/*',
            'profiles/amq_broker/7.7.0/security/gssapi/*',
            'profiles/amq_broker/7.7.0/security/gssapi_ldap/*',
            'profiles/amq_broker/7.7.0/store/jdbc/*',
            'profiles/amq_broker/7.8.0/*',
            'profiles/amq_broker/7.8.0/_modules/bootstrap_xml/*',
            'profiles/amq_broker/7.8.0/_modules/broker_xml/store/*',
            'profiles/amq_broker/7.8.0/cluster/*',
            'profiles/amq_broker/7.8.0/ha/*',
            'profiles/amq_broker/7.8.0/performance/*',
            'profiles/amq_broker/7.8.0/security/gssapi/*',
            'profiles/amq_broker/7.8.0/security/gssapi_ldap/*',
            'profiles/amq_broker/7.8.0/store/jdbc/*',
            'profiles/amq_broker/7.8.1/*',
            'profiles/amq_broker/7.8.1/_modules/bootstrap_xml/*',
            'profiles/amq_broker/7.8.1/_modules/broker_xml/store/*',
            'profiles/amq_broker/7.8.1/cluster/*',
            'profiles/amq_broker/7.8.1/ha/*',
            'profiles/amq_broker/7.8.1/performance/*',
            'profiles/amq_broker/7.8.1/security/gssapi/*',
            'profiles/amq_broker/7.8.1/security/gssapi_ldap/*',
            'profiles/amq_broker/7.8.1/store/jdbc/*',
            'profiles/amq_broker/7.8.2/*',
            'profiles/amq_broker/7.8.2/_modules/bootstrap_xml/*',
            'profiles/amq_broker/7.8.2/_modules/broker_xml/store/*',
            'profiles/amq_broker/7.8.2/cluster/*',
            'profiles/amq_broker/7.8.2/ha/*',
            'profiles/amq_broker/7.8.2/performance/*',
            'profiles/amq_broker/7.8.2/security/gssapi/*',
            'profiles/amq_broker/7.8.2/security/gssapi_ldap/*',
            'profiles/amq_broker/7.8.2/store/jdbc/*',
            'profiles/artemis/2.13.0/*',
            'profiles/artemis/2.13.0/_modules/artemis_profile/*',
            'profiles/artemis/2.13.0/_modules/artemis_profile/performance/*',
            'profiles/artemis/2.13.0/_modules/bootstrap_xml/*',
            'profiles/artemis/2.13.0/_modules/broker_xml/*',
            'profiles/artemis/2.13.0/_modules/broker_xml/acceptors/*',
            'profiles/artemis/2.13.0/_modules/broker_xml/address_settings/*',
            'profiles/artemis/2.13.0/_modules/broker_xml/addresses/*',
            'profiles/artemis/2.13.0/_modules/broker_xml/cluster/*',
            'profiles/artemis/2.13.0/_modules/broker_xml/ha_policy/replication/*',
            'profiles/artemis/2.13.0/_modules/broker_xml/ha_policy/shared_store/*',
            'profiles/artemis/2.13.0/_modules/broker_xml/journal/*',
            'profiles/artemis/2.13.0/_modules/broker_xml/store/*',
            'profiles/artemis/2.13.0/_modules/jolokia_access/*',
            'profiles/artemis/2.13.0/_modules/logging_properties/*',
            'profiles/artemis/2.13.0/_modules/login_config/*',
            'profiles/artemis/2.13.0/_modules/management_xml/*',
            'profiles/artemis/2.13.0/_modules/security/jdk_gssapi/*',
            'profiles/artemis/2.13.0/_modules/users_roles_security/*',
            'profiles/artemis/2.13.0/cluster/*',
            'profiles/artemis/2.13.0/ha/*',
            'profiles/artemis/2.13.0/performance/*',
            'profiles/artemis/2.13.0/security/gssapi/*',
            'profiles/artemis/2.13.0/security/gssapi/ssl_tls/*',
            'profiles/artemis/2.13.0/security/gssapi_ldap/*',
            'profiles/artemis/2.13.0/store/jdbc/*',
            'profiles/artemis/2.14.0/*',
            'profiles/artemis/2.14.0/_modules/artemis_profile/*',
            'profiles/artemis/2.14.0/_modules/artemis_profile/performance/*',
            'profiles/artemis/2.14.0/_modules/bootstrap_xml/*',
            'profiles/artemis/2.14.0/_modules/broker_xml/*',
            'profiles/artemis/2.14.0/_modules/broker_xml/acceptors/*',
            'profiles/artemis/2.14.0/_modules/broker_xml/address_settings/*',
            'profiles/artemis/2.14.0/_modules/broker_xml/addresses/*',
            'profiles/artemis/2.14.0/_modules/broker_xml/cluster/*',
            'profiles/artemis/2.14.0/_modules/broker_xml/ha_policy/replication/*',
            'profiles/artemis/2.14.0/_modules/broker_xml/ha_policy/shared_store/*',
            'profiles/artemis/2.14.0/_modules/broker_xml/journal/*',
            'profiles/artemis/2.14.0/_modules/broker_xml/store/*',
            'profiles/artemis/2.14.0/_modules/jolokia_access/*',
            'profiles/artemis/2.14.0/_modules/logging_properties/*',
            'profiles/artemis/2.14.0/_modules/login_config/*',
            'profiles/artemis/2.14.0/_modules/management_xml/*',
            'profiles/artemis/2.14.0/_modules/security/jdk_gssapi/*',
            'profiles/artemis/2.14.0/_modules/users_roles_security/*',
            'profiles/artemis/2.14.0/cluster/*',
            'profiles/artemis/2.14.0/ha/*',
            'profiles/artemis/2.14.0/performance/*',
            'profiles/artemis/2.14.0/security/gssapi/*',
            'profiles/artemis/2.14.0/security/gssapi/ssl_tls/*',
            'profiles/artemis/2.14.0/security/gssapi_ldap/*',
            'profiles/artemis/2.14.0/store/jdbc/*',
            'profiles/artemis/2.15.0/*',
            'profiles/artemis/2.15.0/_modules/artemis_profile/*',
            'profiles/artemis/2.15.0/_modules/artemis_profile/performance/*',
            'profiles/artemis/2.15.0/_modules/bootstrap_xml/*',
            'profiles/artemis/2.15.0/_modules/broker_xml/*',
            'profiles/artemis/2.15.0/_modules/broker_xml/acceptors/*',
            'profiles/artemis/2.15.0/_modules/broker_xml/address_settings/*',
            'profiles/artemis/2.15.0/_modules/broker_xml/addresses/*',
            'profiles/artemis/2.15.0/_modules/broker_xml/cluster/*',
            'profiles/artemis/2.15.0/_modules/broker_xml/ha_policy/replication/*',
            'profiles/artemis/2.15.0/_modules/broker_xml/ha_policy/shared_store/*',
            'profiles/artemis/2.15.0/_modules/broker_xml/journal/*',
            'profiles/artemis/2.15.0/_modules/broker_xml/store/*',
            'profiles/artemis/2.15.0/_modules/jolokia_access/*',
            'profiles/artemis/2.15.0/_modules/logging_properties/*',
            'profiles/artemis/2.15.0/_modules/login_config/*',
            'profiles/artemis/2.15.0/_modules/management_xml/*',
            'profiles/artemis/2.15.0/_modules/security/jdk_gssapi/*',
            'profiles/artemis/2.15.0/_modules/users_roles_security/*',
            'profiles/artemis/2.15.0/cluster/*',
            'profiles/artemis/2.15.0/ha/*',
            'profiles/artemis/2.15.0/performance/*',
            'profiles/artemis/2.15.0/security/gssapi/*',
            'profiles/artemis/2.15.0/security/gssapi/ssl_tls/*',
            'profiles/artemis/2.15.0/security/gssapi_ldap/*',
            'profiles/artemis/2.15.0/store/jdbc/*',
            'profiles/artemis/2.16.0/*',
            'profiles/artemis/2.16.0/_modules/artemis_profile/*',
            'profiles/artemis/2.16.0/_modules/artemis_profile/performance/*',
            'profiles/artemis/2.16.0/_modules/bootstrap_xml/*',
            'profiles/artemis/2.16.0/_modules/broker_xml/*',
            'profiles/artemis/2.16.0/_modules/broker_xml/acceptors/*',
            'profiles/artemis/2.16.0/_modules/broker_xml/address_settings/*',
            'profiles/artemis/2.16.0/_modules/broker_xml/addresses/*',
            'profiles/artemis/2.16.0/_modules/broker_xml/cluster/*',
            'profiles/artemis/2.16.0/_modules/broker_xml/ha_policy/replication/*',
            'profiles/artemis/2.16.0/_modules/broker_xml/ha_policy/shared_store/*',
            'profiles/artemis/2.16.0/_modules/broker_xml/journal/*',
            'profiles/artemis/2.16.0/_modules/broker_xml/store/*',
            'profiles/artemis/2.16.0/_modules/jolokia_access/*',
            'profiles/artemis/2.16.0/_modules/logging_properties/*',
            'profiles/artemis/2.16.0/_modules/login_config/*',
            'profiles/artemis/2.16.0/_modules/management_xml/*',
            'profiles/artemis/2.16.0/_modules/security/jdk_gssapi/*',
            'profiles/artemis/2.16.0/_modules/users_roles_security/*',
            'profiles/artemis/2.16.0/cluster/*',
            'profiles/artemis/2.16.0/ha/*',
            'profiles/artemis/2.16.0/performance/*',
            'profiles/artemis/2.16.0/security/gssapi/*',
            'profiles/artemis/2.16.0/security/gssapi/ssl_tls/*',
            'profiles/artemis/2.16.0/security/gssapi_ldap/*',
            'profiles/artemis/2.16.0/store/jdbc/*',
            'profiles/artemis/2.17.0/*',
            'profiles/artemis/2.17.0/_modules/artemis_profile/*',
            'profiles/artemis/2.17.0/_modules/artemis_profile/performance/*',
            'profiles/artemis/2.17.0/_modules/bootstrap_xml/*',
            'profiles/artemis/2.17.0/_modules/broker_xml/*',
            'profiles/artemis/2.17.0/_modules/broker_xml/acceptors/*',
            'profiles/artemis/2.17.0/_modules/broker_xml/address_settings/*',
            'profiles/artemis/2.17.0/_modules/broker_xml/addresses/*',
            'profiles/artemis/2.17.0/_modules/broker_xml/cluster/*',
            'profiles/artemis/2.17.0/_modules/broker_xml/ha_policy/replication/*',
            'profiles/artemis/2.17.0/_modules/broker_xml/ha_policy/shared_store/*',
            'profiles/artemis/2.17.0/_modules/broker_xml/journal/*',
            'profiles/artemis/2.17.0/_modules/broker_xml/store/*',
            'profiles/artemis/2.17.0/_modules/jolokia_access/*',
            'profiles/artemis/2.17.0/_modules/logging_properties/*',
            'profiles/artemis/2.17.0/_modules/login_config/*',
            'profiles/artemis/2.17.0/_modules/management_xml/*',
            'profiles/artemis/2.17.0/_modules/security/jdk_gssapi/*',
            'profiles/artemis/2.17.0/_modules/users_roles_security/*',
            'profiles/artemis/2.17.0/cluster/*',
            'profiles/artemis/2.17.0/ha/*',
            'profiles/artemis/2.17.0/performance/*',
            'profiles/artemis/2.17.0/security/gssapi/*',
            'profiles/artemis/2.17.0/security/gssapi/ssl_tls/*',
            'profiles/artemis/2.17.0/security/gssapi_ldap/*',
            'profiles/artemis/2.17.0/store/jdbc/*',
            'profiles/artemis/2.5.0/*',
            'profiles/artemis/2.5.0/_modules/artemis_profile/*',
            'profiles/artemis/2.5.0/_modules/artemis_profile/performance/*',
            'profiles/artemis/2.5.0/_modules/bootstrap_xml/*',
            'profiles/artemis/2.5.0/_modules/broker_xml/*',
            'profiles/artemis/2.5.0/_modules/broker_xml/acceptors/*',
            'profiles/artemis/2.5.0/_modules/broker_xml/address_settings/*',
            'profiles/artemis/2.5.0/_modules/broker_xml/addresses/*',
            'profiles/artemis/2.5.0/_modules/broker_xml/cluster/*',
            'profiles/artemis/2.5.0/_modules/broker_xml/ha_policy/replication/*',
            'profiles/artemis/2.5.0/_modules/broker_xml/ha_policy/shared_store/*',
            'profiles/artemis/2.5.0/_modules/broker_xml/journal/*',
            'profiles/artemis/2.5.0/_modules/broker_xml/store/*',
            'profiles/artemis/2.5.0/_modules/jolokia_access/*',
            'profiles/artemis/2.5.0/_modules/logging_properties/*',
            'profiles/artemis/2.5.0/_modules/login_config/*',
            'profiles/artemis/2.5.0/_modules/management_xml/*',
            'profiles/artemis/2.5.0/_modules/security/jdk_gssapi/*',
            'profiles/artemis/2.5.0/_modules/users_roles_security/*',
            'profiles/artemis/2.5.0/cluster/*',
            'profiles/artemis/2.5.0/ha/*',
            'profiles/artemis/2.5.0/performance/*',
            'profiles/artemis/2.5.0/security/gssapi/*',
            'profiles/artemis/2.5.0/store/jdbc/*',
            'profiles/artemis/2.6.0/*',
            'profiles/artemis/2.6.0/_modules/artemis_profile/*',
            'profiles/artemis/2.6.0/_modules/artemis_profile/performance/*',
            'profiles/artemis/2.6.0/_modules/bootstrap_xml/*',
            'profiles/artemis/2.6.0/_modules/broker_xml/*',
            'profiles/artemis/2.6.0/_modules/broker_xml/acceptors/*',
            'profiles/artemis/2.6.0/_modules/broker_xml/address_settings/*',
            'profiles/artemis/2.6.0/_modules/broker_xml/addresses/*',
            'profiles/artemis/2.6.0/_modules/broker_xml/cluster/*',
            'profiles/artemis/2.6.0/_modules/broker_xml/ha_policy/replication/*',
            'profiles/artemis/2.6.0/_modules/broker_xml/ha_policy/shared_store/*',
            'profiles/artemis/2.6.0/_modules/broker_xml/journal/*',
            'profiles/artemis/2.6.0/_modules/broker_xml/store/*',
            'profiles/artemis/2.6.0/_modules/jolokia_access/*',
            'profiles/artemis/2.6.0/_modules/logging_properties/*',
            'profiles/artemis/2.6.0/_modules/login_config/*',
            'profiles/artemis/2.6.0/_modules/management_xml/*',
            'profiles/artemis/2.6.0/_modules/security/jdk_gssapi/*',
            'profiles/artemis/2.6.0/_modules/users_roles_security/*',
            'profiles/artemis/2.6.0/cluster/*',
            'profiles/artemis/2.6.0/ha/*',
            'profiles/artemis/2.6.0/performance/*',
            'profiles/artemis/2.6.0/security/gssapi/*',
            'profiles/artemis/2.6.0/security/gssapi/ssl_tls/*',
            'profiles/artemis/2.6.0/security/gssapi_ldap/*',
            'profiles/artemis/2.6.0/store/jdbc/*',
            'profiles/artemis/2.9.0/*',
            'profiles/artemis/2.9.0/_modules/artemis_profile/*',
            'profiles/artemis/2.9.0/_modules/artemis_profile/performance/*',
            'profiles/artemis/2.9.0/_modules/bootstrap_xml/*',
            'profiles/artemis/2.9.0/_modules/broker_xml/*',
            'profiles/artemis/2.9.0/_modules/broker_xml/acceptors/*',
            'profiles/artemis/2.9.0/_modules/broker_xml/address_settings/*',
            'profiles/artemis/2.9.0/_modules/broker_xml/addresses/*',
            'profiles/artemis/2.9.0/_modules/broker_xml/cluster/*',
            'profiles/artemis/2.9.0/_modules/broker_xml/ha_policy/replication/*',
            'profiles/artemis/2.9.0/_modules/broker_xml/ha_policy/shared_store/*',
            'profiles/artemis/2.9.0/_modules/broker_xml/journal/*',
            'profiles/artemis/2.9.0/_modules/broker_xml/store/*',
            'profiles/artemis/2.9.0/_modules/jolokia_access/*',
            'profiles/artemis/2.9.0/_modules/logging_properties/*',
            'profiles/artemis/2.9.0/_modules/login_config/*',
            'profiles/artemis/2.9.0/_modules/management_xml/*',
            'profiles/artemis/2.9.0/_modules/security/jdk_gssapi/*',
            'profiles/artemis/2.9.0/_modules/users_roles_security/*',
            'profiles/artemis/2.9.0/cluster/*',
            'profiles/artemis/2.9.0/ha/*',
            'profiles/artemis/2.9.0/performance/*',
            'profiles/artemis/2.9.0/security/gssapi/*',
            'profiles/artemis/2.9.0/security/gssapi/ssl_tls/*',
            'profiles/artemis/2.9.0/security/gssapi_ldap/*',
            'profiles/artemis/2.9.0/store/jdbc/*',
            'templates/artemis/2.13.0/*',
            'templates/artemis/2.13.0/modules/broker_xml/*',
            'templates/artemis/2.13.0/modules/broker_xml/ha_policy/*',
            'templates/artemis/2.13.0/modules/broker_xml/security_settings/*',
            'templates/artemis/2.13.0/modules/broker_xml/store/*',
            'templates/artemis/2.14.0/*',
            'templates/artemis/2.14.0/modules/broker_xml/*',
            'templates/artemis/2.14.0/modules/broker_xml/ha_policy/*',
            'templates/artemis/2.14.0/modules/broker_xml/security_settings/*',
            'templates/artemis/2.14.0/modules/broker_xml/store/*',
            'templates/artemis/2.15.0/*',
            'templates/artemis/2.15.0/modules/broker_xml/*',
            'templates/artemis/2.15.0/modules/broker_xml/ha_policy/*',
            'templates/artemis/2.15.0/modules/broker_xml/security_settings/*',
            'templates/artemis/2.15.0/modules/broker_xml/store/*',
            'templates/artemis/2.16.0/*',
            'templates/artemis/2.16.0/modules/broker_xml/*',
            'templates/artemis/2.16.0/modules/broker_xml/ha_policy/*',
            'templates/artemis/2.16.0/modules/broker_xml/security_settings/*',
            'templates/artemis/2.16.0/modules/broker_xml/store/*',
            'templates/artemis/2.17.0/*',
            'templates/artemis/2.17.0/modules/broker_xml/*',
            'templates/artemis/2.17.0/modules/broker_xml/ha_policy/*',
            'templates/artemis/2.17.0/modules/broker_xml/security_settings/*',
            'templates/artemis/2.17.0/modules/broker_xml/store/*',
            'templates/artemis/2.5.0/*',
            'templates/artemis/2.5.0/modules/broker_xml/*',
            'templates/artemis/2.5.0/modules/broker_xml/ha_policy/*',
            'templates/artemis/2.5.0/modules/broker_xml/security_settings/*',
            'templates/artemis/2.5.0/modules/broker_xml/store/*',
            'templates/artemis/2.6.0/*',
            'templates/artemis/2.6.0/modules/broker_xml/*',
            'templates/artemis/2.6.0/modules/broker_xml/ha_policy/*',
            'templates/artemis/2.6.0/modules/broker_xml/security_settings/*',
            'templates/artemis/2.6.0/modules/broker_xml/store/*',
            'templates/artemis/2.9.0/*',
            'templates/artemis/2.9.0/modules/broker_xml/*',
            'templates/artemis/2.9.0/modules/broker_xml/ha_policy/*',
            'templates/artemis/2.9.0/modules/broker_xml/security_settings/*',
            'templates/artemis/2.9.0/modules/broker_xml/store/*',
            'templates/libs/*',
            'templates/libs/headers/*',
            'templates/libs/licenses/apache-2.0/*'
        ]
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: MacOS',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Software Development :: Code Generators',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Testing',
        'Topic :: System :: Installation/Setup',
        'Topic :: System :: Systems Administration',
        'Topic :: Text Processing',
        'Topic :: Utilities'
    ],
)
