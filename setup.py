from setuptools import setup, find_packages

setup(
    name="dictionary_methods",
    version="0.0.10",
    description="A simple Python package for dictionary operations",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Yabra Muvdi",
    license="Apache 2.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    url="",
    install_requires=["pandas>=1.0.0"],
    extras_require={"dev": ["pytest>=7.0.0", "twine>=4.0.2"]},
    python_requires=">=3.6",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)