from setuptools import setup

VERSION = '0.0.1'
DESCRIPTION = 'Beautifully simple animations'
LONG_DESCRIPTION = 'A content-oriented package to create animations'

setup(
    name="animate",
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    author="Raphaël Candelier",
    author_email="raphael.candelier@sorbonne-universite.fr",
    license='GNU GPL v3',
    packages=['animate'],
    install_requires=['numpy', 'matplotlib', 'pyqt6', 'imageio[ffmpeg]'],
    keywords='conversion',
    classifiers= [
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Education",
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering :: Visualization",
    ]
)
