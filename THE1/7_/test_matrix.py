import pytest
from matrix import Matrix

@pytest.fixture
def test_matrix_alpha() -> "Matrix":
    ''' generate a test matrix. '''
    return Matrix(u_left=1,
                  u_right=2,
                  l_left=3,
                  l_right=4)
    
@pytest.fixture
def test_matrix_beta() -> "Matrix":
    ''' generate a test matrix. '''
    return Matrix(u_left=0,
                  u_right=1,
                  l_left=-1,
                  l_right=0)
    
@pytest.mark.add
def test_add(test_matrix_alpha, test_matrix_beta) -> None:
    ''' test the add method of a matrix. '''
    assert (test_matrix_alpha.add(test_matrix_beta)).u_left==1
    
@pytest.mark.mult
def test_mult(test_matrix_alpha, test_matrix_beta) -> None:
    ''' test the mult method of a matrix. '''
    assert (test_matrix_beta.mult(test_matrix_beta).add(test_matrix_alpha)).u_left==0

@pytest.mark.to_str
def test_to_str(test_matrix_alpha) -> None:
    ''' test the __str__ method of a matrix. '''
    assert (test_matrix_alpha.__str__()) == f'|   {test_matrix_alpha.u_left}   {test_matrix_alpha.u_right}|\n|   {test_matrix_alpha.l_left}   {test_matrix_alpha.l_right}|\n'