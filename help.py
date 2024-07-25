import pygsheets
path='G:\\My Drive\\Climbing Club Personal\\Service Account\\phrasal-bivouac-430516-d6-c28bf227a425.json'
client = pygsheets.authorize(service_account_file=path)
sh = gc.open('pythontest') # Open the google sheet phthontest
wks = sh[0] # select the first sheet 
wks.update_col(2,['ab','cd','ef']) # add list to 2nd column