import setuptools

setuptools.setup (
  include_package_data = True,
  name = 'testoutput1205',
  version = '0.0.1',
  description = 'oss-dev my testoutput1205',
  author = 'minhe8564',
  author_email = 'minhe8564@gmail.com',
  url = "https://github.com/minhe8564/testoutput",
  download_url = "https://github.com/minhe8564/testoutput/releases/tag/v0.0.1.zip",
  install_requires=[ 'pytest' ],
  long_description = 'oss-dev python module',
  long_description_content_type = 'text/markdown',
  classifiers = [
    "Programming Language :: Python :: 3",
    "Operationg System :: OS Independent",
  ],
)
