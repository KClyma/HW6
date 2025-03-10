"""
test_rankine.py

This script tests two different Rankine power cycles:

1. **Saturated Vapor at Turbine Inlet**:
   - High Pressure: 8000 kPa
   - Low Pressure: 8 kPa
   - Quality at Inlet: x = 1 (Saturated vapor entering turbine)

2. **Superheated Steam at Turbine Inlet**:
   - Same as Case 1, except:
   - Temperature at Inlet: T1 = 1.7 * Tsat (Superheated steam into turbine)

The script imports from `rankine.py`, instantiates the Rankine cycle objects,
calculates cycle efficiencies, and prints a report for each cycle.

Thermodynamic properties are determined using `scipy.interpolate.griddata`.
Results can be verified using PyXSteam.
"""

from Rankine_stem import rankine


def main():
    # Case 1: Saturated vapor entering the turbine
    cycle1 = rankine(p_high=8000, p_low=8, name='Rankine Cycle - Saturated Vapor')
    cycle1.calc_efficiency()
    cycle1.print_summary()



    # Case 2: Superheated steam entering the turbine
    # First, determine the saturation temperature at p_high
    T_sat = cycle1.state1.T  # Assuming state1 in cycle1 correctly found Tsat
    T_superheat = 1.7 * T_sat  # Superheated temperature

    cycle2 = rankine(p_high=8000, p_low=8, t_high=T_superheat, name='Rankine Cycle - Superheated Steam')
    cycle2.calc_efficiency()
    cycle2.print_summary()


if __name__ == "__main__":
    main()
