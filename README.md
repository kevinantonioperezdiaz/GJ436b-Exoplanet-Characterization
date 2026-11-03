# Photometric & Radial Velocity Characterization of Exoplanet GJ 436b

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Astrophysics](https://img.shields.io/badge/Domain-Observational%20Astrophysics-orange.svg)](#)

A scientific computing pipeline for the multi-technique characterization of the extrasolar planet **GJ 436b**. This project combines space-based transit photometry from the **Spitzer Space Telescope** (8 $\mu\text{m}$) and high-precision radial velocity (RV) time-series from the **HIRES spectrometer at Keck Observatory** to constrain the planet's orbital dynamics, physical parameters, bulk composition, and planetary classification.

---

## Scientific Overview

GJ 436 is an M2.5 V red dwarf located approximately 10.2 pc away. Its close-in companion, **GJ 436b**, is a benchmark "warm Neptune" that exhibits a significant orbital eccentricity despite its short period ($P \approx 2.644$ days). 

This pipeline models both observational datasets to derive:
- **Transit Photometry:** Planet-to-star radius ratio ($R_p / R_*$), orbital inclination ($i$), scaled semi-major axis ($a / R_*$), transit depth ($\delta$), and transit duration ($T_{14}$).
- **Radial Velocities:** Keplerian orbital solution, radial velocity semi-amplitude ($K$), orbital eccentricity ($e$), argument of periastron ($\omega$), system systemic velocity ($\gamma$), and planetary minimum mass ($M_p \sin i$).
- **Planetary Structure & Environment:** Physical planetary radius ($R_p$), dynamical mass ($M_p$), bulk density ($\rho_p$), surface gravity ($\log g_p$), equilibrium temperature ($T_{eq}$), and circumstellar habitable zone (HZ) boundaries.

---

## Methodology & Pipeline Architecture

The end-to-end processing pipeline executes in three stages:

1. **Light Curve Modeling:** Applies analytic transit models with limb-darkening coefficients to determine photometric parameters from normalized Spitzer flux measurements.
2. **Keplerian Orbital Fitting:** Numerically solves Kepler's equation across phase-folded radial velocity epochs to constrain orbital eccentricity and minimize line-of-sight velocity residuals.
3. **Physical Parameter Synthesis:** Propagates host star parameters ($M_* = 0.445\,M_\odot$, $R_* = 0.437\,R_\odot$, $T_{\text{eff}} = 3416\,\text{K}$) through photometric and spectroscopic posteriors to compute absolute mass, radius, mean bulk density, and insolation environment.

---

## Key Results & Figures

### 1. Primary Transit Light Curve (Spitzer Space Telescope)
Normalized 8 $\mu\text{m}$ light curve centered at mid-transit, demonstrating transit depth and ingress/egress profile.

<p align="center">
  <img src="figures/TRANSITO.png" alt="Transit Light Curve" width="650"/>
</p>

### 2. Radial Velocity Curve & Phase Fold
Unfolded time-series and phase-folded Keplerian orbit illustrating the eccentric line-of-sight wobble induced by GJ 436b.

| Time Series RV | Phase-Folded Keplerian Orbit |
| :---: | :---: |
| <img src="figures/velocidad%20radial.png" alt="RV Time Series" width="400"/> | <img src="figures/velocidad%20radial%20respecto%20a%20la%20fase.png" alt="RV Phase Folded" width="400"/> |

### 3. Planetary Classification & Insolation Environment
Mass-radius regime placing GJ 436b among transition planets (warm Neptunes) and circumstellar radiative equilibrium relative to the host star's habitable zone.

| Mass-Radius Classification | Habitable Zone & Orbital Position |
| :---: | :---: |
| <img src="figures/Tipo%20Planetario.png" alt="Planetary Classification" width="400"/> | <img src="figures/Zona%20de%20Habitabilidad.png" alt="Habitable Zone" width="400"/> |

---

## Derived Parameters Summary

| Parameter | Symbol | Derived Value | Units |
| :--- | :---: | :---: | :---: |
| Orbital Period | P | 2.643898 | days |
| Planet-to-Star Radius Ratio | R_p / R_* | 0.0834 ± 0.0012 | — |
| Orbital Inclination | i | 86.3 ± 0.8 | deg |
| RV Semi-Amplitude | K | 17.6 ± 0.5 | m/s |
| Orbital Eccentricity | e | 0.15 ± 0.02 | — |
| Planetary Mass | M_p | 22.1 ± 1.4 | M_Earth |
| Planetary Radius | R_p | 4.18 ± 0.16 | R_Earth |
| Mean Bulk Density | rho_p | 1.68 ± 0.22 | g/cm^3 |
| Equilibrium Temperature (A_B = 0.3) | T_eq | 660 ± 20 | K |

*Bulk density and mass-radius relation confirm an internal structure dominated by a rock-ice core enveloped in an extended H/He gaseous envelope.*

---

## Repository Structure

- **`data/`**: Space-based transit photometry from Spitzer (8 $\mu\text{m}$) and high-precision radial velocity datasets from Keck/HIRES.
- **`figures/`**: Generated scientific figures (light curves, phase-folded orbits, mass-radius diagrams, habitable zone boundaries).
- **`exoplanet_analysis.py`**: Core Python pipeline executing Keplerian orbit solutions, transit extraction, and parameter synthesis.
- **`requirements.txt`**: Scientific dependencies (`numpy`, `scipy`, `matplotlib`).

---

## Installation & Usage

Clone the repository and install dependencies:

bash
git clone [https://github.com/kevinantonioperezdiaz/GJ436b-Exoplanet-Characterization.git](https://github.com/kevinantonioperezdiaz/GJ436b-Exoplanet-Characterization.git)
cd GJ436b-Exoplanet-Characterization
pip install -r requirements.txt

Ejecución del análisis completo:

python exoplanet_analysis.py  

---

## References

1. Gillon, M., et al. (2007). *Detection of transits of the nearby hot Neptune GJ 436b*. Astronomy & Astrophysics, 472(2), L13-L16.
2. Butler, R. P., et al. (2004). *A Neptune-Mass Planet Orbiting the Nearby M Dwarf GJ 436*. The Astrophysical Journal, 617(1), 580.
3. Deming, D., et al. (2007). *Spitzer Transit and Secondary Eclipse Photometry of GJ 436b*. The Astrophysical Journal, 667(2), L199.

```
