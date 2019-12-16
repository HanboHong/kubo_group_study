"""
kubo_group_study
trial test for kubo cookiecutter
"""

# Add imports here
from .kubo_group_study import Kubo

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions
