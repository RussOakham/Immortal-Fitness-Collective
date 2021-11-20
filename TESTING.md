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

The dalidator shows an error for duplicate 'user-options' id, I've chosen to disregard this as one id is used on desktop, while the other is mobile. Both are required for bootstrap navigation dropdown to function properly.

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

### Python

I validated the Python code was PEP 8 compliaint via the [Pylint Validation Tool](https://www.pylint.org/) and [pycodestyle Validator](https://pypi.org/project/pycodestyle/) within GitPod, which found several simple errors I corrected.

### Google Lighthouse Audit

I used Google's lighthouse audit to test the website conforms positively with Google's performance metrics, with the intent to achieve scores of 90% in all areas on desktop.

## Responsive Device & Browser Testing

To test the responsiveness of the site I used [Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools), [Responsive Design Checker](https://www.responsivedesignchecker.com/) and [Lambdatest](https://www.lambdatest.com/).

### Responsiveness

![Desktop Responsive Testing]()

![Tablet Responsive Testing]()

![Mobile Responsive Testing]()

### Browser Compatibility

![Browser Campatibility Testing]()

Additionally, the site does not load properly while using Internet Explorer, due to compatibility issues.

According to [caniuse](https://caniuse.com/usage-table) the current usage of Internet Explorer is just 0.9% of total browser users, therefore I am comfortable not supporting IE in the site design.

Note: Microsoft released Internet Explorer in 2013 and ceased active development in 2015 when Microsoft Edge was released as the replacement, as evidenced by this article from Microsoft's design team. Since 2015 Microsoft has been actively encouraging users to adopt Edge over Explorer, with the only remaining updates for IE, being security patches and bug fixes.

## Testing User Stories

<
&nbsp;

## Issues I had to overcome

## Issues still to overcome
