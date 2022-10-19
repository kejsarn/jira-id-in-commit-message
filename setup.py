from setuptools import setup

setup(
    name='jira_id_in_commit_message',
    version='0.1.0',    
    description='A example Python package',
    url='https://github.com/shuds13/pyexample',
    author='No Noname',
    author_email='yes@no.com',
    license='BSD 2-clause',
    packages=['jira_id_in_commit_message'],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',  
        'Operating System :: POSIX :: Linux',        
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    entry_points = {
    'console_scripts' : ['jira-id-in-commit-message = jira_id_in_commit_message.jira_id_in_commit_message:main'],
    }
)
