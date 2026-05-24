# Jenkins + GitHub — Atividade Prática

Projeto criado para a atividade prática de integração contínua com Jenkins e GitHub.

## Descrição

Projeto em Python com dois métodos de conversão de temperatura:

- **Fahrenheit → Celsius**
- **Celsius → Fahrenheit**

## Estrutura

```
jenkins-atividade/
├── conversor.py        → métodos de conversão
├── test_conversor.py   → casos de teste
└── Jenkinsfile         → pipeline do Jenkins
```

## Como executar os testes

```bash
pip install pytest pytest-cov
pytest test_conversor.py -v
```

## Cobertura de código

```bash
pytest --cov=conversor --cov-report=term test_conversor.py
```
