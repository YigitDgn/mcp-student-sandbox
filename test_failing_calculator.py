import pytest
from failing_calculator import average_ratios

def test_average_ratios_normal():
    """Test with normal positive numbers"""
    result = average_ratios([10, 5, 2])
    assert result == pytest.approx(26.667, 0.01)


def test_average_ratios_with_zero():
    """Test that function crashes on zero division"""
    with pytest.raises(ZeroDivisionError):
        average_ratios([10, 5, 0])


def test_average_ratios_single_number():
    """Test with single number"""
    result = average_ratios([10])
    assert result == pytest.approx(10.0)


def test_average_ratios_large_numbers():
    """Test with larger numbers"""
    result = average_ratios([100, 50, 25])
    assert result == pytest.approx(2.333, 0.01)


def test_average_ratios_negative_numbers():
    """Test with negative numbers"""
    result = average_ratios([-10, -5])
    assert result == pytest.approx(-15.0)


def test_average_ratios_empty():
    """Test with empty list"""
    with pytest.raises(ValueError):
        average_ratios([])