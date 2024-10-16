import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "textsummarizer_project"
AUTHOR_USER_NAME = "sanaksh"
SRC_REPO = "textsummerizer"
AUTHOR_EMAIL = "sandranakshatra@#gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    AUTHOR_EMAIL=AUTHOR_EMAIL,
    description="A text summarization project using NLP techniques",
    long_description="long description",
    long_description_content="text/markdown",
    url="https://github.com/{AUTHOR_USER_NAME}/{SRC_REPO}",
    project_urls={"Bug Tracker": f"https://github.com/sanaksh/textsummarizer_project/issues",},
    package_dir={"": "src"},
    packages=setuptools.find_packages(where = "src"),
)