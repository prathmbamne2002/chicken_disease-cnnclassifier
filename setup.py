import setuptools
with open("README.md", "r",encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "chicken_disease-cnnclassifier"
AUTHOR_NAME = "Prathmesh Bamane"
SRC_REPO = "cnnclassifier"
AUTHOR_EMAIL="prathmbamne2002@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small package for CNN Classifier",
    long_description=long_description,
    url="https://github.com/prathmbamne2002/chicken_disease-cnnclassifier",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")

)