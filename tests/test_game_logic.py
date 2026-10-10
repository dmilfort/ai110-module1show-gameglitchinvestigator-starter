from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 10 and guess is 10, it should be a win
    result = check_guess(10, 10)
    assert result[0] == "Win"

def test_guess_too_high():
    # If secret is 15 and guess is 10, hint should be "Too High"
    result = check_guess(15, 10)
    assert result[0] == "Too High"

def test_guess_too_low():
    # If secret is 5 and guess is 10, hint should be "Too Low"
    result = check_guess(5, 10)
    assert result[0] == "Too Low"
