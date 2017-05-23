"""Phylogenetic tools part of the Orthologs Package"""

import warnings
from Orthologs import OrthologsWarning
from Bio import AlignIO

# Ignore the warning in this init script.
warnings.simplefilter('ignore', OrthologsWarning)

# Initialize the modules
from Orthologs.Phylogenetics.PAML import ETE3PAML, PamlTest
from Orthologs.Phylogenetics.PhyML import PhyML
from Orthologs.Phylogenetics.Phylip import Phylip
from Orthologs.Phylogenetics.PhyloTree import TreeViz

# Add a new module
class RelaxPhylip(object):
    """Convert the a multiple sequence alignment file to
    relaxed-phylip format.
    """
    def __init__(inputfile, outputfile):
        """Fasta to Relaxed Phylip format."""
        AlignIO.convert(inputfile, "fasta",
                        outputfile, "phylip-relaxed")

# Make this explicit, then they show up in the API docs
__all__ = ("ETE3PAML",
           "PamlTest",
           "PhyML",
           "TreeViz",
           "Phylip",
           "RelaxPhylip",
)
