import pytest
# import sys
import pdb
# sys.path.insert(0,'prettier_html_table')
from prettier_html_table import create_table

def test_data_is_scalar():
    with pytest.raises(Exception, match="data:.* must either be a list of lists or a pandas.DataFrame"):
        create_table(123)

def test_data_is_simple_list():
    with pytest.raises(Exception, match="data:.* must either be a list of lists or a pandas.DataFrame"):
        create_table([1,2,3])


