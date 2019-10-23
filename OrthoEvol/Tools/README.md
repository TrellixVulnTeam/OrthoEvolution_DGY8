# Tools Documentation
The Tools module is a collection of often used classes or functions that either
enhance our other modules and create reusable functions to be used in various
modules.

We've incorporated tools for sge tools for use with pbs, a pandoc
script and class for converting docx files to markdown formats, multiprocessing
in multiprocess, and a ftp module that aids in downloading files from NCBI's
ftp repository.


## Examples
Take a look at the examples below to get an idea of how to incorporate these
tools in your project and how we use these tools in our project.

### Download NCBI databases with our NCBI FTP Client
``` python
from OrthoEvol.Tools.ftp import NcbiFTPClient

ncbiftp = NcbiFTPClient(email='somebody@gmail.com')
ncbiftp.getblastdb(database_name='refseq_rna')
```

### List all subdirectories in a NCBI FTP Path
```python

ncbiftp.listdirectories(path='/blast/db/')
Out[54]: ['FASTA', 'cloud']
```

### Utilize multiprocessing to speed up your code
```python
from OrthoEvol.Tools.parallel import Multiprocess


def printwords(word):
    print(word)


words = ['bae', 'luh', 'cuh']

if __name__ == '__main__':
    mp = Multiprocess()
    mp.map2function(printwords, words)
```

### Integrate logging in a simple and quick way
```python
from OrthoEvol.Tools.logit import LogIt

# Set up your loggers
logit = LogIt()default(logname='test1 log', logfile='log.txt')

# Shutdown logging without deleting the logfile
logit.shutdown()
```
### Send a message to a slack channel
Your config file should look as such:
```python
[APIKEYS]
slack = apikeystring
```

```python
from OrthoEvol.Tools.slackify import Slackify

slack = Slackify(slackconfig='path/to/slackconfig.cfg')
message_to_channel = 'Hey, <@username>. This is an update for the current script.'

slack.send_msg(channel='channelname', message=message_to_channel)
```

### Importing all tools modules
```python
from OrthoEvol.Tools.ftp import BaseFTPClient, NcbiFTPClient
from OrthoEvol.Tools.logit import LogIt
from OrthoEvol.Tools.mygene import MyGene
from OrthoEvol.Tools.parallel import Multiprocess
# from OrthoEvol.Tools.pandoc import PandocConverter
from OrthoEvol.Tools.send2server import S2S
from OrthoEvol.Tools.sge import (BaseSGEJob, SGEJob, Qstat, SGEPipelineTask,
                                 randomid, basejobids, import_temp,
                                 writecodefile,
                                 file2str)
from OrthoEvol.Tools.slackify import Slackify
```


## Additional Documentation

Check the specific modules for more detailed readmes and examples of using the
tools with this package.