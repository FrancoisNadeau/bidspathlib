
"""
BIDS documentation and variable names in a dict.

"""
import json
import os
import sys
from pathlib import Path
from typing import Dict, List, Text, Tuple, Union

__path__: List = [join(sys.path[0], '__init__.py')]
URL: Text = 'https://github.com/FrancoisNadeau/bidspathlib/tree/main/json_docs'
DOCS_PATH = Path(os.path.join(__path__[0], 'json_docs'))

def _load_json(src: Union[Text, os.PathLike]) -> Dict:
    return json.loads(Path(src).read_text())

DATATYPES_PATH, MODALITIES_PATH, DEPR_S_PATH, E_DESC_PATH,\
N_DESC_PATH, FP_STRINGS_PATH, BASE_DATA_PATH, LCS_PARAMS_PATH = \
    sorted(DOCS_PATH.iterdir())

base_data_strings: Dict = json.loads(BASE_DATA_PATH.read_text())

ENTITY_FIELDS, DATATYPE_STRINGS, ENTITIES_ORDER, ENTITY_STRINGS, \
NIFTI_EXTENSIONS, SUFFIX_STRINGS, SPECIFIC_DATATYPE_FIELDS,\
BIDS_RECOMMENDED, NO_EXTENSION_FILES, NON_ENTITY_COMPONENTS = \
    tuple(base_data_strings.values())

COMPONENTS_NAMES: Tuple = ENTITY_STRINGS+NON_ENTITY_COMPONENTS
ENTITY_COLLECTOR_SLOTS: Tuple = tuple(set(ENTITIES_ORDER + COMPONENTS_NAMES))

MODALITIES: Dict = json.loads(MODALITIES_PATH.read_text())
ENTITY_DESC: Dict = json.loads(E_DESC_PATH.read_text())
NON_ENTITY_DESC: Dict = json.loads(N_DESC_PATH.read_text())
LCS_PARAMS: Dict = json.loads(LCS_PARAMS_PATH.read_text())
FP_STRINGS: Dict = json.loads(FP_STRINGS_PATH.read_text())
DEPRECATED_BIDS_SUFFIXES: Dict = json.loads(DEPR_S_PATH.read_text())
DATATYPES_DESCRIPTION: Dict = json.loads(DATATYPES_PATH.read_text())
ENTITY_STRINGS_DESC: Dict = dict(zip(ENTITY_STRINGS, ENTITY_DESC.values()))
COMPONENTS_DESC: Dict = {**ENTITY_STRINGS_DESC, **NON_ENTITY_DESC}

__tuples__: Tuple = (
    DATATYPE_STRINGS, ENTITIES_ORDER, ENTITY_STRINGS,
    NIFTI_EXTENSIONS, SUFFIX_STRINGS, SPECIFIC_DATATYPE_FIELDS,
    BIDS_RECOMMENDED, NO_EXTENSION_FILES, NON_ENTITY_COMPONENTS,
    COMPONENTS_NAMES, ENTITY_COLLECTOR_SLOTS
)
__dicts__: Tuple = (
    MODALITIES, DEPRECATED_BIDS_SUFFIXES,
    DATATYPES_DESCRIPTION, FP_STRINGS,
    LCS_PARAMS, ENTITY_STRINGS_DESC, COMPONENTS_DESC
)

__all__: List = [
    "ENTITY_FIELDS", "DATATYPE_STRINGS", "ENTITIES_ORDER",
    "ENTITY_STRINGS", "NIFTI_EXTENSIONS", "SUFFIX_STRINGS",
    "SPECIFIC_DATATYPE_FIELDS", "BIDS_RECOMMENDED",
    "NO_EXTENSION_FILES", "NON_ENTITY_COMPONENTS",
    "COMPONENTS_NAMES", "ENTITY_COLLECTOR_SLOTS",
    "MODALITIES", "ENTITY_DESC", "NON_ENTITY_DESC",
    "LCS_PARAMS", "FP_STRINGS", "DEPRECATED_BIDS_SUFFIXES",
    "DATATYPES_DESCRIPTION", "ENTITY_STRINGS_DESC", "COMPONENTS_DESC",
    "__tuples__", "__dicts__"
]
