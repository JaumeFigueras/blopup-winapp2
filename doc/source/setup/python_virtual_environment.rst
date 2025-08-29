Python Virtual Environment
==========================

BLOPUP runs on a dedicated Python virtual environment that is required to ensure
that all librearies are isolated and do not cause conflicts with other existing
software. This virtual environment is needed to both users and developers.

Steps
-----

1. **Create virtual environment**

    This environment will be used in the project. If the IDE you are using does not provide
    automatic tools to create the virtual environment you can do it manually.

    .. code-block:: bash

      python3 -m venv .venv

    For **PyCharm**, go to:

    `File → Settings → Python → Interpreter` and create the isolated new virtual environment

2. **Install regular dependencies**

    When all is setup the dependencies can be installed with:

    .. code-block:: bash

      pip3 install -r requirements.txt

References
----------

- `Python Virtual Environments <https://docs.python.org/3/library/venv.html>`_
