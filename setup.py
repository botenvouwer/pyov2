import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyov2",
    version="1.0.0",
    author="William Loosman",
    author_email="william.wl@live.nl",
    description="Python module used to generate ov2 poi (point of interest) files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/botenvouwer/pyov2",
    project_urls={
        "Bug Tracker": "https://github.com/botenvouwer/pyov2/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
)
