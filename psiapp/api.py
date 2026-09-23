from .experiment import load_experiments, Experiment, FrozenExperiment
from .process_manager import ProcessManager
# Also importable as `psiapp.util.set_app_id`, which is what a launcher's
# `main` should use: it has to run before the GUI is built, and `psiapp.util`
# (unlike this module) needs neither the enaml import hook nor psi.
from .util import set_app_id

import enaml
with enaml.imports():
    from .widgets import AddItem, AddRemoveCombo, ExperimentSequence
