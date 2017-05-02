# -*- coding: utf-8 -*-
"""
File Name: OrthoTools.py
Description:

@author: Shaurita D. Hutchins
Date Created: Mon Apr  3 18:02:08 2017
Project Name: KARG Project
"""
# Modules used
import os
import pexpect
from Bio.Align.Applications import ClustalOmegaCommandline
from Bio import AlignIO
from Bio.Phylo.Applications import PhymlCommandline
import sys
from ete3 import EvolTree
import pandas as pd
import configparser
from slacker import Slacker

#------------------------------------------------------------------------------
# Create a variable for os.rename
rn = os.rename

#------------------------------------------------------------------------------
# Tool that uses the CLustalOmega Command line
def clustal_align(gene):
    """ This function aligns genes using parameters similar to the default
    parameters. These parameters include 2 additional iterations for the hmm."""
    # Run clustal omega using the edited file
    clustalo_cline = ClustalOmegaCommandline(infile="MASTER_" + gene + "_CDS1.ffn",
                                             outfile=gene + "_aligned_cds_nucl.fasta",
                                             seqtype="DNA", max_hmm_iterations=2,
                                             infmt="fasta", outfmt="fasta", iterations=3,
                                             verbose=True, threads=8,
                                             force=True,
                                             log=gene + "_alignment.log")
    stdout, stderr = clustalo_cline()
    clustalo_cline()
    print(stdout, stderr)
    return;

#------------------------------------------------------------------------------
# ETE3 Tools
def ete3paml(gene):
    # Import the newick tree
    tree = EvolTree("data/phyml-output/" + gene + "_PhyML/" + gene + "_tree.nw")

    # Import the alignment
    tree.link_to_alignment("data/clustal-output/" + gene + "_Aligned/" + gene + "_aligned_cds_nucl.fasta")

    tree.workdir = 'data/paml-output/'

    # Set the binpath of the codeml binary
    tree.execpath = '/work5/r2295/bin/software/PAML/paml48/'

    # Run the codeml model
    tree.run_model('M1.' + gene)

#------------------------------------------------------------------------------
# Phylip tools

def dnapars(gene):
    # Maximum Parsimony using Phylip executable, dnapars, within unix shell
    dnapars = pexpect.spawnu("dnapars infile")
    dnapars.sendline("Y\r")
    dnapars.waitnoecho()
    rn("outfile", gene + "_maxpars")
    rn("outtree", gene + "_maxparstree")

def dnaml(gene):
    """Maximum Likelihood using Phylip executable, dnaml, within a unix shell. """
    dnaml = pexpect.spawnu("dnaml infile")
    dnaml.sendline("Y\r")
    dnaml.waitnoecho()
    rn("outfile", gene + "_maxlike")
    rn("outtree", gene + "_maxliketree")

def dnadist(gene):
    dnadist = pexpect.spawnu("dnadist infile")
    dnadist.sendline("Y\r")
    dnadist.waitnoecho()
    rn("outfile", gene + "_dnadist")
#------------------------------------------------------------------------------
# PhyMl tools
def relaxphylip(gene):
    """Convert the file to relaxed-phylip format."""
    AlignIO.convert(gene + "_aligned_cds_nucl.fasta", "fasta",
                    gene + "_aligned.phy", "phylip-relaxed")

def runphyml(gene):
    # Run phyml to generate tree results
    # Use the phyml executable file
    phyml_exe = None

    # This is mainly intended for windows use or use with an executable file
    exe_name = "PhyML-3.1_win32.exe" if sys.platform == "win32" else "phyml"
    phyml_exe = exe_name

    # Create the command & run phyml
    # Input a phylip formatted alignment file and describe the datatype ('nt' or 'aa')
    run_phyml = PhymlCommandline(phyml_exe, input=gene + '_aligned.phy', datatype='nt')
    print(run_phyml)
    out_log, err_log = run_phyml()
#------------------------------------------------------------------------------
def SplitLists(listname, basefilename, n):
    # Split the list into chunks
    chunks = [listname[x:x+n] for x in range(0, len(listname), n)]
    list_group = []
    num_lists = len(chunks)

    # Name and save the lists
    for chunk, num in zip(chunks, range(0, num_lists)):
        l = pd.DataFrame(chunk)
        n = basefilename + '_list_' + str(num)
        l.to_csv(n + ".txt", index=False, header=None)
        list_group.append(n)
    return list_group

#------------------------------------------------------------------------------
# Slack Tools
config = configparser.ConfigParser()
config.read('bin/orthologs.ini')
apikey = config['APIKEYS']['slack']
slack = Slacker(apikey)

# Definition for uploading images
def upload_img(channel, imgfile):
    slack.files.upload(imgfile, channel=channel)

# Definition for uploading files
def upload_file(channel, file):
    slack.files.upload(file, channel=channel)

# Definition for posting messages
def message_slack(channel, message, username):
    slack.chat.post_message(channel, message, username, as_user = True)