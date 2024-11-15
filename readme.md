# Clínica Fisioterapia

## Índice

- [Pré-requisitos](#pré-requisitos)
- [Instalação](#instalação)
- [Configuração](#configuração)
- [Execução](#execução)
- [Considerações Importantes](#considerações-importantes)

## Pré-requisitos

- Python 3.x
- Biblioteca `venv` (instalada por padrão com Python 3)

## Instalação

1. **Clone o repositório** (caso ainda não tenha feito):
```bash
   git clone <https://github.com/jimmycalhado/ClinicaFisioterapia.git>

   cd ClinicaFisioterapia
```

2. **Crie uma Máquina Virtual** (venv):

```bash
  python -m venv venv
```
Ou
```bash
  python -m venv .venv
```

3. **Ativar Máquina Virtual**:
```bash
  source .venv/Scripts/activate
```

4. **Instalar requirements.txt**
```bash
  pip install -r requirements.txt
```

4. **Ir para o diretório do projeto Django**
```bash
  cd clinicaFisio
```

## Execução

- Após ir para o diretório correto do projeto e depois de fazer toda a instalação, rode os comandos abaixo para migrar as tabelas do banco de dados da models.py com:

```bash
  python manage.py makemigrations
```
- E logo após, migre:

```bash
  python manage.py migrate
```

- Rode o projeto uusando:

```bash
  python manage.py runserver
```


## Considerações Importantes

- Arquivo .gitignore: Inclua o nome da pasta da sua venv (por exemplo, venv/ ou .venv/) no .gitignore para evitar conflitos de commits.

- Substituições Necessárias: Certifique-se de substituir os tokens e IDs no arquivo .env para garantir o funcionamento correto do bot.
