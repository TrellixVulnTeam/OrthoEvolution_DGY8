from OrthoEvol.Manager.management import ProjectManagement
from OrthoEvol.Manager.database_dispatcher import DatabaseDispatcher
from OrthoEvol.Manager.config import yml
from pkg_resources import resource_filename
from pathlib import Path
import yaml

# Set up project management
pm_config_file = resource_filename(yml.__name__, "initialize_new.yml")
with open(pm_config_file, 'r') as f:
    pm_config = yaml.load(f, Loader=yaml.FullLoader)
pm = ProjectManagement(**pm_config["Management_config"])

# Set up database management
db_config_file = resource_filename(yml.__name__, "databases.yml")
with open(db_config_file, 'r') as f:
    db_config = yaml.load(f, Loader=yaml.FullLoader)
db_config.update(pm_config)

# Generate main config file for this job
config_file = pm.user_log / Path("upload_config.yml")
with open(str(config_file), 'w') as cf:
    yaml.dump(db_config, cf, default_flow_style=False)

# Set up database dispatcher and dispatch the functions
dd = DatabaseDispatcher(config_file, pm)
dd.dispatch(dd.strategies, dd.dispatcher, dd.configuration)
