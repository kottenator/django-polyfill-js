from setuptools import setup, find_packages


setup(
    name='django-polyfill-js',
    version='0.0.1a1',
    description='JS (ES2015+) polyfills',
    long_description='JS polyfills for your user-agent.',
    url='https://github.com/kottenator/django-polyfill-js',
    author='Rostyslav Bryzgunov',
    author_email='kottenator@gmail.com',
    license='MIT',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    extras_require={
        'test': [
            'django~=1.11',
            'pytest~=3.0',
            'pytest-django~=3.0',
            'pytest-cov~=2.4',
            'pytest-pythonpath~=0.7'
        ]
    },
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3'
    ]
)
