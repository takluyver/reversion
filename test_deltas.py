from reversion.deltas import add, final

def test_add():
    assert add('4.0', '1') == '5.0'
    assert add('4.0', '.1') == '4.1'
    assert add('4.0.0beta1', '..0beta1') == '4.0.0beta2'
    assert add('4.3.2', '1') == '5.0.0'
    assert add('4.3.2', '0.1') == '4.4.0'

def test_final():
    assert final('4.0') == '4.0'
    assert final('4.0beta1') == '4.0'
    assert final('4.0.rc3') == '4.0'
