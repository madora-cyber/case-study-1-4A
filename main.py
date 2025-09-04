import subprocess

def run_program(input_data=""):
    """Helper to run student's main.py and capture output"""
    result = subprocess.run(
        ["python3", "main.py"],
        input=input_data.encode(),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        timeout=5
    )
    return result.stdout.decode().strip()

def test_fibonacci():
    # Runs main.py and checks Fibonacci sequence
    output = run_program()
    assert "0 1 1 2 3 5 8 13 21 34" in output

def test_password():
    # Simulates entering wrong password first, then correct one
    output = run_program("wrong\nsecret123\n")
    assert "Access granted" in output

def test_pattern():
    # Runs main.py and checks nested loop pattern
    output = run_program()
    assert "1\n12\n123\n1234" in output

