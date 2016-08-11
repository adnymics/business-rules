#! /usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools

with open('HISTORY.rst') as f:
    history = f.read()

description = 'Python DSL for setting up business intelligence rules that can be configured without code'

version = '0.0.0'
with open('project.json', 'r') as pj:
    try:
        version = json.loads(pj.read()).get('version', '0.0.0')
    except Exception as exp:
        raise Exception('failed to read project.json: {}'.format(exp.message))

setuptools.setup(
        name='business-rules',
        version=version,
        description='{0}\n\n{1}'.format(description, history),
        author='Venmo',
        author_email='open-source@venmo.com',
        url='https://github.com/venmo/business-rules',
        packages=['business_rules'],
        license='MIT'
)
