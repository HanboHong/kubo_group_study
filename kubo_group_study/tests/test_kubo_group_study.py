"""
Unit and regression test for the kubo_group_study package.
"""

# Import package, test suite, and other packages as needed
import kubo_group_study as trial
import pytest
import sys
import numpy as np
import scipy.fftpack as fourier_transform



def test_kubo_group_study_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "kubo_group_study" in sys.modules



def test_ct():
    """Test if Ct calculation work"""
    sample_time = np.loadtxt('ref.txt', usecols=[0])
    reference_ct = np.loadtxt('ref.txt', usecols=[1])
    
    instance = trial.kubo_group_study.Kubo(delta=1 , tau=1)

    calculate_ct = instance.calculate_Ct(time=sample_time)[:,1]

    assert np.allclose(calculate_ct , reference_ct)
