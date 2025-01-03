from setuptools import setup, find_packages

setup(
    name='network-tool',
    version='0.1.0',
    author='Amir-Mahdi-Zare',
    author_email='mahnaznamani007@gmail.com',
    description='A Python-based tool for advanced network commands with a GUI.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/amir13872/network-tool',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'tkinter',  # Add other dependencies as needed
        # 'other-dependency',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
