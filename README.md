




<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->





<h3 align="center">QR Inventory Tracking Web App</h3>

  <p align="center">
    This web app was developed to allow automated inventory tracking to replace a manual and slow process of using excel sheets and manual comparisons. 
    <br />
     <br />
    <a href="https://github.com/jalepino1/QR-Inventory-Tracking-Web-App"><strong>Explore the docs »</strong></a>
    <br />
    <br/>
 







<!-- ABOUT THE PROJECT -->
## About The Project

Developing an automated inventory management system leveraging Python with Django for the server-side logic with PostgreSQL for database management. 

Inventory tracking is done with an integrated barcode using the ScanApp API. A JavaScript function utilizes this API to process QR codes and barcodes. Django's URL routing, template language, and views allow real-time comparison between the QR data, and the data within the database.

Django's built-in authentication features allow permissive access to the web app, as well as CSRF tokens for cross site communication.

The Inventory Management system includes tables that tracks all data within the database in addition to the last time each specific item in the database was last checked. This is done using Django's built-in templates with HTML and Django template language, and CSS for styling. Additionally, forms were made using Django's built in forms and relation with the database.

This project utilizes AWS EC2 and RCS instances to cloud host the PostgreSQL database, as well as the Django web application. Domain and SSL certificate rights were acquired using Amazon LightSail, Route 53, and AWS Certificate Manager.


<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* Django 
* Bootstrap
* PostgreSQL
* AWS


<p align="right">(<a href="#readme-top">back to top</a>)</p>






<!-- USAGE EXAMPLES -->
## Benefits

Automate Manual Tasks: 
  - Barcode and RFID scanning can speed manual inventory checks, inventory searches and decrease labor cost.

Error Reduction: 
  - Using software reduces errors from manual entries and display other information using algorithms.

Greater Organization: 
  - Inventory Management Systems help create better organization structures. They allow categorization of different items within an inventory and track products simply and effectively.

Data Security: 
  - Inventory Management Systems allow users to restrict the access to their inventory. Permissions like this can help prevent data breaches and ensure confidentiality through means of encryption.

<p align="right">(<a href="#readme-top">back to top</a>)</p>





<!-- LICENSE -->
## License

MIT License

Copyright (c) 2024 Henry Crawley

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Henry Crawley - [@LinkedIn](www.linkedin.com/in/henry-crawley-692a08216) - hengeno818@gmail.com

Project Link: [https://github.com/jalepino1/QR-Inventory-Tracking-Web-App](https://github.com/jalepino1/QR-Inventory-Tracking-Web-App)

<p align="right">(<a href="#readme-top">back to top</a>)</p>







<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/github_username/repo_name.svg?style=for-the-badge
[contributors-url]: https://github.com/github_username/repo_name/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/github_username/repo_name.svg?style=for-the-badge
[forks-url]: https://github.com/github_username/repo_name/network/members
[stars-shield]: https://img.shields.io/github/stars/github_username/repo_name.svg?style=for-the-badge
[stars-url]: https://github.com/github_username/repo_name/stargazers
[issues-shield]: https://img.shields.io/github/issues/github_username/repo_name.svg?style=for-the-badge
[issues-url]: https://github.com/github_username/repo_name/issues
[license-shield]: https://img.shields.io/github/license/github_username/repo_name.svg?style=for-the-badge
[license-url]: https://github.com/github_username/repo_name/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
