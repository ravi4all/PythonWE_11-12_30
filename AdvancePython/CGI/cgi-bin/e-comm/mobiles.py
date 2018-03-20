#!C:/Python36/python.exe

productList = []
productList.extend([
        {'id' : 101, 'name' : 'Apple', 'price' : 55000, 'url' : 'https://store.storeimages.cdn-apple.com/4974/as-images.apple.com/is/image/AppleInc/aos/published/images/i/ph/iphone/x/iphone-x-select-2017?wid=189&hei=376&fmt=png-alpha&qlt=95&.v=1504378258086'},
        {'id' : 102, 'name' : 'Samsung', 'price' : 45000, 'url' : 'http://images.samsung.com/is/image/samsung/p5/in/smartphones/galaxy-s8/images/gallery/galaxy-s8-plus_gallery_right_side_coralblue_s4.png?$ORIGIN_PNG$'},
        {'id' : 103, 'name' : 'Redmi', 'price' : 12000, 'url' : 'https://store.storeimages.cdn-apple.com/4974/as-images.apple.com/is/image/AppleInc/aos/published/images/i/ph/iphone/x/iphone-x-select-2017?wid=189&hei=376&fmt=png-alpha&qlt=95&.v=1504378258086'},
        {'id' : 104, 'name' : 'Vivo', 'price' : 25000, 'url' : 'http://images.samsung.com/is/image/samsung/p5/in/smartphones/galaxy-s8/images/gallery/galaxy-s8-plus_gallery_right_side_coralblue_s4.png?$ORIGIN_PNG$'},
        {'id': 107, 'name': 'Redmi', 'price': 13000,
         'url': 'https://store.storeimages.cdn-apple.com/4974/as-images.apple.com/is/image/AppleInc/aos/published/images/i/ph/iphone/x/iphone-x-select-2017?wid=189&hei=376&fmt=png-alpha&qlt=95&.v=1504378258086'},
        {'id': 106, 'name': 'Samsung', 'price': 35000, 'url': 'http://images.samsung.com/is/image/samsung/p5/in/smartphones/galaxy-s8/images/gallery/galaxy-s8-plus_gallery_right_side_coralblue_s4.png?$ORIGIN_PNG$'},
        {'id': 105, 'name': 'Apple', 'price': 65000, 'url': 'https://store.storeimages.cdn-apple.com/4974/as-images.apple.com/is/image/AppleInc/aos/published/images/i/ph/iphone/x/iphone-x-select-2017?wid=189&hei=376&fmt=png-alpha&qlt=95&.v=1504378258086'},
        {'id': 108, 'name': 'Vivo', 'price': 20000, 'url': 'http://images.samsung.com/is/image/samsung/p5/in/smartphones/galaxy-s8/images/gallery/galaxy-s8-plus_gallery_right_side_coralblue_s4.png?$ORIGIN_PNG$'},
        {'id': 109, 'name': 'Apple', 'price': 75000, 'url': 'https://store.storeimages.cdn-apple.com/4974/as-images.apple.com/is/image/AppleInc/aos/published/images/i/ph/iphone/x/iphone-x-select-2017?wid=189&hei=376&fmt=png-alpha&qlt=95&.v=1504378258086'},
        {'id': 110, 'name': 'Samsung', 'price': 25000, 'url': 'http://images.samsung.com/is/image/samsung/p5/in/smartphones/galaxy-s8/images/gallery/galaxy-s8-plus_gallery_right_side_coralblue_s4.png?$ORIGIN_PNG$'},
        {'id': 111, 'name': 'Redmi', 'price': 10000, 'url': 'https://store.storeimages.cdn-apple.com/4974/as-images.apple.com/is/image/AppleInc/aos/published/images/i/ph/iphone/x/iphone-x-select-2017?wid=189&hei=376&fmt=png-alpha&qlt=95&.v=1504378258086'},
        {'id': 112, 'name': 'Vivo', 'price': 18000, 'url': 'http://images.samsung.com/is/image/samsung/p5/in/smartphones/galaxy-s8/images/gallery/galaxy-s8-plus_gallery_right_side_coralblue_s4.png?$ORIGIN_PNG$'},
    ])

print("Content-type:text/html\r\n\r\n")
print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <link rel="stylesheet" href="../../project_1/main.css">
</head>
<body>
<header id="header">
    <div class="logo">
        <h1>Company Logo</h1>
    </div>
    <nav>
        <ul>
            <li><a href="http://localhost:8000/project_1/">Home</a></li>
            <li><a href="../cgi-bin/e-comm/mobiles.py">Mobiles</a></li>
            <li><a href="#">Men</a></li>
            <li><a href="#">Women</a></li>
            <li><a href="#">Sign</a></li>
            <li><a href="#">Login</a></li>
        </ul>
    </nav>
</header>
    <h1>Mobiles</h1>
    <div id="content">
    <ul>
""")

for i in range(len(productList)):
    print("""
        <li>
            <h3>Id : {}</h3>
            <img src="{}" alt="">
            <h3>Name : {}</h3>
            <h4>Price : {}</h4>
        </li>
""".format(productList[i]['id'], productList[i]['url'],
           productList[i]['name'],productList[i]['price']))

print("""
    </ul>
    </div>
</body>
</html>
""".format())