from setuptools import setup, find_packages

setup(
    name="antlr4-cypher",
    version="0.1.2",
    author="qihua",
    author_email="qihua147@qq.com",
    description="A Python package for parsing Cypher queries using ANTLR4.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/qi-hua/antlr4-cypher",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "antlr4-python3-runtime>=4.9.0",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)