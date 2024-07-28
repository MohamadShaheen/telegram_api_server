# Fastapi Server

This server provides endpoints for searching Telegram users by `keyword`.

# Installation and Setup

1. **Environment Variables:**
  - Create an `.env` file in the root directory of your project.
  - Add the following environment variables:
      - `API_ID`: The API ID for accessing the Telegram API.
      - `API_HASH`: The API hash for accessing the Telegram API.

    **WARNING:** Ensure the `.env` file is listed in your `.gitignore` to prevent it from being included in your version control system, such as GitHub.

    You can obtain these values from the [Telegram Credentials Generator](https://my.telegram.org/auth). For more details, refer to [Obtaining API ID](https://core.telegram.org/api/obtaining_api_id). A phone number is required to acquire these credentials.

2. **Install Dependencies:**

    Run the following command to install the required Python packages:
    ```shell
    pip install -r requirements.txt
    ```

3. **Initialize User Data:**

    If the user data is not already found in `data/users.json`, run the following script:
      ```shell
      python utils/search_telegram_users.py
      ```

# Packages Used

- `Telethon`: A library for interacting with Telegram's API, used here to fetch users from a specific group for search functionality.
- `cryptg`: A package that improves the performance of `Telethon` by handling encryption and decryption in C rather than Python.

# Running The Server

To start the FastAPI server, use the following command:
```shell
uvicorn server:app
```