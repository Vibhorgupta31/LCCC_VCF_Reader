# LCCC VCF Dataset Reader WebApplication

A python based webapplication to read vcf dataset built on TileDBVCF technology

### Package requirements

Following python packages are needed to run the code:
- python ==3.10.13
- streamlit ==1.29.0
- tiledbvcf ==0.27.1
- pandas ==2.1.4
- anaconda

### Installation instructions

- conda create --name environment_name python=3.10
- pip install streamlit
- conda install -c conda-forge -c bioconda -c tiledb tiledbvcf-py

### Instructions to run the app

- Alter the path for the metadata and the tiledbvcf dataset file in the code and save it
- On the terminal use streamlit run main.py to run the code

If everything goes well you should see the output as in the figure below:

<img width="1187" alt="Screenshot 2024-01-09 at 10 29 35" src="https://github.com/Vibhorgupta31/LCCC_VCF_Reader/assets/55628881/7f3fabc9-b016-4fdf-9b4d-48b9f7c2c376">


