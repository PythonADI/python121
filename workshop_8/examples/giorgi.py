
rivers = {
    "Nile" : "Egypt",
    "Mississippi" : "USA",
    "Thames" : "UK"
}


screen_size = (1920, 1080)

# width = screen_size[0]
# height = screen_size[1]
width, height = screen_size
print(f"{width}x{height}")

for river, country in rivers.items():
    # river, country = item
    # print(item)
    print(f"{river} flows through {country}")



# list in dict
products = [
    {
        "title": "Iphone 16",
        "price": 1000
    },
    {
        "title": "Samsung Galaxy s25",
        "price": 1100
    },
    {
        "title": "Iphone 16 Pro Max",
        "price": 1200
    },
]

products.append({
    "title": "Pixel 9 XL",
    "price": 1300
})

print(products)
products[0]

for product in products:
    # for key, value in product.items():
    #     print(f"{key}: {value}")
    product["title"]
