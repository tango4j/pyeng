#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test script to verify the GUI fix
"""

from module import ThisStudy

def test_lin_reg_out():
    """Test that lin_reg_out returns a scalar value"""
    study = ThisStudy()
    
    # Test with different sentence lengths
    test_lengths = [10, 20, 50, 100]
    
    print("Testing lin_reg_out function:")
    print("-" * 40)
    
    for length in test_lengths:
        result = study.lin_reg_out(length)
        print(f"Sentence length: {length}")
        print(f"Result: {result} (type: {type(result)})")
        print(f"Is scalar: {isinstance(result, (int, float))}")
        print()
    
    print("✅ Test completed!")

if __name__ == "__main__":
    test_lin_reg_out() 