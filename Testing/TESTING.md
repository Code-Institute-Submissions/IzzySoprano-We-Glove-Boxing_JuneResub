## Table of Contents ##

- [We Glove Boxing Testing Details](#we-glove-boxing-project-testing-details)
  - [Automated Testing](#automated-testing)
    - [Validation Services](#validation-services)
  - [Manual Testing](#manual-testing)
    - [Testing undertaken on desktop](#testing-undertaken-on-desktop)
    - [Testing From User Stories](#testing-from-user-stories)
  - [Bugs discovered](#bugs-discovered)

---
## Automated Testing ##

### Validation Services ###

The following **validation services** and **linters** were used to check the validity of the website code.

- [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/)
  - This validator checks the validity of cascading style sheets (CSS) and (X)HTML documents with style sheets.
  - All CSS files passed the validation service.

    ![W3c CSS Results Image](Testing/Validator/css.png)

- [W3C Markup Validator](https://validator.w3.org/)
  - This validator checks the markup validity of Web documents in HTML

  - Home:

    ![W3c Markup Validator](/Testing/Validator/home.png)

  - Product Page:

    ![W3C Markup Results image](Testing/Validator/products-page.png)

  - Add Product:

    ![W3C Markup Results image](Testing/Validator/products-add.png)

  - Edit Product:

    ![W3C Markup Results image](Testing/Validator/edit-product.png)

  - Bag:

    ![W3C Markup Results image](Testing/Validator/bag.png)

  - Profile:

    ![W3C Markup Results image](Testing/Validator/profile.png)

  - Register:

    ![W3C Markup Results image](Testing/Validator/register.png)

  - Login:

    ![W3C Markup Results image](Testing/Validator/login.png)

---
## Manual Testing ##

### Testing undertaken on desktop ###

- Hardware:
    - Dell 15 XPS Laptop
- Tested Operating Systems:
    - Windows 10
- Tested Browsers:
    - Windows 10:
        - Chrome
        - Edge 

### Testing undertaken on phone devices ###

- Hardware:
    - iPhone 8 Plus
    - iPhone 11 Pro
- Tested Operating Systems:
    - iOS 15.4
- Tested Browsers:
    - iOS
        - Safari

---
### Testing From User Stories

### **User Stories**

#### Viewing and Navigation

- As a **shopper**, I want to be able to view a list of products so that I can choose some items to purchase.

  All users, regardless of registered/logged in status, can browse through all products, add to bag and make a purchase:

---

- As a **shopper**, I want to be able to filter products that I am interested in without searching through all the products.

  Users are able to filter the specific product they want through the navbar

---

- As a **shopper**, I want to be able to select individual products to see more detailed information and add the item to my shopping cart.

  Users are able to click on the product they want to purchase and have the product information displayed 

---

- As a **shopper**, I want to be able to see items I have placed in my shopping cart easily so that I can keep track of what I am buying

  Users are able to have the product they have added to their shopping bag

--- 

-As a **shopper**, I want to be able to see breadcrumb navigation links to see where I am on the site easily.

  The navbar I have included includes a breadcrumb navigation to allow the sub categories to be displayed

---

#### Registration and User Accounts 

- As a **site user**, I want to be able to register for an account to make future purchases easier

  Users are able to register

---

- As a **site user**, I want to be able to easily log in and out of my account so that I can access my personal account information

  Users are able to login 

---

- As a **site user**, I want to be able to log in and have a personal profile page containing order history

  Once users make a purchase, they can view they purchase history 

---

#### Sorting and Searching 

- As a **shopper**, I want to be able to sort the available products by price, category product type

  Users are able to filter the products based on clothing, footwear, clothing, protection, boxing fitness and accessories

---

- As a **shopper**, I want to be able to filter and group products for men, women or kids.

  The navbar includes a Men, Women and Kids section in the Clothing section. I only wanted to include clothing for women and kids and have the rest of the boxing related products as unisex.

---

- As a **shopper**, I want to be able to search for a product by name, type or category.

  The site includes a search bar that allows the user to search for products

---

#### Purchasing and Checkout 

- As a **shopper**, I want to be able to view the items in my shopping cart waiting to be purchased, seeing the grand total amount.

  The user can purchase products that are in the shopping bag and it displays the total amount 

---

- As a **shopper**, I want to be able to easily update the items in the shopping cart by changing the quantities of products or remove them from the cart.

  The user can modify the quantity of the products they've added to the shopping cart

---

- As a **shopper**, I want to be able to checkout securely where I can enter my delivery and credit card payment details with confidence.

  The user can securely pay for the products using Stripe payments (Demonstration purposes only)

#### Admin and Store Management

- As a **store owner**, I want to be able to add new products to my store

  I am able to login into my admin and modfiy products such as adding and deleting.

---

- As a **store owner**, I want to be able to edit / update the current product details and replace the product image file

  I am able to login and modify all prducts in my admin

---

- As a **store owner**, I want to be able to delete a product that is no longer for sale.

  I am able to add and delete products via my admin page

---
## Bugs Overview ##

In doing this project, I learned a lot. I encountered numerous bugs which I've tried to log to my README as much as possible. 

The major setback I kept having was that I struggled to transfermy SQLite database to my deployed Heroku PosGreSQL. Everytime I deployed to Heroku, I had to catergorise my products in the admin. Considering I have 120 products, I felt I should of learned the necessary commands to do so. For future, I need to understand migrating, loading data, dump data a lot more.

Another bug I had to overcome was at one point, as I staretd a new workspace, my static files weren't loading. With the help of my mentor and tutor, support I figured it was due to the paths needed to be changed from MEDIA to STATIC

  ![Static files not loading](Testing/images.png)

Another bug I came across was whilst correcting my DEBUG, My deployed link wasn't working. Thankfully with tutor support adnd the slack community, I was able to solve this issue.

  ![No Django table](Testing/django_session.png)
