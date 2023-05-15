
# bassmodel

The bassmodel package is a Python package that provides functions for fitting and predicting using the Bass diffusion model.

## Functions



'diffusion(sales)'
This function calculates the cumulative diffusion curve for a given set of data's slaes column.

'adoption_rate(t, p, q, m, N)'
This function calculates the adoption rate for a given set of parameters and time.

'bass_f(t, p, q)'
This function calculates the Bass diffusion curve for a given set of parameters and time.

'bass_F(t, p, q)'
This function calculates the cumulative Bass diffusion curve for a given set of parameters and time.

'predict_bass_model(params, m)'
This function predicts the diffusion of a new product using the parameters p and q and the total market potential m.

'plot_bass(p, q, title)'
This function plots the Bass diffusion curve for a given set of parameters.

## Installation

To install the bassmodel package, you can use pip:

```
pip install bassmodel
```
## Usage

To use the bassmodel package, first import it:
```
import bassmodel
```

calculate the parameters 

```
diffusion(sales)
```

plot the Bass diffusion curve:
```
bassmodel.plot_bass(params['p'], params['q'], 'Bass diffusion curve')
```
