from setuptools import setup, find_packages

setup(
    name="ktml",
    version="1.0",
    packages=find_packages(),
    install_requires=['numpy', 'matplotlib', 'scikit-learn', 'pandas',
                      'pillow', 'cycler', 'imageio', 'joblib'],
    include_package_data=True,

    author="Andreas Bernhardt",
    author_email="bernhardtandreas",
    description=("karriere tutor - Machine Learning"),
    license="BSD",
    keywords="machine learning ml sklearn scikit learn",
    url="https://github.com/Jacoby7/ktml",
)
