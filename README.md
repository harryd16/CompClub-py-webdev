<html>
<head>
    <title>Python Flask</title>
    <!-- Latest compiled and minified CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
    <script>
        (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
        (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
        m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
        })(window,document,'script','https://www.google-analytics.com/analytics.js','ga');

        ga('create', 'UA-84018363-1', 'auto');
        ga('send', 'pageview');

    </script>
</head>
<body>
    <div class="container">
        <div class="page-header">
            <h1>Python Flask Dynamic Web Dev</h1>
            <p class="lead">
                A brief Introduction to the python web development framework
                <a href="http://flask.pocoo.org/"><i>flask</i></a>.
                <br>Some knowledge of python, and a little HTML/CSS is necessary
                to follow along with this tutorial.
            </p>
        </div>

        <h3>How do websites work?</h3>
        <p>
            Perhaps you've worked with pure HTML+CSS before and discovered that
            you are limited to static webpages that can't easily move information
            around from page to page. With the power of python and the framework
            Flask, we are able to extend our website's capability to handle interaction
            with the user through the likes of activity sharing, user management
            and applications.
        </p>

        <p>
            The diagram below shows how a user interacts with your website. (Taken from <a href="http://www.lubith.com/tutorials/how-a-website-works-and-why-do-i-need-web-hosting/">lubith.com</a>)
            <br>
            <ul>
                <li>
                    The <b>web server</b> receives the request for a web page sent by the user's <b>browser</b>.
                </li>
                <li>
                    The user's <b>browser</b> connects to the <b>web server</b> via an IP address (which
                    may have been translated from a domain name) before the <b>web server</b> responds
                    to it.
                </li>
            </ul>
            <center><img src="http://www.monolithdesign.com/class-html/images/Site-Mechanics-New.gif" width=40% height=40%></center>
        </p>

        <h3>What are the roles of HTML and CSS?</h3>
        <p>
            HTML stands for Hypertext Markup Language and is the language used
            by browsers for displaying data/information and presenting it in certain ways.
            <br>
            CSS stands for Cascading Style Sheets and is used for describing the
            way in which HTML documents are presented.
        </p>

        <h3>Backend VS Frontend</h3>
        <p>
            <b>Backend</b> refers to the code and processes that occur on the server-side.
            These processes commonly handle user requests and work with the database
            closely where security is usually assured. An example of a backend process
            would be the log-in process where the user has provided their username/password.
        </p>
        <p>
            <b>Frontend</b> refers to all the code, information and processes that
            have been passed onto the user's browser from the server and influence
            the way the user interacts and perceives the data/information. HTML/CSS fits
            with belonging to the Frontend since the user interacts with it.
        </p>

        <p>
            <center><img src="http://i.imgur.com/PoEpci8.png"></center>
        </p>

        <h3>Where does Python and Flask come in?</h3>
        <p>
            Flask is a framework used in the backend side of web development and sits
            on the server and NOT on the user's end. Flask handles user requests that
            the server receives and processes them accordingly. Python is a favourable
            language for it's incredible simplicity whilst also remaining incredibly
            powerful.
        </p>
        <p>
            Many popular websites run off of python including the following:
            <ul>
                <li>Facebook</li>
                <li>Reddit</li>
                <li>Youtube</li>
                <li>CompClub!</li>
            </ul>
        </p>
        <p>
            Flask is just one of many frameworks written in Python, and here's a list
            of some other popular ones:
            <ul>
                <li><a href="https://www.djangoproject.com/">Django</a></li>
                <li><a href="http://www.tornadoweb.org/en/stable/">Tornado</a></li>
                <li><a href="https://trypyramid.com/">Pyramid</a></li>
            </ul>
        </p>

        <h2>Tutorial</h2>
        <table class="table">
            <tr>
                <th>Part</th>
                <th>Description</th>
            </tr>
            <tr>
                <td><a href="Part-1-Hello-World.html">Part 1 - Hello World</a></td>
                <td>
                    Every starting tutorial gets you to write a hello world program.
                    This one is no different.
                </td>
            </tr>
            <tr>
                <td>TBC</td>
                <td>TBC</td>
            </tr>
        </table>

        <h2>Source Code</h2>
        <h4>The project code can be found on <a href="https://github.com/jqhils/flask-tut-app">github</a></h4>
        <center><img src="https://assets-cdn.github.com/images/modules/site/squares.png" width=100%></center>
        <h2>Further Readings</h2>
        <table class="table">
            <tr>
                <th>Resource</th>
                <th>Description</th>
            </tr>
            <tr>
                <td><a href="https://docs.google.com/document/d/16MluPbbv6yjOVersR0TOqoyltRJ5L4yWL4SdswwzJqg/edit?usp=sharing">Terminal Cheat Sheet</a></td>
                <td>
                    The terminal interface can seem daunting at first. This Cheat
                    Sheet will aid your discovery with useful tips and hints on various
                    commands.
                </td>
            </tr>
            <tr>
                <td><a href="http://flask.pocoo.org/">Offical Flask Website</a></td>
                <td>
                    The official website for flask includes tutorials for getting started,
                    and references for various popular flask extensions you can quickly
                    import into your project and quickly get working.
                    <br>
                    E.g. Login, Admin, Encryption, Mail, Security, Uploads etc.
                </td>
            </tr>
            <tr>
                <td><a href="https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world">Flask Mega-Tutorial</a> by Miguel Grinberg</td>
                <td>
                    A comprehensive tutorial that takes you through many aspects
                    of flask and working with databases, as well as deploying your
                    website to a public domain through heroku.
                </td>
            </tr>
            <tr>
                <td><a href="https://tutorial.djangogirls.org/en/">Django Girls Tutorial</a></td>
                <td>
                    A great comprehensive tutorial set at a very beginner-friendly
                    level, but for the Python Django Framework. (Another widely popular
                    framework)
                </td>
            </tr>
            <tr>
                <td><a href="https://rogerdudler.github.io/git-guide/">git - the simple guide</a></td>
                <td>
                    A simple guide for getting started with git with nothing too
                    advanced.
                </td>
            </tr>
            <tr>
                <td><a href="http://javascript.info/">The Javascript Tutorial</a></td>
                <td>
                    HTML5 is great. jQuery is cool. Node.JS is awesome. Base them
                    on the solid, powerful basement of pure JavaScript and you can rock the web! ;)
                </td>
            </tr>
            <tr>
                <td><a href="https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/JavaScript_basics">MDN - Javascript Basics</td>
                <td>
                    Mozilla Developer Network is one of the best javascript referencing
                    sites at the moment. For all your javascript needs.
                </td>
            </tr>
        </table>
    </div>
</body>
</html>
