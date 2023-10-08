import setuptools

with open("README.md","r",encoding = "utf-8") as f:
    long_desription = f.read()

__version__ = "0.0.0"

REPO_NAME = "Kidney_Disease_Classificaton_DL_Project"
AUTHOR_USER_NAME = "swetanshu-ds"
SRC_REPO = "cnnClassifier"
AUTHOR_EMAIL = "swetanshupandey1722@gmail.com"

setuptools.setup(
    name = SRC_REPO,
    version = __version__,
    author = AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for CNN app",
    long_description= long_desription,
    long_desription_content = "text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)