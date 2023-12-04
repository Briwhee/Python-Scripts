#Extract Table as a CSV

import pandas as pd

Japan = pd.read_csv("https://www.football-data.co.uk/new/JPN.csv")

Japan.rename(columns={'HG':'home_goals', 'AG':'away_goals'}, inplace=True)

print(Japan)