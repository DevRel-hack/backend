# DEVREL HACKATHON: DevRel Hack 2.0. Команда 7Eleven.

## Задача
Ваша цель - создать инструмент, который сделает работу DevRel более эффективной, позволив легко управлять и взаимодействовать с участниками ИТ-сообщества.<br>
Сервис должен включать в себя следующие ключевые функциональности:<br>

Управление участниками:<br>
Регистрация новых участников, добавление и обновление их данных.<br>
Возможность классификации участников по различным критериям.<br>
 
Аналитика:<br>
Система аналитики для отслеживания активности участников и успеха проведенных мероприятий.<br>
Построение отчетов о мероприятиях и участниках.<br>
 
Рассылки и коммуникации:<br>
Возможность отправки персонализированных сообщений участникам.<br>
Автоматизированные рассылки о предстоящих событиях и новостях, обновлениях.<br>
 
Интеграция социальных сетей:<br>
Возможность подключения к социальным сетям для мониторинга обсуждений и взаимодействия внутри сообщества.<br><br>
## Решение
Сервис состоит из 4 основных разделов:<br>
1. Главная: <br>
Планировщик задач DevRel: клаендарь и TODO-лист DevRel на выбранный день. Переход в Kanban-доску организации и проведения мероприятия.<br>
2. Люди:<br>
База данных контактов и участников. Таблица с профилями и активностью. Данные грузятся с внешних ресурсов, отвечающих за регистрацию участников на мероприятия. Есть возможность добавления контакта вручную. Удобные фильтры. Просмотр карточки контакта с данными по участию в меропритиях с комментарием DevRel.<br>
3. Мероприятия:<br>
Просмотр/создание/изменение мероприятий. Иконки статистики (регистрации/посещения/KPI), удобные фильтры. Возможность добавления мероприятий в сравнение.<br>
В карточке мероприятия детальные данные; ключевые участники (организаторы/спикеры/проч.) с комментариями о работе, которые доступны в виде истории<br>
4. Рассылки:<br>
Список контактов в БД - возможность настройки списка получателей по фильтрам и отправки сообщения. Хранится история рассылок с данными о результатах переходов и регистраций по ссылкам, загружаемыми с внешних API.<br>
5. Аналитика: <br>
Статистика по мероприятиям с ключевыми показателями: регистрации/посещения/KPI/бюджет;<br>
График активности регистраций по выбранным периодам.<br>
Портрет участника мероприятий в разрезе тегов мероприятий/должности/навыков/уровня знаний<br>

## Figma
https://www.figma.com/file/BHx1XvXp1SEpR47URlaFax/%D0%A5%D0%B0%D0%BA%D0%B0%D1%82%D0%BE%D0%BD-DevRel-2023?type=design&node-id=89-7478&mode=design&t=vv4E1vhwWtQzIBsU-0


##  BACKEND: 
### Инструменты:
![image](https://img.shields.io/badge/Python%203.11-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![image](https://img.shields.io/badge/Django%204.2-092E20?style=for-the-badge&logo=django&logoColor=green)
![image](https://img.shields.io/badge/django%20rest%203.14-ff1709?style=for-the-badge&logo=django&logoColor=white)
![image](https://img.shields.io/badge/DRF_Spectacular-aa1000?style=for-the-badge&logo=django&logoColor=white)
![image](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![image](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)
![image](https://img.shields.io/badge/Nginx-009639?style=for-the-badge&logo=nginx&logoColor=white)
![image](https://img.shields.io/badge/Poetry-053766?style=for-the-badge&logo=Sailfish%20OS&logoColor=white)


## Frontend:
Код: https://github.com/DevRel-hack/frontend<br>
Сборка: https://devrel-hack.github.io/dev-rel-me/entry/login

### Описание возможностей BACKEND (возможности прототипа отличаются от концепта выше)
```
Регистрация / Аутентификация / Выход
Получение списка всех аттрибутов специалистов и мероприятий (для фильтра и аналитики)
Мероприятия: получение списка (общая информация + статистика), просмотр данных по мероприятию (общая информация + список участников с комментариями), создание/изменение/удаление; удобные фильтры по теме/тегам/формату
Участники: список участников ("встреча-специалист-роль(слушатель/организатоор/спискер)-комментарий о его участии"), просмотр 1 участника, создание, изменение, удаление;
Специалисты: получение списка (профиль + активность), просмотр (профиль + список мероприятий, в которых участвовал с комментариями), изменение, удаление; удобные фильтры по тексту/работе/навыкам/ролям в мероприятиях
Статистика: статистика посещения всех или 1 мероприятия в разрезе тегов, навыков, развития, направлениям работы; 
```

## Запуск проекта
### Переменные окружения
Необходимо создать файл .env - хранится в корневой папке проекта; пример заполнения в .env.example (можно переименовать в .env).

### Запуск с установленным Docker
Копировать проект в папку целиком (для запуска контейнеров достаточно .env в корне проекта и папки /deploy)
```
git clone git@git.codenrock.com:devrel-2.0/cnrprod-team-66306/devrel-hack.git
```
Перейти в папку deploy и запустить сборку контейнеров
```
cd backend/deploy
docker compose up -d --build
```
Сервис доступен по адресу http://127.0.0.1/<br>
В базе данных уже есть Суперпользователь с указанными в .env данными (или данными по умолчанию выше). Для загрузки фикстур людей и мероприятий предусмотрены соответствующие эндпонты.

### Доступ в админ-панель:
http://127.0.0.1/admin 
```
email: admin@admin.admin
password: Password-123
```

### API-документация:
http://127.0.0.1/api/schema/swagger/#
```
Авторизация через headers:
Authorization: JWT <access-token>
```

## Команда
### Project Manger
Марина Нюнякина
### Backend:
[Руслан Атаров](https://github.com/ratarov) <br>
### Design:
[Евгения Постникова](https://www.behance.net/eugi_eugenia)<br>
### Frontend:
[Влад Мещеринов](https://github.com/beardy-raccoon) <br>
[Артем Никифоров](https://github.com/Art-Frich) <br>