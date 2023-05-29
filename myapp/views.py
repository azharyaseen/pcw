from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from bs4 import BeautifulSoup
import requests
from .models import Contact , Subscribe
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views her

def search(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        if query != None:
      #  ebay data
            ebaywebpage = requests.get(
                f'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p1380057.m570.l1313&_nkw={query}')
            sp = BeautifulSoup(ebaywebpage.content, 'html.parser')
            ebaytitle = sp.find_all('div', 's-item__title')
            ebaysellprice = sp.find_all('span', 's-item__price')
            ebayreviews = sp.find_all('div', 'x-star-rating')
            ebaylinks = [link["href"]
                         for link in sp.find_all("a", class_="s-item__link")]
            ebay_image_links = sp.select(
                'img[src^="https://i.ebayimg.com/thumbs/images/"]')
            ebay_image_links_array = []
            for i in range(len(ebay_image_links)):
                ebay_image_links_array.append(ebay_image_links[i]['src'])
            ebaylink_array = []
            for i in range(len(ebaylinks)):
                ebaylink_array.append(ebaylinks[i])
            ebaytitleLoop = [titles.text for titles in ebaytitle]
            ebaysellpriceLoop = [sell.text for sell in ebaysellprice]
            ebayreviewsLoop = [review.text for review in ebayreviews]
            
            ebay_data = {
                'links': ebaylink_array,
                'images': ebay_image_links_array,
                'titles': ebaytitleLoop,
                'prices': ebaysellpriceLoop,
                'reviews': ebayreviewsLoop,
            }
            # Sort ebay data by price
            ebay_data['data'] = sorted(
                zip(ebay_data['titles'], ebay_data['prices'],
                    ebay_data['reviews'], ebay_data['links'],
                    ebay_data['images'],
                    ),
            )

#  if the above data cant be found
            ebay2webpage = requests.get(
                f'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p1380057.m570.l1313&_nkw={query}')
            sp = BeautifulSoup(ebay2webpage.content, 'html.parser')
            ebay2title = sp.find_all('div', 's-item__title')
            ebay2sellprice = sp.find_all('span', 's-item__price')
            ebay2links = [link["href"]
                         for link in sp.find_all("a", class_="s-item__link")]
            ebay2_image_links = sp.select(
                'img[src^="https://i.ebayimg.com/thumbs/images/"]')
            ebay2_image_links_array = []
            for i in range(len(ebay2_image_links)):
                ebay2_image_links_array.append(ebay2_image_links[i]['src'])
            ebay2link_array = []
            for i in range(len(ebay2links)):
                ebay2link_array.append(ebay2links[i])
            ebay2titleLoop = [titles.text for titles in ebay2title]
            ebay2sellpriceLoop = [sell.text for sell in ebay2sellprice]
            ebay2_data = {
                'links': ebay2link_array,
                'images': ebay2_image_links_array,
                'titles': ebay2titleLoop,
                'prices': ebay2sellpriceLoop,
            }
            # Sort ebay data by price
            ebay2_data['data'] = sorted(
                zip(ebay2_data['titles'], ebay2_data['prices'],
                    ebay2_data['links'], ebay2_data['images'],
                    ),
            )
           
#  FlipKart data
            flipcartwebpage = requests.get(
                f'https://www.flipkart.com/search?q={query}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off')
            sp = BeautifulSoup(flipcartwebpage.content, 'html.parser')
            flipcart_title = sp.find_all('div', '_4rR01T')
            flipcart_price = sp.find_all('div', '_30jeq3 _1_WHN1')
            flipcart_reviews = sp.find_all('div', '_3LWZlK')
            flipcart_links = [link["href"]
                              for link in sp.find_all("a", class_="_1fQZEK")]
            flipcart_image_links = [link["src"]
                                    for link in sp.find_all("img", class_="_396cs4")]
            flipcart_image_links_array = []
            for i in range(len(flipcart_image_links)):
                flipcart_image_links_array.append(flipcart_image_links[i])
            flipcart_links_array = []
            for i in range(len(flipcart_links)):
                flipcart_links_array.append(flipcart_links[i])
            flipcart_titleLoop = [
                flipcart_title.text for flipcart_title in flipcart_title]
            flipcart_priceLoop = [
                flipcart_price.text for flipcart_price in flipcart_price]
            flipcart_reviewsLoop = [
                flipcart_reviews.text for flipcart_reviews in flipcart_reviews]
            flipkart_data = {
                'links': flipcart_links_array,
                'images': flipcart_image_links_array,
                'titles': flipcart_titleLoop,
                'prices': flipcart_priceLoop,
                'reviews': flipcart_reviewsLoop,
            }
            # Sort ebay data by price
            flipkart_data['data'] = sorted(
                zip(flipkart_data['titles'], flipkart_data['prices'],
                    flipkart_data['reviews'], flipkart_data['links'],
                    flipkart_data['images']
                    ),
            )

# if above things are not found there
            flipcartwebpage2 = requests.get(
                f'https://www.flipkart.com/search?q={query}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off')
            sp = BeautifulSoup(flipcartwebpage2.content, 'html.parser')
            flipcart2_title = sp.find_all('a', 's1Q9rs')
            flipcart2_price = sp.find_all('div', '_30jeq3')
            flipcart2_reviews = sp.find_all('div', '_3LWZlK')
            flipcart2_links = [link["href"]
                               for link in sp.find_all("a", class_="s1Q9rs")]
            flipcart2_image_links = [link["src"]
                                     for link in sp.find_all("img", class_="_396cs4")]
            # print(flipcart_image_links)
            flipcart2_image_links_array = []

            for i in range(len(flipcart2_image_links)):
                flipcart2_image_links_array.append(flipcart_image_links[i])
            flipcart2_links_array = []
            for i in range(len(flipcart2_links)):
                flipcart2_links_array.append(flipcart2_links[i])
            flipcart2_titleLoop = [
                flipcart2_title.text for flipcart2_title in flipcart2_title]
            flipcart2_priceLoop = [
                flipcart2_price.text for flipcart2_price in flipcart2_price]
            flipcart2_reviewsLoop = [
                flipcart2_reviews.text for flipcart2_reviews in flipcart2_reviews]
            flipkart2_data = {
                'links': flipcart2_links_array,
                'images': flipcart2_image_links_array,
                'titles': flipcart2_titleLoop,
                'prices': flipcart2_priceLoop,
                'reviews': flipcart2_reviewsLoop,
            }
            # Sort ebay data by price
            flipkart2_data['data'] = sorted(
                zip(flipkart2_data['titles'], flipkart2_data['prices'],
                    flipkart2_data['reviews'], flipkart2_data['links'],
                    flipkart2_data['images']
                    ),
            )

# if above things are not found there
        flipcartwebpage3 = requests.get(
                f'https://www.flipkart.com/search?q={query}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=off&as=off')
        sp = BeautifulSoup(flipcartwebpage3.content, 'html.parser')
        flipcart3_title = sp.find_all('div', '_2WkVRV')
        flipcart3_price = sp.find_all('div', '_30jeq3')
        flipcart3_links = [link["href"]
                               for link in sp.find_all("a", class_="_2UzuFa")]
        flipcart3_image_links = [link["src"]
                                     for link in sp.find_all("img", class_="_2r_T1I")]
        flipcart3_image_links_array = []
        for i in range(len(flipcart3_image_links)):
                flipcart3_image_links_array.append(flipcart3_image_links[i])
        flipcart3_links_array = []
        for i in range(len(flipcart3_links)):
                flipcart3_links_array.append(flipcart3_links[i])
        flipcart3_titleLoop = [
                flipcart3_title.text for flipcart3_title in flipcart3_title]
        flipcart3_priceLoop = [
                flipcart3_price.text for flipcart3_price in flipcart3_price]
        flipkart3_data = {
                'links': flipcart3_links_array,
                'images': flipcart3_image_links_array,
                'titles': flipcart3_titleLoop,
                'prices': flipcart3_priceLoop,
            }
            # Sort ebay data by price
        flipkart3_data['data'] = sorted(
                zip(flipkart3_data['titles'], flipkart3_data['prices'],
                    flipkart3_data['links'], flipkart3_data['images']
                    ),
            )

    return render(request, 'search-result.html', {'ebay_data': ebay_data,'ebay2_data': ebay2_data, 'flipkart_data': flipkart_data, 'flipkart2_data': flipkart2_data,'flipkart3_data':flipkart3_data, 'query': query})

def index(request):
    return render(request, 'index.html')
  
def subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        subscibe = Subscribe(email=email)
        subscibe.save()
    return render(request, 'subscribe.html')

def team(request):    
    return render(request, 'team.html')

def about_us(request):
    return render(request, 'about_us.html')

def services(request):
    return render(request, 'services.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        User.objects.create_user(username=username, password=password,email=email)        
        return redirect('login')
    return render(request, 'register.html')

def LoginPage(request):  
    if request.method == 'POST':
            username = request.POST['username']       
            password = request.POST['password']  
            user = authenticate(request=request, username=username,password=password)
            if user is not None:
                return redirect('/home')
                messages.success(request, "successfully logged in")
            else:
                messages.warning(request, "invalid credentials")    
    return render (request,'login.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        contact_form = Contact(name=name, email=email,
                               subject=subject, message=message)
        contact_form.save()
        messages.success(request, "your message succesfully delivered!")

    return render(request, 'contact.html')
