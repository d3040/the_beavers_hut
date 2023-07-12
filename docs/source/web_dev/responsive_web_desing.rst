Responsive Web Design[#]_
=========================

* Only use one h1 element per page and place lower importance headings below higher important headings.
* All img elements should have an alt attribute. It is used for screen readers to improve accessibility and is displayed if the image fails to load.
* The ``figure``element represents sel-contained content and will allow you to associate an image with a caption.
* The default behaviour of clicking a form button without any attributes submits the form to the location specified in the form's ``action`` attribute. To avoid confusion add the ``type`` attribute with the value 'submit' on the button to make it clear that it is a submit button.
* label elements are used to help associate the text for an ``input`` element with the ``input`` element itsel (especially for assistive thecnologies like screen readers).
* To make a unique selection in a group of radio buttons, the buttons must have a ``name`` attribute with the same value.
* ``fieldset `` element is used to group related inputs and labels together in a web form.
* The ``legend`` element acts as a caption for the content in the ``fieldset`` element. It gives users context about what they should enter into that part of the form.
* Another way to associate an ``input`` element's text with the element itself is using a ``label`` element and a ``for`` attribute with the same value as the ``input`` element's ``id`` attribute.
* Form data for selected checkboxes are ``name`` / ``value`` attribute pairs. While the ``value`` attribute is optional, it's best practice to include it with any checkboxes or radio buttons on the page.
* Add a ``lang`` attribute to the ``head`` element in order to stablish a laguage for the website.
* All pages should begin with <!DOCTYPE html>. This special string is known as a declaration and ensures the browser tries to meet industry-wide specifications. 
* The ``title`` is one of several elements that provide extra information not visible on the web page, but it is useful for search engines or how the page gets displayed. It aslo displays the content of that ``title`` elemet in 2 ways:
	+ in the title bar when the page is open,
	+ in the browser tab for the page when you hover on it. Even if that tab is not active, once you hover on the, the ``title`` text is displayed.

* For the styling of a page to look similar on mobile as it does on a desktop or laptop, need to add: ``<meta name="viewport" content="width=device-width, initial-sclae=1.0" />``.
* The inline-blcok element only take up the width of their content.
* One enter alter the position of the elements (E.g. Step 41 Responsive Web Desing Lear Basic CSS by Building a Cafe Menu).
* The deaful color of a link that has not yet been clicked on is typically blue. The default color of a link that has alreaduy been visited from a page is typically purple. This can be change by applying the color property to the anchor tag (a).
* There ar two main color models: the additive RGB (red, gree, blue) model used in electronic devices, and the substractive CMYK /cyan, magenta , yellow, black) model used in print.
	+ Primary colors: basic at they maximum.
	+ Secondary colors: the color you get when combine primary colors. Cyan, Magenta, Yellow.
	+ Tertiary colors are created combining a primary with a nearby secondary color.
* A color wheel is a circle where similar colors, or `hues`, are near each other, and different ones are further apart. Two colors that are opposite from each other on the color wheel are called complementary colors. If two complementary colors are combined, the produce gray. But when they are placed side-by-side, these colors produce strong visual contrast and appear brighter.
* It's better practice to choose one color as the dominant color, and use its complementary color as an accent to bring attention to certain content on the page.
* There are several other important color combinations outside of complementary colors.
* ``HEX color`` values start with a # characgter and take six characters from 0-9 and A-F. The first pair of characters represent red, the second pair represent green, and the third pair represent blue.
* The ``HSL`` color model, or hue, saturation and lightness, is another way to represent colors. The CSS hsl function accepts 3 values: a numbre from 0 to 360 for hue, a percentage from 0 to 100 for saturation, and a percengage from 0 to 100 for lightness. If you imagine a color wheel, the hue red is at 0 degress, green is at 120 degreses, and blue is at 240 degrees. Saturation is the intensity of a color from 0%, or gray, to 100% for pure color. The % sign must be added to the saturation and lightness values. Lightness is how bright a color appears, from 0%, or complete black, to 100%, complete white, with 50% being neutral.
* A gradient is when one color transitions into another. The CSS ``linear-gradient`` funtion lets you control de direction of the transition along a line, and which colors are used. One thing to remember is that the ``linear-gradient`` funtcion actually creates an ``image`` element, and i usually paired with the background property which can accept an image as a value.
* If you want a value of zero (0) for any or both offsetX and offsetY, you don't need to add a unit. Every browser understands that zero means no change.
* rem: unit stands for root em, and is also relative to the font size of the html element.
* Give width of "unset" in order to remove previous rules.
* Attribute selector: selects an element based on the given attribute value (e.g. input[name="password"]).


Basic html template:

``` html

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Colored Markers</title>
  </head>
  <body>
  </body>
</html>

```


Registration form:
------------------

* Atributes form element:
	- action: where from data should be sent.
	- method: specifies how send form-data to the URL specified in the action attribute.
		+ GET request: 
		+ POST request: 
* Elements:
	- fieldset:
	- label:
		+ for 
	- input (self-closing):
		+ id
		+ type
		+ name
		+ placeholder
		+ required
- To handle the form submission, after the last ``fielset`` element add an ``input``element with the ``type`` attribute set to "submit" and the ``value``attribute set to "Submit".
- To every input element add a ``name`` attribute.
- During development, it is useful to see the fieldset default borders.

``` html

<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <title>Registration Form</title>
    <link rel="stylesheet" href="styles.css" />
  </head>
  <body>
    <h1>Registration Form</h1>
    <p>Please fill out this form with the required information</p>
    <form method="post" action='https://register-demo.freecodecamp.org'>
      <fieldset>
        <label for="first-name">Enter Your First Name: <input id="first-name" name="first-name" type="text" required /></label>
        <label for="last-name">Enter Your Last Name: <input id="last-name" name="last-name" type="text" required /></label>
        <label for="email">Enter Your Email: <input id="email" name="email" type="email" required /></label>
        <label for="new-password">Create a New Password: <input id="new-password" name="new-password" type="password" pattern="[a-z0-5]{8,}" required /></label>
      </fieldset>
      <fieldset>
        <label for="personal-account"><input id="personal-account" type="radio" name="account-type" class="inline" /> Personal Account</label>
        <label for="business-account"><input id="business-account" type="radio" name="account-type" class="inline" /> Business Account</label>
        <label for="terms-and-conditions">
          <input id="terms-and-conditions" type="checkbox" required name="terms-and-conditions" class="inline" /> I accept the <a href="https://www.freecodecamp.org/news/terms-of-service/">terms and conditions</a>
        </label>
      </fieldset>
      <fieldset>
        <label for="profile-picture">Upload a profile picture: <input id="profile-picture" type="file" name="file" /></label>
        <label for="age">Input your age (years): <input id="age" type="number" name="age" min="13" max="120" /></label>
        <label for="referrer">How did you hear about us?
          <select id="referrer" name="referrer">
            <option value="">(select one)</option>
            <option value="1">freeCodeCamp News</option>
            <option value="2">freeCodeCamp YouTube Channel</option>
            <option value="3">freeCodeCamp Forum</option>
            <option value="4">Other</option>
          </select>
        </label>
        <label for="bio">Provide a bio:
          <textarea id="bio" name="bio" rows="3" cols="30" placeholder="I like coding on the beach..."></textarea>
        </label>
      </fieldset>
      <input type="submit" value="Submit" />
    </form>
  </body>
</html>

```



	self-closing tags:
		* img
		* input




.. [#] `FreeCodeCamp - Responsive Web Desing <https://www.freecodecamp.org/learn/2022/responsive-web-design/>`_

