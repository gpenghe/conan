# Allow conans to import ConanFile from here
# to allow refactors
from conans.model.conan_file import ConanFile
from conans.model.options import Options
from conans.model.settings import Settings
from conans.client.cmake import CMake
from conans.client.gcc import GCC

__version__ = '0.4.0'