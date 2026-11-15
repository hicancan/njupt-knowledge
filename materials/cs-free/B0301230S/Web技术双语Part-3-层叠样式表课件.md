---
title: 《Web技术（双语）》Part 3 层叠样式表（课件）
kind: 课件
course: Web技术（双语）
source: https://github.com/NJUPTFreeExams/NJUPT-CS-FREE/blob/main/%E3%80%90B0301230S%E3%80%91Web%E6%8A%80%E6%9C%AF%28%E5%8F%8C%E8%AF%AD%29/PPT_hjy%E5%BD%95%E9%9F%B3%E7%89%88/part3-css-voice.pptx
---

# 《Web技术（双语）》Part 3 层叠样式表（课件）

原件的每一页，下面附识别出的文字。

### Part 3 Cascading Style Sheets

![第 1 页](Web技术双语Part-3-层叠样式表课件.assets/第1页.webp)

原文：

Part 3 Cascading Style Sheets

PEARSON Addison Wesley

Programming the World Wide Web

### Content

![第 2 页](Web技术双语Part-3-层叠样式表课件.assets/第2页.webp)

原文：

Content

• 3.1 Introduction
• 3.2 Levels of style sheets
• 3.3 Style specification formats
• 3.4 Selector forms
• 3.5 Property values forms
• 3.6-3.12 All kinds of properties
Programming the World Wide Web

### 3.1 Introduction (pp.96)

![第 3 页](Web技术双语Part-3-层叠样式表课件.assets/第3页.webp)

原文：

3.1 Introduction (pp.96)

• CSS provides the means to control and change presentation of HTML documents.

• Style sheets allow you to impose a standard style on a whole document, or even a whole collection of documents.

• CSS is not technically HTML, but can be embedded in HTML documents

Programming the World Wide Web

2-3

### 3.2 Levels of Style Sheets (pp.97)

![第 4 页](Web技术双语Part-3-层叠样式表课件.assets/第4页.webp)

原文：

3.2 Levels of Style Sheets (pp.97)

There are three levels of style sheets:

• Inline level - specified for a specific occurrence of a tag and apply only to that tag.

• Document level - apply to the whole document in which they appear.

• External level - can be applied to any number of documents.

When more than one style sheet applies to a specific tag in a document, the lowest level style sheet has precedence.

Programming the World Wide Web

### 3.2 Levels of Style Sheets

![第 5 页](Web技术双语Part-3-层叠样式表课件.assets/第5页.webp)

原文：

3.2 Levels of Style Sheets

• Inline style sheets appear in the tag itself <p style="color: red">inline style sheet</p>

• Document-level style sheets appear in the head of HTML document <style type="text/css"> p{color: red; font-weight: bold} </style>

• External style sheets are in separate files on any server of the Internet

• Written as text files

• Named with the suffix .css

Programming the World Wide Web

### 3.2 Levels of Style Sheets

![第 6 页](Web技术双语Part-3-层叠样式表课件.assets/第6页.webp)

原文：

3.2 Levels of Style Sheets

• A <link> tag is used to specify that the browser is to fetch and use an external style sheet file.

• Example 3-external.html

Programming the World Wide Web

2-6

### • Inline level:

![第 7 页](Web技术双语Part-3-层叠样式表课件.assets/第7页.webp)

原文：

3.3 Style specification formats-Inline level

Format depends on the level of the style sheet!

• Inline level:

• Style sheet appears as the value of the style attribute of a tag

• General form:

• Example 3-inline.html

Programming the World Wide Web

### • Document level:

![第 8 页](Web技术双语Part-3-层叠样式表课件.assets/第8页.webp)

原文：

3.3 Style specification formats-Document level

• Document level:

• Style sheet appears as a list of rules that are the content of a <style> tag

• The <style> tag must include the type attribute, setting to "text/css“

Programming the World Wide Web

2-8

### • General form:

![第 9 页](Web技术双语Part-3-层叠样式表课件.assets/第9页.webp)

原文：

3.3 Style specification formats-Document level

• General form:

<style type = "text/css"> rule list

</style>

• Form of the rules:

selector {list of property/values}

• Each property/value pair has the form

property : value

• Pairs are separated by semicolons, just as in the value of a <style> attribute of inline level.

• Example 3-document.html

Programming the World Wide Web

### • Example 3-external.html

![第 10 页](Web技术双语Part-3-层叠样式表课件.assets/第10页.webp)

原文：

3.3 Style specification formats-External level

• It is a list of style rules, as in the content of a <style> tag for document-level style sheets

• But the rules are in a separate file which is named with the suffix .css.

• Example 3-external.html

Programming the World Wide Web

### 3.4 Selector Forms (pp.99)

![第 11 页](Web技术双语Part-3-层叠样式表课件.assets/第11页.webp)

原文：

3.4 Selector Forms (pp.99)

3.4.1 simple selector forms
3.4.2 class selectors
3.4.3 generic selectors
3.4.4 id selectors
3.4.5 contextual selectors
3.4.6 pseudo class
3.4.7 universal selectors

Programming the World Wide Web

2-11

### 3.4.1 Simple selector form

![第 12 页](Web技术双语Part-3-层叠样式表课件.assets/第12页.webp)

原文：

3.4.1 Simple selector form

The selector is a tag name or a list of tag names, separated by commas.

h1, h3 {font-size:30pt}

p {font-size:20pt}

Programming the World Wide Web

### 3.4.2 Class selectors

![第 13 页](Web技术双语Part-3-层叠样式表课件.assets/第13页.webp)

原文：

3.4.2 Class selectors

• It allows different occurrences of the same tag to use different styles.

• A style class has a name, which is attached to a tag name.

p.narrow {property/value list}

p.wide {property/value list}

• The class you want on a particular occurrence of a tag is specified with the class attribute of the tag

• For example:

Programming the World Wide Web

### 3.4.3 Generic selectors

![第 14 页](Web技术双语Part-3-层叠样式表课件.assets/第14页.webp)

原文：

3.4.3 Generic selectors

• A generic class can be defined if you want a style to apply to more than one kind of tags.

• A generic class must be named, and the name must begin with a period.

• Example:

.really-big { … }

Programming the World Wide Web

2-14

### 3.4.4 id selectors

![第 15 页](Web技术双语Part-3-层叠样式表课件.assets/第15页.webp)

原文：

3.4.4 id selectors

• An id selector allow the application of a style to one specific element.

• General form:

specific-id {property-value list}

• Example:

section14 {font-size: 20}

<h2 id=“section14”>1.4 Example</h2>

Programming the World Wide Web

2-15

### 3.4.5 Contextual selectors

![第 16 页](Web技术双语Part-3-层叠样式表课件.assets/第16页.webp)

原文：

3.4.5 Contextual selectors

The simplest form of contextual selection is the descendant selector, and different element names are separated by white space.

body b i{font-size:20pt}

Programming the World Wide Web

### 3.4.6 Pseudo class

![第 17 页](Web技术双语Part-3-层叠样式表课件.assets/第17页.webp)

原文：

3.4.6 Pseudo class

Pseudo classes are styles that apply when something happens, rather than because the target element simply exists.

• Names begin with colons

• Example pseudo.html

• hover classes apply when the mouse cursor is over the element

• focus classes apply when an element gets focus

Programming the World Wide Web

### 3.4.6 Pseudo Class Example

![第 18 页](Web技术双语Part-3-层叠样式表课件.assets/第18页.webp)

原文：

3.4.6 Pseudo Class Example

Programming the World Wide Web

### 3.4.7 Universal Selector

![第 19 页](Web技术双语Part-3-层叠样式表课件.assets/第19页.webp)

原文：

3.4.7 Universal Selector

The universal selector applies its style to all elements in a document.

\* {font-size:20pt}

Programming the World Wide Web

2-19

### 3.5 Properties

![第 20 页](Web技术双语Part-3-层叠样式表课件.assets/第20页.webp)

原文：

3.5 Properties

• There are 60 different properties in categories:

• Fonts

• Lists

• Alignment of text

• Colors

• Backgrounds

• Special sections

Programming the World Wide Web

2-20

### 3.6 Font Properties

![第 21 页](Web技术双语Part-3-层叠样式表课件.assets/第21页.webp)

原文：

3.6 Font Properties

• font-family

• Value is a list of font names - browser uses the first in the list

• font-family: Arial, Helvetica, Courier

• If a font name has more than one word, it should be single-quoted.

•font-family: ‘Times New Roman

Programming the World Wide Web

2-21

### 3.6 Font Properties

![第 22 页](Web技术双语Part-3-层叠样式表课件.assets/第22页.webp)

原文：

3.6 Font Properties

• font-size

• Possible values are a length number in points such as 10 pt

or a keyword from the list: xx-small, x-small, small, medium, large, x-large, and xx-large

• Relative size such as smaller or larger

Exampe: font-size: 1.2 em

• font-style

• italic, normal

Programming the World Wide Web

### 3.6 Font Properties

![第 23 页](Web技术双语Part-3-层叠样式表课件.assets/第23页.webp)

原文：

3.6 Font Properties

• font-weight - degrees of boldness

• bolder, lighter, bold, normal

• Could be specified as a multiple of 100 (100 – 900)

• font

• For specifying a list of font properties

font: bolder 14pt Arial Helvetica

• Order must be: style, weight, size, family(s)

• Example fonts.html and fonts2.html

Programming the World Wide Web

### 3.6 Font Properties

![第 24 页](Web技术双语Part-3-层叠样式表课件.assets/第24页.webp)

原文：

3.6 Font Properties

• The text-decoration property

• line-through, overline, underline, none

• Example 3-decoration.html

Programming the World Wide Web

### 3.7 List properties

![第 25 页](Web技术双语Part-3-层叠样式表课件.assets/第25页.webp)

原文：

3.7 List properties

• list-style-type property of an unordered lists

• Bullet can be a disc (default), a square, a circle

• Set it in either the <ul> or <li> tag

• In <ul>, it applies to all list items

• Example

<h3> Some Common Single-Engine Aircraft </h3>

<li> Beechcraft Bonanza </li>

<li> Piper Cherokee </li>

Programming the World Wide Web

2-25

### 3.7 List properties

![第 26 页](Web技术双语Part-3-层叠样式表课件.assets/第26页.webp)

原文：

3.7 List properties

• In <li>, list-style-type applies to just that item

2-26

### 3.7 List properties

![第 27 页](Web技术双语Part-3-层叠样式表课件.assets/第27页.webp)

原文：

3.7 List properties

• On ordered lists list-style-type property can be used to change the sequence values

<table><tr><td>Property value</td><td>Sequence type</td><td>First four</td></tr><tr><td>decimal</td><td>Arabic numerals</td><td>1, 2, 3, 4</td></tr><tr><td>upper-alpha</td><td>Uppercase letters</td><td>A, B, C, D</td></tr><tr><td>lower-alpha</td><td>Lowercase letters</td><td>a, b, c, d</td></tr><tr><td>upper-roman</td><td>Uppercase Roman</td><td>I, II, III, IV</td></tr><tr><td>lower-roman</td><td>Lowercase Roman</td><td>i, ii, iii, iv</td></tr></table>

• Example 3-sequence\_types.html

Programming the World Wide Web

### 3.8 Alignment of text

![第 28 页](Web技术双语Part-3-层叠样式表课件.assets/第28页.webp)

原文：

3.8 Alignment of text

• The text-indent property allows the indentation of the first line

• Takes either a length or a % value

• text-indent:0.5in

• The text-align property is used to arrange text horizontally.

The text-align property has the possible values, left (the default), center, right, or justify

Programming the World Wide Web

2-28

### 3.9 Colors

![第 29 页](Web技术双语Part-3-层叠样式表课件.assets/第29页.webp)

原文：

3.9 Colors

• The color property specifies the foreground color of elements

• The background-color property specifies the background color of elements.

Programming the World Wide Web

2-29

### 3.10.2 Margins

![第 30 页](Web技术双语Part-3-层叠样式表课件.assets/第30页.webp)

原文：

3.10.2 Margins

The margin property is the space between the border (if any) of an element and the element's neighbor.

• It can also be refined into four properties, margin-left, margin-right, margin-bottom, and margin-top

• Example 3-margin.html

Programming the World Wide Web

2-30

### 3.11 Background images

![第 31 页](Web技术双语Part-3-层叠样式表课件.assets/第31页.webp)

原文：

3.11 Background images

• background-image property is used to place an image in the background of an element.

• Example 3-back.html

Programming the World Wide Web

2-31

### 3.12 The  and  tags

![第 32 页](Web技术双语Part-3-层叠样式表课件.assets/第32页.webp)

原文：

3.12 The <span> and <div> tags

In many situations, we want to apply special font properties to less than a whole paragraph of text.

• Solution: a new tag to define an element in the content of a larger element - <span>

• The default meaning of <span> is to leave the content as it is

Now is the <span> best time </span> ever!

Programming the World Wide Web

2-32

### 3.12 The  and  tags

![第 33 页](Web技术双语Part-3-层叠样式表课件.assets/第33页.webp)

原文：

3.12 The <span> and <div> tags

Programming the World Wide Web

2-33

### 3.12 The  and  tags

![第 34 页](Web技术双语Part-3-层叠样式表课件.assets/第34页.webp)

原文：

3.12 The <span> and <div> tags

• Another tag that is useful for style specifications: <div> • Used to create document sections (several paragraphs) for which style can be specified.

• Example 3-div.html

Programming the World Wide Web

2-34

### Class exercises

![第 35 页](Web技术双语Part-3-层叠样式表课件.assets/第35页.webp)

原文：

Class exercises

Exercise 3.5 (pp.135)

Create and test an HTML document that has six short paragraphs of text that describe various aspects of the state in which you live.

You must define three different paragraph styles, p1, p2, and p3. The p1 style must use left and right margins of 20 pixels, a background color of pink, and a foreground color of blue. The p2 style must use left and right margins of 30 pixels, a background color of black, and a foreground color of yellow. The p3 style must use a text indent of 1 centimeter, a background color of green, and a foreground color of white.

The first and fourth paragraphs must use p1, the second and fifth must use p2, and the third and sixth must use p3.

Programming the World Wide Web

2-35
