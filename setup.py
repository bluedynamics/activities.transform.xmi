from setuptools import setup, find_packages
import sys, os

version = '1.0'
shortdesc ="XMI Transformation for Activities"
longdesc = open(os.path.join(os.path.dirname(__file__), 'README.txt')).read()
longdesc += open(os.path.join(os.path.dirname(__file__), 'LICENSE.txt')).read()

setup(name='activities.transform.xmi',
      version=version,
      description=shortdesc,
      long_description=longdesc,
      classifiers=[
            'Development Status :: 3 - Alpha',
            'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Framework :: Zope3',
            'Intended Audience :: Developers',
            'Topic :: Software Development :: Libraries :: Python Modules'
      ], # Get strings from http://pypi.python.org/pypi?:action=list_classifiers
      keywords='UML Activities xmi transformation',
      author='Johannes Raggam',
      author_email='',
      url='',
      license='LGPL',
      packages = find_packages('src'),
      package_dir = {'': 'src'},
      namespace_packages=['activities','activities.transform'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*
          'activities.metamodel',
          'zope.interface',
          'agx.core',
          'agx.io.xml',
      ],
      extras_require={
          'test': [
              'interlude',
              'zope.component',
              'zope.configuration', # may not only needed by tests? (zcml...)
          ]
      },
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
