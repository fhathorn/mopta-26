"""
This module demonstrates how to initialize and access an AIMMS project using the Python API.

Overview:
---------
1. Import required AIMMS API classes and enums.
2. Optionally import type hints for static analysis.
3. Create a singleton AIMMS Project instance, exposing all identifiers for easy access.
4. Retrieve the AIMMS Model object from the project, which provides access to model data and procedures.

Details:
--------
- The `Project` class represents an AIMMS project and manages the connection to the AIMMS engine.
- The `exposed_identifier_set_name` argument controls which identifiers (parameters, variables, sets, etc.) are accessible from Python. Here, we expose all identifiers for convenience.
- The `get_model` method loads the model definition from the specified stub file (here, "model_stub.py"). This allows you to interact with the model's data and procedures from Python.

Usage:
------
After importing this module, you can use `project` to access the AIMMS project and `my_aimms` to interact with the model. For example, you can read/write data, run procedures, and retrieve results.
"""

from aimmspy.project.project import Project, Model
from aimmspy.model.enums.data_return_types import DataReturnTypes

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from model_stub import Model

project: Project = Project(exposed_identifier_set_name="AllIdentifiers")

my_aimms: Model = project.get_model("model_stub.py")