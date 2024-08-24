












# Настройте свою виртуальную среду для Windows

```bash
python -m venv env 
.\env\Scripts\activate 
pip install -r requirements.txt 
```
# Если вы используете Linux или macOS, вы вместо этого запустите

```bash
python3 -m venv env 
source ./env/bin/activate
pip install -r requirements.txt
```

# Создаем и запускаем контейнер(У вас должен быть Docker установлен)

```bash
docker-compose up -d --build
```
