from setuptools import setup, find_packages

setup(
    name='churn-prediction-app',
    version='3.10.0',
    author='Tinotenda Chagaka',
    description='Churn Prediction Web Application',
    packages=find_packages(),
    install_requires=[
        'streamlit',
        'numpy',
        'tensorflow',
    ],
)