# EPA1361_Model-based_Decision-making
Repository for the course EPA1361 Model-based Descision Making
<h1> Group 02 - Actor: Analysts for the province of Overijsel </h1>
Jasper Baars - 4884280 <br>
Berend Nieuwschepen - 4966104 <br>
Sabine Verbunt - 5637953 <br>
Vince Meier - 4955277 <br>
Lennard Steketee - 4707850 <br>
Jari van der Broek - 4932749 <br>

## How-To

### Main Results

The main results obtained from this analysis can be found in several Jupyter Notebooks in the `model` folder:

1. `2a. Open Exploration.ipynb`: This notebook performs the open exploration and provides the analysis of the model
2. `2b. MOEA.ipynb`: This notebook shows the results of a multi-objective evolutionary algorithm run tailored towards the dike rings associated with Overijsel.
3. `3. Uncertainty Analysis.ipynb`: This notebook shows the results of the uncertainty analysis and tests the pareto policies against different scenarios to determine the robustness.
4. `4. Scenario Discovery.ipynb`: determines the best policies and makes various visualisations.

### Directory structure

```
---\
    Model and Notebooks\
    ------ *Model files, forked from quaquel/epa1361_open*
    ----- 2a. Open Exploration.ipynb
    ----- 2b. MOEA.ipynb
    ----- 3. Uncertainty Analysis.ipynb
    ----- 4. Scenario Discovery.ipynb

    generated_datasets\
    ------ *Modeling outputs to reproduce results*

    Visualisations\
    ------ *Figures saved from the notebooks*
```

To reproduce our results, please install the following packages (these can also be found in the requirements.txt):

ema_workbench <br>
networkx<br>
xlrd<br>
openpyxl<br>
networkx<br>
ipyparalel<br>
scipy<br>
seaborn<br>
matplotlib.pyplot

