import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="newrelic_deploy",
    version="0.0.3",
    author="Aurelio Saraiva",
    author_email="aurelio.saraiva@creditas.com.br",
    description="NewRelic deployment notify",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/creditas/newrelic-deploy",
    packages=setuptools.find_packages(),
    entry_points={"console_scripts": ["newrelic-deploy=newrelic_deploy:main"]},
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    install_requires=[
        'requests'
    ]
)
