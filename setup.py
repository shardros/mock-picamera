from distutils.core import setup
setup(
  name = 'mock-picamera',
  packages = ['mock-picamera'],
  version = '0.1',
  license='MIT',
  description = 'A pi camera module which does nothing and so does not require a physical picamera',
  author = 'Edwin Shepherd',
  url = 'https://github.com/shardros/mock-picamera',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/shardros/mock-picamera/archive/v_01.tar.gz',
  keywords = ['RaspberryPi', 'Camera',],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
)