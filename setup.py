from setuptools import setup, find_packages

setup(
    name='llm-real-estate-agent',
    version='0.1.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='A Python project that utilizes large language models and vector databases to generate personalized real estate narratives based on buyer preferences.',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'numpy',
        'pandas',
        'scikit-learn',
        'transformers',
        'torch',
        'faiss-cpu',  # or 'faiss-gpu' if using GPU
        'pytest',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)