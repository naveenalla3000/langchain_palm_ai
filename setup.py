from setuptools import find_packages, setup

setup(
    name='langchainplamai',
    version='0.0.1',
    author='Naveen alla',
    author_email='naveenalla3000@gmail.com',
    install_requires=[
        "langchain_google_genai",
        "chainlit",
        "python-dotenv",
        "chainlit",
    ],
    packages=find_packages(),
)