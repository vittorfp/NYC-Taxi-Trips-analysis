NYC Taxi trips analysis
==============================

Este repositório contém os códigos utilizados para realizar a análise da base NYC Taxi trips, mais especificamente no
contexto de um teste técnico para a vaga de Engenheiro de dados na DataSprints.
 
Para reproduzir as análises é necessário rodar os seguintes comandos no terminal (já é necessário ter o python3 e o
venv instalados):
```bash
git clone https://github.com/vittorfp/NYC-Taxi-Trips-analysis.git
cd NYC-Taxi-Trips-analysis/
 
python3 -m venv .venv
source .venv/bin/activate
 
make data
```
 
Os comandos acima vão clonar o repositório, criar um *venv*, realizar o download dos dados a partir dos links
fornecidos na [especificação do teste](references/Teste%20Técnico%20-%20Engenharia%20de%20Dados.pdf) (pode dermorar) 
e realizar sua inserção em um banco de dados SQLite, para que seja possível realizar consultas SQL nos dados
(um dos requisitos do teste técnico).
 
Após esse comando abra um ``jupyter lab`` na raiz do repositório e fique a vontade para refazer as análises utilizando
os notebooks que estão dentro da pasta *notebooks*. Observação: Os notebooks devem ser executados com o kernel
``NYC-taxi-trips-analysis`` (também foi criado com o comando rodado, mais detalhes no [Makefile](Makefile)) que possui
todas as dependências necessárias instaladas.
 
O arquivo [Análise.html](notebooks/Análise.html) é uma versão em HTML do notebook utilizado para realizar as
análises.



Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.testrun.org


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
