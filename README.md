# MÕL (Matemaatika õppimise lehekülg)

Kristian Kõivastik, Mikk Reinkubjas, Silver Nõgols

Teema: Matemaatika riigieksamiks valmistumine

Lühikirjeldus: Veebirakendus, millega saab ette valmistuda matemaatika riigieksamiks. Seal saab õppida valemeid, et need paremini ja lihtsamini meelde jääks.

Ülesanded: https://trello.com/invite/b/66e009d4df074761a8900389/ATTIbf81fcdbdee7198661a586072e8af8bb2EE268D9/proge-matemaatika-eksamiks-oppimine

Figma prototüüp: https://www.figma.com/design/NycjU9DmSonCdnZszjRUjV/Untitled?node-id=0-1&t=vNDZWrawTzXrZVWb-1

**Projekti veebileht: https://riigieksam.pythonanywhere.com/**

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/kristiank139/progeprojekt.git
    cd progeprojekt
    ```

2. Install Django:
    ```sh
    pip install Django
    ```

3. Install `django-latexify`:
    ```sh
    pip install django-latexify
    ```

4. Install `google-generativeai`:
    ```sh
    pip install google-generativeai
    ```

## Running the Application

1. Navigate to the `src/mol` directory:
    ```sh
    cd src/mol
    ```

2. Run the development server:
    ```sh
    python manage.py runserver
    ```

3. Open your web browser and go to `http://127.0.0.1:8000/` to see the application in action.
