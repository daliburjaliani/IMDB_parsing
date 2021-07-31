from bs4 import BeautifulSoup
import datetime


def pop_movie():
    import requests
    url = "https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm"

    requests = requests.get(url).text

    soup = BeautifulSoup(requests, 'html.parser')

    data = soup.find('tbody')
    movie = data.find_all('tr')

    for index, i in enumerate(movie, 1):
        try:
            n = i.find("td", class_='titleColumn')
            name = n.find("a").text
            year = n.find("span").text
            r = i.find("strong").text

            print(f"{index}.{name}{year} | IMDb Rating - {r}")

        except:
            r = None


def by_ganre():
    import requests

    genre = input("Enter Ganre : ")

    url = 'https://www.imdb.com/search/title/?genres='

    requests = requests.get(
        url + genre.lower() + '&explore=title_type,genres&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=3396781f-d87f-4fac-8694-c56ce6f490fe&pf_rd_r=76YPF52252A1VVV4QQ79&pf_rd_s=center-1&pf_rd_t=15051&pf_rd_i=genre&ref_=ft_gnr_pr1_i_2').text

    soup = BeautifulSoup(requests, 'html.parser')

    data = soup.find_all("div", class_="lister-item mode-advanced")

    for index, i in enumerate(data, 1):

        try:
            movie = i.find("h3")
            name = movie.find("a").text
            year = movie.find_all("span")[1].text
            content = i.find_all('p', class_='text-muted')[1].text
            r = i.find("strong").text
            act = i.find_all("p")[2]
            stars = act.find_all("a")[0:4]

            print(
                f"{index}. Movie: {name}{year} | IMDB Rating - {r} -{content} \nStars: {stars[0].text}, {stars[1].text}, {stars[2].text}, {stars[3].text} \n")

        except:
            r = None


def top_rated():
    import requests

    url = 'https://www.imdb.com/chart/top/?ref_=nv_mv_250'

    requests = requests.get(url).text

    soup = BeautifulSoup(requests, 'html.parser')

    data = soup.find('tbody')

    mov = data.find_all('tr')

    for index, i in enumerate(mov, 1):
        name = i.find_all('a')[1].text
        year = i.find_all('span')[5].text
        r = i.find('strong').text

        print(f'{index}. Movie: {name}{year} | IMDB Rating - {r}')


def bth():
    import requests

    x = datetime.datetime.now()

    date = f'{x.strftime("%m")}-{x.strftime("%d")}'

    url = 'https://www.imdb.com/search/name/?birth_monthday='+date+'&ref_=nv_cel_brn'
    requests = requests.get(url).text

    soup = BeautifulSoup(requests, 'html.parser')

    data = soup.find_all("div", class_='lister-item-content')

    for index, i in enumerate(data, 1):
        name = i.find("a").text
        cont = i.find_all("p")[1].text

        print(f"{index}.{name}{cont}\n")


def coming_soon():
    import requests

    url = 'https://www.imdb.com/movies-coming-soon/?ref_=inth_cs'

    requests = requests.get(url).text

    soup = BeautifulSoup(requests, 'html.parser')

    data = soup.find_all('td', class_='overview-top')

    for index, i in enumerate(data, 1):
        name = i.find('a').text
        con = i.find('div', class_='outline').text

        st = i.find_all('div', class_='txt-block')[1]
        stars = st.find_all('a')[0:4]

        print(f'{index}. {name} {con} \nStars: {stars[0].text}, {stars[1].text}, {stars[2].text}, {stars[3].text}')


def menu():
    inp = int(input("Choose \n1) Popular Movie \n2) Top 50 Tv Shows and Movie by Genre \n3) Top Rated \n4) Born Today "
                    "\n5) This Month \n->  "))

    if inp == 1:
        pop_movie()
    elif inp == 2:
        by_ganre()
    elif inp == 3:
        top_rated()
    elif inp == 4:
        bth()
    else:
        print("Choose correctly!")


while True:
    menu()
    print('-----------------------------------------------------------------------------------------------')
