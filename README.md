# Insta Follow Bot

A simple Python-based bot using Selenium to automatically log in to Instagram, find the followers of a specific account, and follow them.

## Features:
- **Automated Login**: The bot logs into Instagram with provided username and password.
- **Cookie Warning Handling**: The bot automatically handles cookie warnings and login prompts.
- **Auto-follow**: The bot automatically follows the people the target account is following.
- **Scroll Mechanism**: The bot scrolls through the following list to ensure it loads all users to follow.
- **Element Interaction**: Handles situations where elements may be blocked or need to be dismissed (e.g., Cancel buttons).

## Requirements:
- **Python**: Version 3.x
- **Selenium**: Python library for browser automation.
- **ChromeDriver**: Chrome WebDriver for interacting with Google Chrome. [Download ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/).
- **Google Chrome**: Ensure the latest version of Chrome is installed.

## Installation:

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/ulquiorraexe/insta-follow-bot.git
   cd insta-follow-bot

2. **Install the required dependencies**:

   Ensure you have Python installed, then install the necessary packages by running:

   ```bash
   pip install selenium
   ```

3. **Download ChromeDriver**:

   - Go to [ChromeDriver Downloads](https://sites.google.com/a/chromium.org/chromedriver/) and download the ChromeDriver that matches your version of Google Chrome.
   - Place the `chromedriver` executable in your project folder or provide the path in the script.

4. **Set Your Instagram Credentials**:

   Open the `insta_follow_bot.py` file and set your Instagram login credentials by modifying the `username` and `password` variables:

   ```python
   username = "your_username"
   password = "your_password"
   ```

## Usage

1. After setting your Instagram credentials, run the bot by executing the following command:

   ```bash
   python main.py
   ```

2. The bot will:
   - Log in to your Instagram account.
   - Navigate to a specific Instagram account's following page: `https://www.instagram.com/ogretmensitemiz/following/`.
   - Scroll through the followers list and automatically follow them.
   - Handle pop-ups such as cookie consent prompts and login save requests.

3. The bot will continue running until it completes the task or you manually stop it.

## Code Overview

### `InstaFollower` class:
- **`__init__`**: Initializes the WebDriver with Chrome options to keep the browser open.
- **`login`**: Logs in to Instagram using the provided credentials.
- **`find_followers`**: Navigates to the followers page and scrolls through the follower list.
- **`follow`**: Clicks the follow buttons for each user.

### Script Flow:
- The script logs into Instagram using your provided credentials.
- It navigates to the followers' page of a specific account.
- It automatically follows the users displayed on that page.
- Handles pop-ups like cookie consent and login save prompts to ensure smooth operation.

## Notes
- **Rate Limiting**: Be cautious when using the bot. Instagram may flag or block accounts for performing actions too quickly or for using automation. Use it responsibly.
- **Customizing the Target Account**: You can change the account whose followers you want to follow by modifying the URL in the `find_followers()` method.

## License
This project does not have a license.
