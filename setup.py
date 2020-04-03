from setuptools import setup, find_packages
from os import path
from io import open

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='addletterboxcv',
    version='0.1.3',
    description='Add a letterbox to the video and scale it to the specified size.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/makutamoto/addletterboxcv',
    author='Makutamoto',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: End Users/Desktop',
        'Topic :: Multimedia :: Video :: Conversion',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    keywords='video letterbox resize',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    python_requires='>=3.6',
    install_requires=['opencv-python', 'numpy', 'tqdm'],
    entry_points={
        'console_scripts': [
            'addletterboxcv=addletterboxcv:main',
        ],
    },
    project_urls={
        'Bug Reports': 'https://github.com/makutamoto/addletterboxcv/issues',
        'Source': 'https://github.com/makutamoto/addletterboxcv',
    },
)
