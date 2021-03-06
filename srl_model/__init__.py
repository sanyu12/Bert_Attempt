# pylint: disable=wrong-import-position

# Make sure that allennlp is running in Python 3.6
import sys
if sys.version_info < (3, 6):
    raise RuntimeError("AllenNLP requires Python 3.6 or later")

# We get a lot of these spurious warnings,
# see https://github.com/ContinuumIO/anaconda-issues/issues/6678
import warnings
warnings.filterwarnings("ignore", message="numpy.dtype size changed")
warnings.filterwarnings("ignore", message="numpy.ufunc size changed")

try:
    # On some systems this prevents the dreaded
    # ImportError: dlopen: cannot load any more object with static TLS
    import spacy, torch, numpy  # pylint: disable=multiple-imports

except ModuleNotFoundError:
    print("Using AllenNLP requires the python packages Spacy, "
          "Pytorch and Numpy to be installed. Please see "
          "https://github.com/allenai/allennlp for installation instructions.")
    raise

from srl_model.version import VERSION as __version__
