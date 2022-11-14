Написание автотестов для сайта mvideo.ru. 

Использовался стек Python + Selenium, Pytest.Для отслеживания процесса подключено логирование и формирование отчета Allure.

Были написаны тесты для страниц: Главная, Телефоны, Корзина.

Главная:
- Пользователь может открыть Главную страницу.
- Пользователь может зарегистрировать новую учетную запись для личного кабинета.
- Пользователь может войти под уже созданной учетной записью в личный кабинет.
- Пользователь может выбрать город.
- Пользователь может перейти от главной страницы на страницу телефоны.
- Клик по логотипу перезагружает страницу.
- Пользователь может ввести наименование товара в строку поиска и сформировать запрос.
- Пользователь может войти под уже созданной учетной записью, произвести поиск товара, отфильтровать нужный, выбрать необходимый магазин для получения,
пройти все необходимые шаги для подтверждения и произвести оплату(Покупка iphone 13 pro).
- Пользователь не может войти в личный кабинет указав неверный проверочный код присланный из смс или email.
- Пользователь не может выбрать несуществующий город
- Пользователь не может войти под определенным номером телефона

Телефоны:
- Пользователь может открыть страницу Телефоны.
- Пользователь может выбрать категорию телефонов samsung

Корзина:
- Пользователь может открыть страницу Корзина.
- Пользователь находясь на странице Корзина кликнув по логотип имеет возможность перейти на главную страницу
- Пользователь может выбрать город.
- Пользователь может авторизоваться в личный кабинет.
- Пользователь может выбрать товар из предложенных на странице и добавить его.
- Пользователь может удалить товар из корзины.
