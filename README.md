Notes and comments regarding "Weighted Reaction Fingerprints for Visualizing Reactivity Cliffs and Generality"

Last Updated: December 2023

The tutorial folder provides a single script and a detailed tutorial notebook to allow users to quickly get started with using the method.




The remaining folders are provided to allow interested parties to recreate the figures and analytics shown in the manuscript.

This repository contains the data used to create the figures and analytics shown in the manuscript, as well as the scripts and notebooks used for each figure, separated by folder. The main figures can be found in the folders labeled folder[1-5], and SI figures and analytics can be found in the SI folder. 

The Suzuki data used in the analysis can be found in the reactions2.db SQLite3 database, which works with the database.py file and contains a table called 'reactions' with the following columns:
    number = Column(Integer, primary_key=True)
    temperature = Column(Integer, nullable=False)
    treatment = Column(String(255), nullable=False)
    plate = Column(Integer, nullable=False)
    row = Column(String(40),nullable=False)
    column = Column(String(40), nullable=False)
    electrophile = Column(String(255), nullable=False)
    electrophile_conc = Column(types.Numeric, nullable=False)
    nucleophile = Column(String(255), nullable=False)
    nucleophile_conc = Column(types.Numeric, nullable=False)
    product = Column(String(255), nullable=False)
    catalyst = Column(String(255), nullable=False)
    catalyst_smiles = Column(String(255), nullable=False)
    catalyst_conc = Column(types.Numeric, nullable=False)
    base = Column(String(255), nullable=False)
    base_smiles = Column(String(255), nullable=False)
    base_conc = Column(types.Numeric, nullable=False)
    solvent = Column(String(255), nullable=False)
    analytical_method = Column(String(255), nullable=False)
    output_value = Column(types.Numeric, nullable=False)
    group = Column(String(255), nullable=False)
    reaction_name = Column(String(255), nullable=False)

The data used in figure 3 is in the figure 3 folder in a csv file called 'rose_data.csv', which is compiled HTE data from https://onlinelibrary.wiley.com/doi/abs/10.1002/anie.202112454.

The data used in figure 5 is in the figure 5 folder in various csv files sourced from https://www.nature.com/articles/s41467-023-39531-0. 

For all figures with analytics (figures 2-5), there is a single notebook file in the corresponding figure folder that can be run to regenerate images shown in the manuscript. 

Likewise, most figures in the SI can be recreated with the corresponding notebook file found in its respective folder on the repository. 

