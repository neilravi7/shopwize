# Shopwize Ecommerce Website

Shopwize is an ecommerce website that allows users to view products, place orders, and make payments. The platform provides a seamless shopping experience with various features and integrations.

# Screenshots

**Product Listing Page**

![Screenshot 2023-12-02 211305](https://github.com/neilravi7/shopwize/assets/63995407/3fab846f-6fbd-45ce-85ee-9ece4ab6350e)

**Product Detail Page**

![Screenshot 2023-12-02 211331](https://github.com/neilravi7/shopwize/assets/63995407/38cfea27-90df-4dad-a6d4-a916d5dd9f62)

**Cart Items**

![Screenshot 2023-12-02 211534](https://github.com/neilravi7/shopwize/assets/63995407/cdf0630e-55ae-4e84-a604-d71ac241c30b)

**Checkout and Pay**

![Screenshot 2023-12-02 212007](https://github.com/neilravi7/shopwize/assets/63995407/622e5b59-8062-44a6-8a1b-8182d5a12ee0)
![Screenshot 2023-12-02 211946](https://github.com/neilravi7/shopwize/assets/63995407/0afdd09c-446e-4f60-967a-2673f47dd7d7)

**Profile And Orders**

![Screenshot 2023-12-02 212117](https://github.com/neilravi7/shopwize/assets/63995407/7d74980a-cad7-444e-866a-df388a1d6fe7)

## Features

1. **User Authentication and Profiles:**
   - Create user accounts
   - Log in to existing accounts
   - Update user profiles
   - View and manage user profile details

2. **Order Management:**
   - View multiple orders
   - View detailed order information

3. **Product Management:**
   - Admin panel for managing products
   - Add new products to the site
   - View, update, and delete products

4. **Media File Storage:**
   - Utilize AWS S3 bucket for storing media files
   - Efficiently manage and serve images and media content

5. **Payment Gateway Integration:**
   - Integrate with Stripe and PayPal for secure online payments
   - Provide users with multiple payment options

## Installation and Setup

# 1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/shopwize.git
   # Navigate to the project directory
   cd shopwize
   pip install -r requirements.txt
   # 2. Set up environment variables for AWS S3, Stripe, and PayPal configurations.
   # 3. Run database migrations
   python manage.py migrate
   # 4. Launch the development server:
   python manage.py runserver
   # Access the website at http://localhost:8000.
