from .experiment import Experiment, FrozenExperiment

import enaml
with enaml.imports():
    from .widgets import AddRemoveCombo, ExperimentSequence
