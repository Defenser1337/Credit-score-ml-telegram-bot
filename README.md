# Credit score ml telegram bot

This telegram bot can help you estimate your credit score without going to the bank. The bot works using a machine learning model trained on this dataset [Credit score classification](https://www.kaggle.com/datasets/parisrohan/credit-score-classification).

You can deploy your own bot or use mine.

# Features

- In order to get an estimate of your credit score, you need to take a small survey, after which the machine learning model will tell you a prediction: `good` or `bad`
- The repository also contains: dataset analysis and model building (all comments and conclusions in Jupyter Notebooks are in Russian)

# Bot commands

- `/start` - The command to start the survey, after passing the model will make a prediction

# Setup

1. Get your Telegram bot token from [@BotFather](https://t.me/BotFather)
2. Clone the repository into your directory
```bash
cd path/to/your/directory
git clone https://github.com/Defenser1337/Credit-score-ml-telegram-bot.git
```
3. Create a new `.venv`, then install all dependencies
```bash
pip install -r requirements.txt
```
4. Run `main.py` from the `code/bot` folder

# Recreate the model construction

1. Download the dataset from this link [Credit score classification](https://www.kaggle.com/datasets/parisrohan/credit-score-classification)
2. Change all paths in Jupyter Notebook to place where you uploaded the dataset
3. Now u can run all cells in notebook

# Contributors
- Me [Defenser1337](https://github.com/Defenser1337)
