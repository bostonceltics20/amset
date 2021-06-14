from setuptools import find_packages, setup

from amset import __version__

with open("README.md", "r") as file:
    long_description = file.read()

if __name__ == "__main__":
    setup(
        name="amset",
        version=__version__,
        description="AMSET is a tool to calculate carrier transport properties "
        "from ab initio calculation data",
        long_description=long_description,
        long_description_content_type="text/markdown",
        url="https://github.com/hackingmaterials/amset",
        author="Alex Ganose",
        author_email="aganose@lbl.gov",
        license="modified BSD",
        keywords="mobility conductivity seebeck scattering lifetime rates dft vasp",
        packages=find_packages(),
        package_data={
            "amset": [
                "defaults.yaml",
                "plot/amset_base.mplstyle",
                "plot/revtex.mplstyle",
            ]
        },
        data_files=["LICENSE"],
        zip_safe=False,
        install_requires=[
            "quadpy==0.16.7",
            "numpy==1.20.3",
            "pymatgen==2022.0.8",
            "scipy==1.6.3",
            "monty==2021.5.9",
            "matplotlib==3.4.2",
            "BoltzTraP2==20.7.1",
            "tqdm==4.61.0",
            "tabulate==0.8.9",
            "memory_profiler==0.58.0",
            "spglib==1.16.1",
            "click==8.0.1",
            "sumo==2.2.5",
            "h5py==3.2.1",
            "pyFFTW==0.12.0",
            "interpolation==2.2.1",
            "numba==0.53.1",
        ],
        extras_require={
            "docs": [
                "mkdocs==1.1.2",
                "mkdocs-material==7.1.8",
                "mkdocs-minify-plugin==0.4.0",
                "mkdocs-macros-plugin==0.5.5",
                "markdown-include==0.6.0",
                "markdown-katex==202105.1031",
            ],
            "tests": ["pytest==6.2.4", "pytest-cov==2.12.1"],
            "all-electron": ["pawpyseed==0.6.4"],
            "dev": [
                "coverage==5.5",
                "codacy-coverage==1.3.11",
                "pycodestyle==2.7.0",
                "mypy==0.902",
                "pydocstyle==6.1.1",
                "flake8==3.9.2",
                "pylint==2.8.3",
                "black==21.5b2",
                "pre-commit==2.13.0",
            ],
        },
        classifiers=[
            "Programming Language :: Python :: 3.6",
            "Development Status :: 4 - Beta",
            "Intended Audience :: Science/Research",
            "Intended Audience :: System Administrators",
            "Intended Audience :: Information Technology",
            "Operating System :: OS Independent",
            "Topic :: Other/Nonlisted Topic",
            "Topic :: Scientific/Engineering",
        ],
        tests_require=["pytest"],
        entry_points={
            "console_scripts": [
                "amset = amset.tools.cli:cli",
                "desym = amset.tools.desym:desym",
            ]
        },
    )
