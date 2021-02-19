import setuptools

setuptools.setup(
    name="genpasswd-everdrone",
    version="2.0.2",
    author="Giorgio Tropiano",
    author_email="giorgiotropiano@gmail.com",
    description="Password Generator",
    long_description=open('readme.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/everdrone/genpasswd2",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    license='MIT',
    entry_points={
        'console_scripts': ['genpasswd=genpasswd.cli:main']
    },
    install_requires=[],
    python_requires='>=3.7.5',
)
