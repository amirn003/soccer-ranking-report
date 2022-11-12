import pandas as pd

## extract from html

def getPremierLeagueRanking():
    prem_table = pd.read_html('https://www.bbc.co.uk/sport/football/premier-league/table')
    print(type(prem_table))
    Premier_table = prem_table[0]
    print(type(Premier_table))
    #print(prem_table)

    return Premier_table


def getLigue1Ranking():

    l1_table = pd.read_html('https://www.lequipe.fr/Football/ligue-1/page-classement-equipes/general')
    print(type(l1_table))
    L1_table = l1_table[0]
    print(type(L1_table))
    #print(prem_table)

    return L1_table


##drop columns

""" Premier_table.columns
Index(['Unnamed: 0', 'Unnamed: 1', 'Team', 'P', 'W', 'D', 'L', 'F', 'A', 'GD',
       'Pts', 'Form'],
      dtype='object')

Premier_league = Premier_table.drop(['Unnamed: 1'], axis=1)
Premier_league.head(6) """