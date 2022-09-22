Installation
============

The pyECSS can be installed via the standard mechanisms for Python packages, and is available through PyPI for standalone use, 
or Github, for development. We strongly propose to **install and use** pyECSS within a new environment created via ``conda``.


Creating a Conda Environment
------------------------------
After downloading the proper 
`Anaconda python distribution <https://www.anaconda.com/distribution/#download-section>`_, 
based on your system you may create a virtual environment via the ``conda`` command.

Typically, you may create a new envirnment via the command::

    conda create -n myenv python==3.9

This creates a new environment, named myenv, with a python version 3.9, which is the proper version to run pyECSS.

You may now activate the environment by running::

    conda activate myenv

When finished, you may deactivate it by running::

    conda deactivate



Stable Version - Standalone Use
--------------------------------
For standalone use, you may install pyECSS, via ``pip3`` ::

    pip3 install pyECSS

.. note ::

    The version installed via pip3 may be a few versions behind the current version in development. 
    If you need to test the latest version, you should install it via ``git`` and local install.

Latest Version - Standalone Use
----------------------------------

If you want the latest (development) version of ``pyECSS`` you can locally pip install it from the latest master with::

    pip3 install git+https://github.com/papagiannakis/pyECSS.git@develop

Latest Version - For development
-----------------------------------

If you want to modify ``pyECSS`` itself, then you should use an editable (``-e``) installation::

    git clone https://github.com/papagiannakis/pyECSS.git@develop
    pip3 install -e ./clifford

The proper way to contribute is to fork the `develop branch <https://github.com/papagiannakis/pyECSS.git@develop>`_ , 
clone it to your computer and run::

    pip3 install -e .

at the directory where the `setup.py` file is located. 
You should then work on a feature branch and open a pull request, when you see fit. 
