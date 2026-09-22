'''
Small helpers for experiment launchers.

Deliberately free of psi, enaml and atom imports so that it can be used from
the very top of a launcher's `main`, before the GUI machinery is loaded, and
imported without the enaml import hook being active (unlike `psiapp.api`,
which pulls in .enaml modules).
'''
import logging
log = logging.getLogger(__name__)

import os


def set_app_id(app_id):
    '''
    Give this process its own identity on the Windows taskbar.

    Windows groups taskbar buttons by AppUserModelID, and a Python GUI that
    never sets one inherits the interpreter's. Without this every psi program
    shares a single taskbar button showing Python's icon (or the console-script
    wrapper's), no matter what icon its windows carry.

    `psi.application.set_app_id` is a deliberate copy of this, used by `psi`
    itself to claim `psi.psi`. psi cannot import psiapp -- psiapp is built on
    psi, not the other way around -- so the two are kept in sync by hand.

    Parameters
    ----------
    app_id : string
        Dotted identifier, by convention `psi.<program>` (e.g., `psi.cftscal`,
        `psi.noise-exp`). Launchers give themselves an ID distinct from the
        `psi.psi` claimed by the experiments they spawn, so that a launcher and
        the experiments running under it get separate taskbar buttons.

    Notes
    -----
    Call this from the program's entry point before the Qt application is
    created. Once a window exists Windows has already bound the process to the
    default ID and this has no effect.

    No-op off Windows, and fails soft: a mis-grouped taskbar button is cosmetic
    and shouldn't keep the program from starting.
    '''
    if os.name != 'nt':
        return
    import ctypes
    try:
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(app_id)
    except Exception:
        log.warning('Unable to set the AppUserModelID to %r', app_id,
                    exc_info=True)
