# Shopwize Ecommerce Website

Shopwize is an ecommerce website that allows users to view products, place orders, and make payments. The platform provides a seamless shopping experience with various features and integrations.

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
