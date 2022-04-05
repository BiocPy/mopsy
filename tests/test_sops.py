from mopsy.sops import Sops
from scipy.sparse import eye

__author__ = "jkanche"
__copyright__ = "jkanche"
__license__ = "MIT"

mat = eye(5)
group = ["col1", "col2", "col1", "col2", "col2"]


def test_init():
    tmat = Sops(mat)
    assert tmat is not None


def test_group_iter_rows():
    tmat = Sops(mat)

    groups = tmat.iter(group, axis=0)
    assert sum(1 for _ in groups) == 2


def test_group_iter_cols():
    tmat = Sops(mat)

    groups = tmat.iter(group, axis=1)
    assert sum(1 for _ in groups) == 2


def test_group_apply_rows():
    tmat = Sops(mat)
    rmat = tmat.apply(sum, group=group, axis=0)
    assert rmat.shape[0] == 2
    assert rmat.shape[1] == 5
    assert rmat[0, :].flatten().tolist() == [1.0, 0.0, 1.0, 0.0, 0.0]
    assert rmat[1, :].flatten().tolist() == [0.0, 1.0, 0.0, 1.0, 1.0]


def test_group_apply_cols():
    tmat = Sops(mat)
    rmat = tmat.apply(sum, group=group, axis=1)
    assert rmat.shape[0] == 5
    assert rmat.shape[1] == 2
    assert rmat[:, 0].flatten().tolist() == [1.0, 0.0, 1.0, 0.0, 0.0]
    assert rmat[:, 1].flatten().tolist() == [0.0, 1.0, 0.0, 1.0, 1.0]


def test_group_apply_row_None():
    tmat = Sops(mat)
    rmat = tmat.apply(sum, group=None, axis=0)
    assert rmat is not None
    assert rmat.shape[0] == 1
    assert rmat.shape[1] == 5
    assert rmat[
        :,
    ].flatten().tolist() == [1.0, 1.0, 1.0, 1.0, 1.0]


def test_group_apply_col_None():
    tmat = Sops(mat)
    rmat = tmat.apply(sum, group=None, axis=1)
    assert rmat is not None
    assert rmat.shape[0] == 5
    assert rmat.shape[1] == 1
    assert rmat[
        :,
    ].flatten().tolist() == [1.0, 1.0, 1.0, 1.0, 1.0]
