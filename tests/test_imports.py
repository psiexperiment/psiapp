import subprocess
import sys
import textwrap


def test_api_does_not_import_cftscal():
    # cftscal depends on psiapp, so psiapp importing cftscal would be a
    # cycle -- and would stop other launchers from using psiapp's widgets
    # without installing cftscal. Checked in a fresh interpreter so that
    # modules imported by other tests don't hide the problem. Imported the
    # way a launcher does, with the enaml import hook active, since psiapp.api
    # pulls in .enaml modules from psi.
    code = textwrap.dedent('''
        import sys
        import enaml
        with enaml.imports():
            import psiapp.api
        sys.exit(1 if 'cftscal' in sys.modules else 0)
    ''')
    result = subprocess.run([sys.executable, '-c', code], capture_output=True,
                            text=True)
    assert result.returncode == 0, result.stderr or 'psiapp.api imported cftscal'
