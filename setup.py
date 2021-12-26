import sys

try:
    from skbuild import setup
except ImportError:
    print('Please update pip, you need pip 10 or greater,\n'
          ' or you need to install the PEP 518 requirements in pyproject.toml yourself', file=sys.stderr)
    raise

setup(
    name="audio-plugin-test",
    version="0.0.1",
    description="Test VST effects in python",
    author='Dmitry Galchinsky',
    license="GPLv3",
    packages=['audio_plugin_test'],
    package_dir={'': 'source'},
    cmake_install_dir='source/audio_plugin_test'
)
