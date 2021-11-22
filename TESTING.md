# Immortal Fitness Collective Testing

- [Validation](#validation)
  - [W3 HTML](#w3-html)
  - [W3 CSS](#w3-css)
  - [JavaScript](#javascript)
  - [Python](#python)
  - [Google Lighthouse Audit](#google-lighthouse-audit)
- [Responsive Device & Browser Testing](#responsive-device--browser-testing)
  - [Responsiveness](#responsiveness)
  - [Browser Compatibility](#browser-compatibility)
- [Testing User Stories](#testing-user-stories)
- [Issues I had to overcome](#issues-i-had-to-overcome)
- [Issues still to overcome](#issues-still-to-overcome)

## Validation

### W3 HTML

I validated the HTML with [W3 Validation Service](https://validator.w3.org/). The results can be seen below;

<details>
<summary>base.html & home.html</summary>

![Base & Home](media/HTML-Home.PNG)

The validator shows an error for duplicate 'user-options' id, I've chosen to disregard this as one id is used on desktop, while the other is mobile. Both are required for bootstrap navigation dropdown to function properly.

The warning for 'type' javascript I have also chosen to disregard, as although unnecessary, it is useful for other developers to quickly see script code language.

I have filtered these errors and warnings for all other results.

</details>

<details>
<summary>about-us.html</summary>

![Base & Home](media/HTML-AboutUs.PNG)

</details>

<details>
<summary>Programme.html</summary>

![About Us](media/HTML-AProgramme.PNG)

</details>

<details>
<summary>Products.html</summary>

![Products](media/HTML-Products.PNG)

</details>

<details>
<summary>about-us.html</summary>

![Product Detail](media/HTML-ProductDetail.PNG)

The validator shows an error for 'data_item_id' attribute not being allowed on form input, however I have disregarded this, as it's used for django to identify the product being adjusted in the bag.

</details>

### W3 CSS

I validated the CSS with the [W3 Validation Service](https://jigsaw.w3.org/css-validator/) and it found no errors.

<details>
<summary>Base</summary>

![About Us](media/CSS-Base.PNG)

</details>

<details>
<summary>Profiles</summary>

![About Us](media/CSS-Profiles.PNG)

</details>
<details>
<summary>Checkout</summary>

![About Us](media/CSS-Checkout.PNG)

</details>

### JavaScript

I validated the JavaScript with [JSHint](https://jshint.com/).

<details>
<summary>countryfield.js</summary>

![script.js](media/JS-countryfield.PNG)
</details>

<details>
<summary>ratingstars.js</summary>

![script.js](media/JS-ratingstars.PNG)
</details>

<details>
<summary>Stripe.js</summary>

JSHint incorrectly identifies 'Stripe' as an undefined variable, however this is a variable used by Stripe and identified within their own scripts.

![script.js](media/stripe.PNG)
</details>

### Python

I validated the Python code was PEP 8 compliant via the [Pylint Validation Tool](https://www.pylint.org/) and [pycodestyle Validator](https://pypi.org/project/pycodestyle/), which found several simple errors I corrected.

All apps now received a score of over 9/10, any errors that do remain are either false-positives or superficial.

<details>
<summary>Home</summary>

![Home App](media/Python-home.PNG)
</details>

<details>
<summary>Immortal Fitness Collective</summary>

![IFC App](media/immortal_fitness_collective.PNG)
</details>

<details>
<summary>Bag</summary>

![Bag App](media/bag.PNG)
</details>

<details>
<summary>Checkout</summary>

![Checkout App](media/Python-checkout.PNG)
</details>

<details>
<summary>Products</summary>

![Products App](media/Python-products.PNG)
</details>

<details>
<summary>Profiles</summary>

![Profiles App](media/Python-profiles.PNG)
</details>

<details>
<summary>Workout Blog</summary>

![Workout Blog App](media/Python-workout_blog.PNG)
</details>

#### .pylintrc

After the above corrections, Pylint was still displaying a handful of warnings, however, these were false-positive results for the following reasons:

- import-outside-toplevel: This is flagging for the signal import in apps.py files, which is acceptable.
- unused-import, unused-argument and unused-variable: Flagging in various places, but all imports are required for method functionality.
- missing-module-docstring: Flagging on unused files automatically created by django, such as __init.py.
- invalid-name & unused-argument: 'e' is an accepted variable, used to capture errors in error handling functionality.
- 'env' is the local file used to configure the development environment, as it is not pushed to live via .gitignore, pylint incorrectly believes the function is not used.

To clean up these false positives, I created a .pylintrc file and added the below rules to allow for these warning instances.

<details>
<summary>.pylintrc</summary>

![Pylintrc App](media/Python-pylintrc.PNG)
</details>

### Google Lighthouse Audit

I used Google's lighthouse audit to test the website conforms positively with Google's performance metrics, with the intent to achieve scores of 90% in all areas on desktop.

![Google Lighthouse Audit Score](media/Google-Lighthouse-Audit.PNG)

This shows 90%+ scores for all metrics except for performance. Upon checking the reasoning for the low performance score I decided to take no further action for the below reasons:

<details>
<Summary>Performance</Summary>

![Performance Score](media/Google-Lighthouse-Audit-Performance.PNG)

The driving factors to the low-performance score are, 'Serve images in next-gen formats', 'Eliminate Render Blocking Resources' and 'Remove Unused JavaScript'. Due to Safari only recently adopting WebP compatibility, I chose to keep images as .jpg. The 'Render Blocking'Resources' and 'Remove Unused JavaScript', the sources driving these are external resources, such as Boostrap and jQuery. Therefore as the underlying cause is due to third party scripts, no further on-site optimisation is suitable.

</details>

## Responsive Device & Browser Testing

To test the responsiveness of the site I used [Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools), [Responsive Design Checker](https://www.responsivedesignchecker.com/) and [Lambdatest](https://www.lambdatest.com/).

### Responsiveness

![Desktop Responsive Testing](media/Responsive-Test-Desktop.PNG)

![Tablet Responsive Testing](media/Responsive-Test-Tablet.PNG)

![Mobile Responsive Testing](media/Responsive-Test-Mobile.PNG)

To ensure responsive design, I used bootstrap grid, flexbox, containers and custom media queries to ensure all site pages resized responsively for all mainstream device viewports.

### Browser Compatibility

![Browser Compatibility Testing](media/Responsive-Test-Browser.PNG)

The site does not load properly while using Internet Explorer, due to compatibility issues.

According to [caniuse](https://caniuse.com/usage-table) the current usage of Internet Explorer is 0.7% of total browser users, therefore I am comfortable not supporting IE in the site design.

Note: Microsoft released Internet Explorer in 2013 and ceased active development in 2015 when Microsoft Edge was released as the replacement, as evidenced by this article from Microsoft's design team. Since 2015 Microsoft has been actively encouraging users to adopt Edge over Explorer, with the only remaining updates for IE, being security patches and bug fixes.

## Testing User Stories


#### Browsing

- US101: Home Page has clear CTA leading customers to online shop, alongside clear content promoting both fitness programmes and merchanise.
- US102: Site is responsive for all major device view ports, maintaining all key functionality, whilst displaying content clearly and legibly.
- US103: Navigation is clearly accessible at all times via the sticky-top navigation bar on all pages and view ports.
- US104: Purchase History is easily accessible via accessing 'My Account' in top navigation menu.

#### Searching

- US201: Users can access product categories via links in top navigation menu.
- US202: User can access product details, via clicking on product card on catalogue page.
- US203: Users can search products by keyword, via use of 'Search' function in top navigation menu.
- US204: Users can sort products by rating via using the 'Sort By' function on product category page.
- US205: Users can sort products by price via using the 'Sort By' function on product category page.

#### Users

- US301: Users can register accounts through the sites allauth integration.
  - The site restricts information shown to users based on whether they are unregistered, registered, staff or admin.
- US302: The site uses django and allauth to ensure secure logins and access restrictions.
  - The site enforces HTTPS to ensure user communications and data are transmitted securely.
  - Passwords are stored in hashed form for additional security.
  - User accounts store personal user info, such as basic personal details and checkout information.
- US303: Allauth allows users to request a password reset via 'Forgot Password?' option on login screen.
- US304: Registered users can leave ratings and reviews of products via form submission on product detail page.

#### Administration

- US401: Admins are able to add, edit and delete workouts via the 'Workout Management' link in top navigation, 'Edit' and 'Delete' links on Workout Detail Pages.
- US402: Admins are able to add, edit and delete products via the 'Product Management' link in top navigation, 'Edit' and 'Delete' links on Product Detail Pages.
- US403: Admins can delete user reviews via 'delete' link on review posts.

#### Purchasing and Checkout

- US501: Users can easily select products to add to basket via product catalogue page and adjust the amount via product detail page.
- US502: Users can review their basked contents via the 'bag' page, prior to checkout.
- US503: Users can adjust amount of a product in their basket, via the amount selection input in the 'bag' page.
- US504: Users can input their payment details via the stripe elements payment integrations on the checkout page.
- US505: Checkout is supported by secure stripes secure payment platform.
- US506: After checkout a success page is presented, giving the user details of their order and notification of e-mail confirmation.
- US507: After checkout an email is generated with the order information.

#### General

- US601: To ensure users receive positive or negative feedback for their actions, confirmation pages and bootstrap toast messages are used extensively throughout the site.

&nbsp;

## Issues I had to overcome

## Issues still to overcome
