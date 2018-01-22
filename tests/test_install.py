import spice_api as spice

def test_install():
    assert spice.user_agent == 'spice API (https://github.com/Utagai/spice)'
