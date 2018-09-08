# LuKARS
The LuKARS model is a lumped karst hydrological model that was proposed to perform land use change impact 
studies in karstic environments (Bittner et al., 2018).

The following model functions are provided and should be applied in the presented order.

model_period.py:
Sets the period for the model run.

t_index.py:
Simulates snow melt based on a temperature time series (degree-day method). The required parameters are a melt 
factor and a temperature threshold. More information are provided in Martinec (1960).
Required input: model_period, temperature_ts, melt_factor, t_threshold

thornthwaite.py:
Evapotranspiration model based on monthly mean temperatures proposed by Thornthwaite (1948). The original model 
calculates monthly values for evapotranspiration. Here we split the monthly values to the number of days in a 
month and perform a linear interpolation to generate a daily time series of evapotranspiration.
Required input: model_period, temperature_ts

interception_losses.py:
Calculates the losses of interception in a beech forest according to the percentage losses proposed in DVWK (1996).
Required input: model_period

sink_n_source.py:
Calculates the sink and source term for each individual hydrotope. 
Required input: model_period, precipitation_ts (optional: et_model, snow_model, interception_losses, interception_threshold,
temperature_ts, t_threshold). Note that, if interception_losses and/or the snow_model are defined, the interception_threshold 
and the temperature_ts and t_threshold need to be defined as well.

model.py:
The model code of LuKARS as presented in Bittner et al. (2018).
Required input: sink_n_source_hyd_1, sink_n_source_hyd_2, sink_n_source_hyd_3, sink_n_source_hyd_4 and input_parameters.
Note that the current version of the model only allows to simulate 4 hydrotopes (as presented for the Kerschbaum spring in Waidhofen,
Austria, in Bittner et al. (2018)). An example application is given in model_kerschbaum.py. An example for the input parameters of
the model is given in kerschbaum_input.txt. The relevant time series for this model run are provided in kerschbaum_py.csv.


References:

Bittner, D., Sheikhy Narany, T., Kohl, B., Disse, M., Chiogna, G., 2018. Modeling the hydrological impact of land 
use change in a dolomite-dominated karst system. Journal of Hydrology (under review).

DVWK, 1996. DVWK-Merkblatt 238/1996. Ermittlung der Verdunstung von Land- und Wasserflächen, Bonn.

Martinec, J., 1960. The degree-day factor for snowmelt-runoff forecasting. IUGG General Assembly of Helsinki, 
IAHS Commission of Surface Waters (51), 468–477.

Thornthwaite, C.W., 1948. An Approach toward a Rational Classification of Climate. Geographical Review 38 (1), 55.
