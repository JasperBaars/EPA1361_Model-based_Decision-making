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

The main results obtained from this analysis can be found in several Jupyter Notebooks in the [`Model and Notebooks`](Model%20and%20Notebooks) folder. The steps must be followed in the following order:

1. [`2a. Open Exploration.ipynb`](Model%20and%20Notebooks%2F2a.%20Open%20Exploration.ipynb): This notebook performs the open exploration and provides the analysis of the model
2. [`2b. MOEA.ipynb`](Model%20and%20Notebooks%2F2b.%20MOEA.ipynb): This notebook shows the results of a multi-objective evolutionary algorithm run tailored towards the dike rings associated with Overijsel.
3. [`3. Uncertainty Analysis.ipynb`](Model%20and%20Notebooks%2F3.%20Uncertainty%20Analysis.ipynb): This notebook shows the results of the uncertainty analysis and tests the pareto policies against different scenarios to determine the robustness. However, as Notebooks tend to not like MultiProcessing, we ran the model-part of this step in a .py file, called '[`3. Uncertainty Analysis.py`](Model%20and%20Notebooks%2F3.%20Uncertainty%20Analysis.py)'
4. [`4. Scenario Discovery.ipynb`](Model%20and%20Notebooks%2F4.%20Scenario%20Discovery.ipynb): determines the best policies and makes various visualisations.
<br/><br/>
For ease of access, we made the references to the files and directory clickable. 

### Directory structure

```
---\
    Model and Notebooks\
    ------ *Model files, forked from quaquel/epa1361_open*
    ----- 2a. Open Exploration.ipynb
    ----- 2b. MOEA.ipynb
    ----- 3. Uncertainty Analysis.ipynb
    ----- 3. Uncertainty Analysis.py
    ----- 4. Scenario Discovery.ipynb

    generated_datasets\
    ------ *Modeling outputs to reproduce results*

    Visualisations\
    ------ *Figures saved from the notebooks*

    archives\
    ------ *archives saved from the notebooks*
```

To reproduce our results, please install the packages listed in the requirement.txt file

