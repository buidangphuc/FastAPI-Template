## Project structure
```
├─📁 backend--------------- # Backend
│ ├─📁 alembic------------- # DB migration
│ ├─📁 app----------------- # Application
│ │ ├─📁 admin------------- # System admin
│ │ │ ├─📁 api------------- # Interface
│ │ │ ├─📁 crud------------ # CRUD
│ │ │ ├─📁 model----------- # SQLA model
│ │ │ ├─📁 schema---------- # Data transmit
│ │ │ ├─📁 service--------- # Service
│ │ │ └─📁 tests----------- # Pytest
│ │ └─📁 task-------------- # Celery task
│ ├─📁 common-------------- # public resources
│ ├─📁 core---------------- # Core configuration: Config, Path Config, App Config
│ ├─📁 database------------ # Database connection
│ ├─📁 log----------------- # Log
│ ├─📁 middleware---------- # Middlewares
│ ├─📁 scripts------------- # Scripts
│ └─📁 utils--------------- # Toolkit
├─📁 model----------------- # Training model
│ ├─📁 data---------------- # Application
│ │ ├─📁 external---------- # Data from third party sources.
│ │ ├─📁 interim----------- # Intermediate data that has been transformed.
│ │ ├─📁 processed--------- # The final, canonical data sets for modeling.
│ │ ├─📁 raw--------------- # The original, immutable data dump.
│ ├─📁 models-------------- # Trained and serialized models, model predictions, or model summaries
│ ├─📁 notebooks----------- # Jupyter notebooks
│ ├─📁 references---------- # Data dictionaries, manuals, and all other explanatory materials.
│ ├─📁 reports------------- # Generated analysis as HTML, PDF, LaTeX, etc.
│ │ ├─📁 figures----------- # Generated graphics and figures to be used in reporting
│ ├─📁 ds------------------ # Application
│ │ ├─📁 config.py--------- # Store config
│ │ ├─📁 dataset.py-------- # Scripts to download or generate data
│ │ ├─📁 features.py------- # Create features for modeling
│ │ ├─📁 modeling---------- # The original, immutable data dump.
│ │ | |─📁 __init__.py----- #
│ │ | |─📁 predict.py------ # Code to run model inference with trained models  
│ │ | |─📁 train.py-------- # Code to train models
│ | |─📁 plots.py---------- # Code to create visualizations
│ ├─📁 models-------------- # Trained and serialized models, model predictions, or model summaries
└─📁 deploy---------------- # Server deployment
