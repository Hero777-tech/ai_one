import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()
    
    
__version__ = "1.0.0"

REPO_NAME = "ai_one"
AUTHOR_USER_NAME = "Aditto"
SRC_REPO = "cnn_Clissifier"
AUTHOR_EMAIL = "pro.codenow@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for CNN app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/Hero777-tech/ai_one",
    project_urls={
        "Bug Tracker": f"https://github.com/Hero777-tech/ai_one/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)
