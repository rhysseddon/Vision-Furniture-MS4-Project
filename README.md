# Vision Furniture

## Contents

* [Purpose](#Purpose)
* [User Stories](#User-Stories)
* [UX](#UX)
    * [Strategy](#Strategy)
    * [Scope](#Scope)
    * [Structure](#Structure)
    * [Database Schema](#Database-Schema)
    * [Skeleton](#Skeleton)
    * [Wireframes](#Wireframes)
    * [Surface](#Surface)
* [Features](#Features)
    * [Implemented Features](#Implemented-Features)
    * [Features To Add Later](#Features-To-Add-Later)


# Purpose

Vision Furniture is an e-commerce store selling stylish vintage furniture, where people can shop for furniture from the comfort 
of their own home.
The website is entirely fictional and was created for my fourth milestone project for a software development course I am undertaking 
at the code institute.

# User Stories

### New User

As a new user of the site a want to be able to:  
1.	Browse all products – to gain some inspiration on what to buy.
2.	Sort order of products – to find the cheapest or most expensive products.
3.	Find products that go in a particular room.
4.	View details of a product – like price, delivery costs and product dimensions.
5.	Be able to view a total cost of a potential multiple purchase.
6.	Be able to search for a specific product.

### Returning User

As a returning user to the site, I would like to:  
1.	Easily register my details – to create a profile for my personal details.
2.	Be able to view my previous purchases.
3.	Edit my personal details on my profile.
4.	Be able to contact the company regarding a previous purchase.  

### Staff User 

As a member of staff, I need to be able to:
1.	Easily add, update and delete products.
2.	Easily view, update and delete customer orders.

# UX

## Strategy

The world has changed a lot in 2020/21, property sales have sharply risen, and people are spending more time at home hence a high demand 
for furniture. Online shopping has also increased significantly which is a trend which is expected to remain.  
Through the rise of Instagram and other social media sites people now have many interior design ideas at their fingertips and 
the “Vintage” theme is particularly popular. For these reasons, a new vintage style furniture store website is positioned to do very 
well at this current time.

### Research

I researched 3 e commerce furniture stores - [Johnlewis.com](https://Johnlewis.com), [MADE.com](https://made.com) and [Habitat.co.uk](https://Habitat.co.uk):

-	All had a similar navbar layout - logo on the left, search bar in the middle, profile and checkout on the right.
-	All had a mainly black and white theme which accentuated the colours of the products in the pictures.
-	Products were all laid out in a grid format.
-	To give their customers inspiration MADE had an “ideas” area, showing images of impressively designed rooms containing their products, 
if you click on the images you can see the products with the product descriptions.
-	Habitat had a “new in” section where customers can see recently added products.
-	All had a shop by room menu, containing Living room, dining room, bedroom, kitchen, office and bathroom.
-	John Lewis and Habitat had customer reviews for each product.
-	Made and John Lewis had a favourites or wish list feature for customers to save products without adding to their basket. 

## Scope 

Based upon the strategy and research,  some design features that I aim to include are:
-	Search bar for customers to search for an item that they are looking for.
-	Shop by room menu which takes the customer to products for a specific room they are looking to furnish. 
-	A shopping bag for customers to add their products and see what the total charges will come to.
-	A “new in” area for the customers to see if there are any new products on the site since they last visited.
-	Profile page for customers to save their delivery details and see their previous orders.
-	Contact us or About section for customers to query anything which is not covered on the website itself.
-	FAQ section to save on admin time replying to customer queries and to streamline the user experience.
-	On each product page the ability to sort the products by name (A-Z) or price (high to low).
-	A favourites feature for customers to save a product to their profile - if they are not ready to buy but 
wish to save the product for a future purchase.  

For now, I will not be including:
-	Ideas area. For the customers to gain inspiration from seeing the products in a room together. 
With an icon on each product that will link to the page showing the details of that product. Can be added in future 
once the minimum viable product has been built and the website is generating money.
-	Product reviews. Could possibly be added in future, more research required on how to regulate the reviews. 

### Structure

-	The site will be structured in a linear format keeping the users’ expectations as the main priority.
-	The site will have a similar layout to the websites I’ve researched, so the customers will not need to “re-learn” how 
to navigate a website and keep their user experience as streamlined as possible with minimal frustration.
-	The layout will be similar across all pages to keep a consistent and clean UX.

### Database Schema

### Skeleton

### Wireframes

<details>
<summary>Home (Click for images)</summary>
<p align="center">

![Image](readme-images/wireframes/home-wireframes.png)
</p>
</details>

<details>
<summary>Product Pages  (Click for images)</summary>
<p align="center">

![Image](readme-images/wireframes/products-wireframes.png)
</p>
</details>

<details>
<summary>Profile (Click for images)</summary>
<p align="center">

![Image](readme-images/wireframes/profile-wireframes.png)
</p>
</details>

<details>
<summary>Login (Click for images)</summary>
<p align="center">

![Image](readme-images/wireframes/login-wireframes.png)
</p>
</details>

<details>
<summary>Register (Click for images)</summary>
<p align="center">

![Image](readme-images/wireframes/register-wireframes.png)
</p>
</details>

<details>
<summary>Shopping Bag (Click for images)</summary>
<p align="center">

![Image](readme-images/wireframes/shopping-bag-wireframes.png)
</p>
</details>

<details>
<summary>Checkout (Click for images)</summary>
<p align="center">

![Image](readme-images/wireframes/checkout-wireframes.png)
</p>
</details>

<details>
<summary>Checkout Success (Click for images)</summary>
<p align="center">

![Image](readme-images/wireframes/checkout-success-wireframes.png)
</p>
</details>

<details>
<summary>Admin Add Products (Click for images)</summary>
<p align="center">

![Image](readme-images/wireframes/admin-add-wireframes.png)
</p>
</details>

<details>
<summary>Admin Edit Products (Click for images)</summary>
<p align="center">

![Image](readme-images/wireframes/admin-edit-wireframes.png)
</p>
</details>

<details>
<summary>Help Centre (Click for images)</summary>
<p align="center">

![Image](readme-images/wireframes/help-wireframes.png)
</p>
</details>


# Features

## Existing Features

### Navbar

-	All pages will contain the navbar.
-	Vision furniture logo on left side next to all products and shop by room link.
-   All products link will link to all products page.
-   Shop by room will be a full width dropdown with links to bedroom, dining room, bathroom, living room, kitchen
and office product pages.
-   Search bar in centre of navbar which will allow customers to search for keywords found in product names or descriptions.
-   Right hand logos will feature links to favorites page, my account pages and cart page.
-   Favorites link will only be visible to logged in users.
-   My account when logged in as superuser will dropdown links to product admin, help admin, my profile and logout.
-   My account when logged in as user will dropdown links to my profile and logout.
-   My account when not logged in will dropdown links to register and login.
-   In tablet view or smaller all links will be contained in a burger dropdown icon on the right side and the search 
bar will be below the navbar full width.


<details>
<summary>Navbar (Click for image)</summary>
<p align="center">

![Image](readme-images/navbar-screenshot.png)
</p>
</details>

### Footer

-   All page will contain the same Footer.
-   Social media links on left, to Facebook, Instagram and Twitter.
-   Link to help centre page on right, displaying "Need Help".

<details>
<summary>Footer (Click for image)</summary>
<p align="center">

![Image](readme-images/footer-screenshot.png)
</p>
</details>

### Home Page

- A full height and width background furniture image.
- A central title "Vision Furniture" and below "refresh your space".
- A central "view our stock" button linking to all products page"

<details>
<summary>Footer (Click for image)</summary>
<p align="center">

![Image](readme-images/home-screenshot.png)
</p>
</details>

### Product Pages

- Displaying all products or a specific products from each room, depending on where the user has linked from.
- Central title informing what products are displaying.
- Below a graphic will display underlining the title.
- Below on the left will display the number of product displaying.
- On the right will be a dropdown menu for the user to sort products by:
    - Price (low to high)
    - Price (high to low)
    - Name (A-Z)
    - Name (Z-A)
- Below will display a grid containing each product. The grid will display 3 items on each row on tablet or larger
and 1 item per row on mobile.
- Each item will display the product image, product name, product price and a button to view further details of the 
item.
- An edit and delete link will display for superusers, edit link will take the superuser to the edit product page and
delete will remove the item.

<details>
<summary>Products (Click for image)</summary>
<p align="center">

![Image](readme-images/products-screenshot.png)
</p>
</details>

### Product Detail Page

- Will display a box containing product image on the left and information on the right, and in mobile view product 
image at the top and below the product information.
- Product information will include title with the name of the product, product price, product description,
product dimensions, delivery cost, a form to increment / reduce quantity and buttons to "add to cart", "keep shopping" and
add to favorites (heart icon).
- For super users below the title links will display for superusers, edit link will take the superuser to the edit product page and
delete will remove the item.

<details>
<summary>Product Detail (Click for image)</summary>
<p align="center">

![Image](readme-images/product-detail-screenshot.png)
</p>
</details>

### Profile Page

- Profile page will only be accessible for logged in users.
- Will display the central heading "My Profile".
- Below a graphic will display underlining the title.
- Subheading below displaying "Your delivery Information"
- Below will be a central django crispy form, which will be prefilled if the user has ticked the "save this 
information to my profile" checkbox on the checkout page. The form will contain:
    - Phone number
    - Street address 1
    - Street address 2
    - Town or city
    - County
    - Postcode
    - Country (dropdown)
- Central button "Update information"
- Suheading "Order history"
- A table containing the users previous orders.
- The columns for the table will be order number, date, items and order total.

<details>
<summary>Profile (Click for image)</summary>
<p align="center">

![Image](readme-images/profile-screenshot.png)
</p>
</details>

### Cart Page

- Displaying all products that have been added to cart.
- Central title "Shopping cart"
- Below a graphic will display underlining the title.
- A table containing the users products added to cart.
- The columns for the table will be product info, price, quantity and total.
- Product info will contain the product name and image.
- Quantity will be a form to increment / reduce quantity.
- Total will be product price multiplied by quantity.
- At the bottom of the table will be delivery (calculated using delivery policy)
- A link to the delivery policy on the help centre page.
- Subtotal which will be total of all the items plus delivery cost.
- Grand total will be delivery plus subtotal.
- Below buttons to "keep shopping" and to secure checkout"
- If there are no items in the cart, a subheading will display "Your cart is empty" and a "keep shopping" button.

<details>
<summary>Cart (Click for image)</summary>
<p align="center">

![Image](readme-images/profile-screenshot.png)
</p>
</details>

### Checkout

- Central title "Checkout"
- Below a graphic will display underlining the title.
- I if the user is not registered or logged in, "Register / Login now to save your delivery information and order history"
will display and buttons to link to register and log in pages. Below will display - "In a hurry? Checkout below"
- In laptop and tablet delivery information will be a left column and order summary on the right.
- In mobile view Order summary will display above delivery information.
- Delivery information will be form with a subheading "Details" and containing name and email address and
 below a crispy form with the heading "Delivery" and the fields:
    - Phone number
    - Street address 1
    - Street address 2
    - Town or city
    - County
    - Postcode
    - Country (dropdown)
- If the user is a logged in user, at the bottom of the form will display "Save this delivery information to my profile" with a checkbox, when the user
ticks the checkbox the delivery information will be saved to their profile. 
- Below a stripe payment field will display a button to "adjust cart", which will take user back to cart page and "Complete order"
which will send payment to stripe.
- Below buttons will display "Your card will be charged (amount)"
- The order summary will display subheading of "Order Summary" and will display the information:
    - Product image
    - Product name
    - Quantity
    - Item total
    - Subtotal
    - Delivery
    - Grandtotal

<details>
<summary>Checkout (Click for image)</summary>
<p align="center">

![Image](readme-images/checkout-screenshot.png)
</p>
</details>

### Checkout Success

- Central title "Thankyou!"
- Below a graphic will display underlining the title.
- Display "A confirmation email will be sent to (users email address)"
- A box containing a table of: 
    - Order info: order number and date.
    - Order details: product names, quantity and price.
    - Delivering to: user name, address and phone number.
    - Billing Info: order total, delivery and grand total.
- Central button "Return to shop" which will return user to all products page.


<details>
<summary>Checkout Success(Click for image)</summary>
<p align="center">

![Image](readme-images/checkout-success-screenshot.png)
</p>
</details>

### Admin Add / Edit Products

- Add / Edit product page will be the same layout.
- Only accessible as superuser.
- Will edit or add products that user enter into form.
- Central title "Product Administration"
- Below a graphic will display underlining the title.
- Subheading Add / Edit Product
- Central form containing:
    - Room 
    - Sku
    - Name
    - Description
    - Price
    - Delivery cost
    - Depth
    - Height
    - Width
    - Image
- Edit page will display the current image.
- Both will display a button to "Select Image".
- Edit page with display central buttons "Cancel" and "Update"
- Add page with display central buttons "Cancel" and "Add Product"

<details>
<summary>Product Admin(Click for image)</summary>
<p align="center">

![Image](readme-images/product-admin-screenshot.png)
</p>
</details>




