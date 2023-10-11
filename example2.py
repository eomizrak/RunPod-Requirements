from fexbind.train.hyp_search import hyperparameter_search
from fexbind.train.train import training
from fexbind.utils.config import sweep_configuration



#training(config = None, conv = 'GCN', device = 'cuda:0')
run = hyperparameter_search(config = sweep_configuration, 
                            device = 'cuda:0', wand_dir = 'cache/', 
                            project = 'MM_Smiles_runp', count=200000)

run.run_sweep()
