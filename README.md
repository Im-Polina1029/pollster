<div>
  <img src="https://github.com/Im-Polina1029/pollster/blob/main/src/app/common_static/img/header.png">
</div>

**Современный многофункциональный отечественный сервис для создания и прохождения опросов**

*Создавай - Узнавай - Анализируй*  

## 🛠 Технологический стек

### Основные технологии
<div align="center">
  <img src="https://img.shields.io/badge/Python-3.9+-%233776AB?logo=python" alt="Python">
  <img src="https://img.shields.io/badge/Django-4.0+-%23092E20?logo=django" alt="Django">
  <img src="https://img.shields.io/badge/MySQL-8.0+-%234479A1?logo=mysql" alt="MySQL">
  <img src="https://img.shields.io/badge/Docker-%232496ED?logo=docker" alt="Docker">
  <img src="https://img.shields.io/badge/RabbitMQ-%23FF6600?logo=rabbitmq" alt="RabbitMQ">
</div>

### Все используемые технологии
<div align="center" style="margin-top: 15px;">
  <!-- Технологии с бейджами -->
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original-wordmark.svg" width="70" title="Python 3.9+">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/django/django-plain-wordmark.svg" width="70" title="Django 4.0+">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/mysql/mysql-original-wordmark.svg" width="70" title="MySQL 8.0+">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/docker/docker-original.svg" width="70" title="Docker">
  
  <!-- Технологии без бейджей -->
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg" width="70" title="JavaScript">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original-wordmark.svg" width="70" title="HTML5">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/css3/css3-original-wordmark.svg" width="70" title="CSS3">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/rabbitmq/rabbitmq-original-wordmark.svg" width="70" title="RabbitMQ">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pandas/pandas-original-wordmark.svg" width="70" title="Pandas">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/tensorflow/tensorflow-original-wordmark.svg" width="70" title="TensorFlow">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/jquery/jquery-original-wordmark.svg" width="70" title="jQuery">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/keras/keras-original-wordmark.svg" width="70" title="Keras">
</div>

## 🌟 Ключевые возможности

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 15px; margin: 20px 0;">

<div style="background: #f8f9fa; padding: 15px; border-radius: 8px; border-left: 4px solid #6f42c1;">
<strong>📝 Создание опросов</strong><br>
Несколько типов вопросов, гибкие настройки, интуитивный интерфейс
</div>

<div style="background: #f8f9fa; padding: 15px; border-radius: 8px; border-left: 4px solid #28a745;">
<strong>🔐 Безопасность</strong><br>
PoW защита от спама, надежная аутентификация, шифрование данных
</div>

<div style="background: #f8f9fa; padding: 15px; border-radius: 8px; border-left: 4px solid #fd7e14;">
<strong>📊 Аналитика</strong><br>
Экспорт в CSV/PDF, визуализация результатов, статистика
</div>

<div style="background: #f8f9fa; padding: 15px; border-radius: 8px; border-left: 4px solid #17a2b8;">
<strong>⚡ Производительность</strong><br>
Асинхронные задачи через RabbitMQ, кэширование, оптимизация
</div>

</div>

## 🚀 Быстрый старт

### Установка (обычный способ)  
```bash  
git clone https://github.com/Seigneurs-Team/pollster/
cd pollster/src  
pip install -r requirements.txt  
python3 -m app.manage runserver  
```  

### Запуск через Docker  
```bash  
docker-compose up  
```  

## 🗂 Структура проекта  
```  
───src
    ├───app
    │   ├───change_settings_of_user
    │   │   └───migrations
    │   ├───common_static
    │   │   ├───css
    │   │   ├───img
    │   │   └───scripts
    │   ├───components
    │   ├───create_new_account_page
    │   │   ├───migrations
    │   │   └───templates
    │   ├───create_poll_page
    │   │   ├───migrations
    │   │   └───templates
    │   ├───delete_account
    │   │   └───migrations
    │   ├───delete_poll
    │   │   └───migrations
    │   ├───log_out
    │   │   └───migrations
    │   ├───main_page
    │   │   ├───migrations
    │   │   └───templates
    │   ├───passing_poll_page
    │   │   ├───migrations
    │   │   └───templates
    │   ├───pollster
    │   ├───profile_page
    │   │   ├───migrations
    │   │   └───templates
    │   └───sign_in_page
    │       ├───migrations
    │       └───templates
    ├───authentication
    ├───Configs
    ├───databases
    ├───Dionysus
    ├───PoW
    └───Tools_for_rabbitmq
```  



## 🤝 Как внести свой вклад  
1. Форкните репозиторий  
2. Создайте ветку для своей фичи (`git checkout -b feature/amazing-feature`)  
3. Сделайте коммит изменений (`git commit -m 'Add some amazing feature'`)  
4. Запушьте в свой форк (`git push origin feature/amazing-feature`)  
5. Откройте Pull Request  

## 📄 Лицензия  
Этот проект распространяется под лицензией MIT - подробности см. в файле [LICENSE](LICENSE).  

---  
**Разработано с ❤️ командой Seigneurs - делаем сбор мнений простым и удобным!**  
