from .linkedin import get_profile

def test_values():
    profile = get_profile("arnoinen")
    assert profile.get('firstName') == 'Arno'
    assert profile.get('lastName') == 'Inen'
    
def test_non_existing_name():
    profile = get_profile("gntrbgrtgyugotrgrtjgkrt")
    assert profile == {}