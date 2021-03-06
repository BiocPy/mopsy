import numpy as np
import scipy.sparse as sp
from .nops import Nops
from .sops import Sops

from typing import Union

__author__ = "jkanche"
__copyright__ = "jkanche"
__license__ = "MIT"


def get_matrix_type(
    mat: Union[np.ndarray, sp.spmatrix], non_zero: bool = False
):
    """Get an internal matrix state

    Args:
        mat (Numpy.ndarray or scipy.sparse.spmatrix): a numpy or scipy matrix
        non_zero (bool): filter zero values ?

    Raises:
        Exception: TypeNotSupported, when the matrix type is not supported

    Returns:
        an internal matrix representation object
    """
    if isinstance(mat, np.ndarray):
        return Nops(mat, non_zero=non_zero)

    if isinstance(mat, sp.spmatrix):
        return Sops(mat, non_zero=non_zero)

    # TODO: zarr, xarray, idk what else, pandas df/sparsedf ?

    print(f"{type(mat)} is not supported")
    raise Exception("TypeNotSupported")
