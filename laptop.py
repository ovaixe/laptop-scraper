from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'https://www.flipkart.com/search?q=best%20laptops%20under%2080000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'

page = urlopen(url)
page_html = page.read()
page.close()
page_soup = BeautifulSoup(page_html, 'html.parser')

containers = page_soup.findAll('div', {'class': '_2kHMtA'})
print('Total div elements: ', len(containers))

# print(BeautifulSoup.prettify(containers[3]))

# Get the product name
product = containers[3]
product_name = product.findAll("div", {"class": "_4rR01T"})
print(f'Product Name: {product_name[0].text}')

# Get the original price of the product
original_price = product.findAll('div', {'class': '_3I9_wc _27UcVY'})
print(f'Original Price: {original_price[0].text}')

# Get the discount percentage on the product
discount_percent = product.findAll('div', {'class': '_3Ay6Sb'})
print(f'Discount on the product: {discount_percent[0].text}')

# Get the discounted price of the product
discounted_price = product.findAll('div', {'class': '_30jeq3 _1_WHN1'})
print(f'Discounted price of the product: {discounted_price[0].text}')

# Get the product ratings
ratings = product.findAll('span', {'class': '_1lRcqv'})
if ratings:
    print(f'Ratings: {ratings[0].text}')
else:
    print('No ratings for the product')

# Get the product reviews
reviews = product.findAll('span', {'class': '_2_R_DZ'})
if reviews:
    print(f'Reviews: {reviews[0].text}')
else:
    print('No reviews for the product')



for product in containers[:5]:
    product_name = product.findAll("div", {"class": "_4rR01T"})
    name = product_name[0].text.strip()

    original_price = product.findAll("div", {"class": "_3I9_wc _27UcVY"})
    price = original_price[0].text.strip()

    discount_percent = product.findAll("div", {"class": "_3Ay6Sb"})
    percent = discount_percent[0].text.strip()

    discounted_price = product.findAll("div", {"class": "_30jeq3 _1_WHN1"})
    discounted_price = discounted_price[0].text.strip()

    product_rating = product.findAll("span", {"class": "_1lRcqv"})
    rating = product_rating[0].text.strip()

    product_reviews = product.findAll("span", {"class": "_2_R_DZ"})
    reviews = product_reviews[0].text


    print("\033[1mProduct Name: \n"+ '\033[0m'+ str(name), "\n"),
    print("\033[1mOriginal Price: \n"+ '\033[0m'+ str(price), "\n"),
    print("\033[1mDiscount Percentage: \n"+ '\033[0m'+ str(percent), "\n"),
    print("\033[1mDiscounted Price: \n"+ '\033[0m'+ str(discounted_price), "\n"),
    print("\033[1mRatings: \n"+ '\033[0m'+ rating, "\n"),
    print("\033[1mNumber of Reviews: \n"+ '\033[0m'+ reviews, "\n"),
    print("------------------------------------------------------------------------------------------------------------------")