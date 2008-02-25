from setuptools import setup, find_packages
import os.path

versionfile = open(os.path.join('xm', 'booking', 'version.txt'))
version = versionfile.read().strip()
versionfile.close()

readmefile = open(os.path.join('xm', 'booking', 'README.txt'))
readme = readmefile.read().strip()
readmefile.close()


setup(name='xm.booking',
      version=version,
      description="Bookings for eXtremeManagement",
      long_description=readme,
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Framework :: Zope2",
        "Framework :: Zope3",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='eXtremeManagement booking',
      author='Maurits van Rees',
      author_email='m.van.rees@zestsoftware.nl',
      url="http://plone.org/products/extreme-management-tool/",
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['xm'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
