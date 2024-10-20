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
└─📁 deploy---------------- # Server deployment
```

## Local development / Docker deployment

For more details, please check
the [official documentation](https://fastapi-practices.github.io/fastapi_best_architecture_docs/)

## License

This project is licensed by the terms of
the [MIT](https://github.com/fastapi-practices/fastapi_best_architecture/blob/master/LICENSE) license
