import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="aqiretrieve-sai-manoj-bharadwaj", # Replace with your own username
    version="0.0.1",
    author="Sai Manoj",
    author_email="mnjkshrm@gmail.com",
    description="A python package for retrieving AQI from EPA",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://https://github.com/Manojython/aqirereive",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
