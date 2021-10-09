import requests
from bs4 import BeautifulSoup
import urllib.request
import json
import uuid
import sched, time


biglist = []

def verify_url(url):
    try:
        link = url.strip()
        link = link.split('//')[1]
        link = link.split('/')
        if link[1] == 'public_profiles' and uuid.UUID(link[2]):
            return True
        else:
            return False
    except:
        return False

def get_profile_data(url: str) -> dict:
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        quests = soup.findAll('div', attrs = {'class':'profile-badge'})
        latest_quest = []
        user = dict()
        user['name'] = soup.find('h1', attrs = {'class':'ql-headline-1'}).text
        badge_count = 0
        old_badge_count = 0
        for quest in quests:
            old_badge_count += 1
            time=quest.find('span', attrs = {'class':'ql-body-2 l-mbs'})
            date=time.text.split()
            #print(date)
            if(date[1]=='Oct' and date[2][0]=='9' and date[3]=='2021'):
                badge_count+=1
                latest_quest.append(quest.find('span', attrs = {'class':'ql-subhead-1 l-mts'}).text)
        user['badges'] = latest_quest
        user['badge_count'] = badge_count
        user['profile_url'] = url
        user['old_badge_count'] = old_badge_count
        user['status'] = 'success'
        return user
    except:
        user = dict()
        user['profile_url'] = url
        user['status'] = 'failure'


def gather_data():
    url_file = open('userurl.txt', 'r')
    for line in url_file.readlines():
        line = line.strip()   
        biglist.append(get_profile_data(line))
    #print(biglist)
    url_file.close()

def write_data():
    with open('userdata.json', 'w') as outfile:
        json.dump(biglist, outfile)

def sort_by_key(list):
    return list['badge_count']

def sort_data():
    sorted(biglist,key=sort_by_key, reverse=True)



def main():
    try:
        gather_data()
        print('Data Gathered',end='\n')
    except:
        print('Error in gathering data',end='\n')
    finally:
        try:
            write_data()
            print('Data Written',end='\n')
        except:
            print('Error in writing data',end='\n')
    try:
        sort_data()
        print('Data Sorted',end='\n')
    except:
        print('Error in sorting data',end='\n')
    finally:
        try:
            print('Done')
        except:
            print('Error in Process',end='\n')



if __name__ == "__main__":
    try:
        print('Running....',end='\n')
        while True:
            try:
                main()
            except:
                print('Error in main',end='\n')
                exit()
            finally:
                try:
                    print('Sleeping for 1 hour',end='\n')
                    time.sleep(3600)
                    print('Script Re-executing ...')
                except:
                    print('Error!!!',end='\n')
                    exit()
    except KeyboardInterrupt:
        print('Exiting!!!',end='\n')
    except Exception as e:
        print(e)
    except:
        print('Unknown Error!!!',end='\n')
    exit()

#print(get_profile_data('https://www.qwiklabs.com/public_profiles/07a95dbe-9d41-4ef9-acd3-620a73ef7720'))


