{% load static %}
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>Ruheza NS | Portfolio</title>
    <meta name="description" content="">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="robots" content="all,follow">
    <!-- Bootstrap CSS-->
    <link rel="stylesheet" href="{% static 'vendor/bootstrap/css/bootstrap.min.css' %}">
    <!-- Google fonts-->
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Cardo:400,400i">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Montserrat:400,700">
    <!-- Lightbox-->
    <link rel="stylesheet" href="{% static 'vendor/lightbox2/css/lightbox.min.css' %}">
    <!-- Font Awesome-->
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.7.2/css/all.css" integrity="sha384-fnmOCqbTlWIlj8LyTjo7mOUStjsKC4pOpQbqyi7RrhN7udi9RwhKkMHpvLbHG9Sr" crossorigin="anonymous">
    <!-- Parallax-->
    <link rel="stylesheet" href="{% static 'vendor/onepage-scroll/onepage-scroll.css' %}">
    <!-- theme stylesheet-->
    <link rel="stylesheet" href="{% static 'css/style.default.css' %}" id="theme-stylesheet">
    <!-- Custom stylesheet - for your changes-->
    <link rel="stylesheet" href="{% static 'css/custom.css' %}">
    <!-- Favicon-->
    <link rel="shortcut icon" href="{% static 'favicon.png' %}">
    <!-- Tweaks for older IEs--><!--[if lt IE 9]>
        <script src="https://oss.maxcdn.com/html5shiv/3.7.3/html5shiv.min.js"></script>
        <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script><![endif]-->
  </head>
  <body>
    <div class="main">
      <section class="bg-cover bg-center hero">
        <div class="dark-overlay"></div>
        <div class="position-relative z-index-1">
          <div class="container text-center text-white">
            <p class="font-italic lead">Oh, hello, nice to meet you!</p>
            <h2 class="text-uppercase my-4">i'm Stan.</h2>
            <p class="font-italic lead">its my pleasure to find you here. Hope you'll enjoy this intergration</p>
            <p class="font-italic lead">...remember, dont leave void.Make a scratch up and i'll respond</p>
          </div>
        </div>
        <div class="scroll-btn link-scroll"><i class="fas fa-angle-double-down"></i></div>
      </section>
      <section id="1">
        <div class="d-flex h-100 align-items-center">
          <div class="container">
            <div class="row align-items-center">
              <div class="col-lg-6 mb-4 mb-lg-0">
                <header class="text-center">
                  <h2 class="text-uppercase lined">About Me</h2>
                </header>
                <p class="lead">here's me....huh!</p>
                  <p></p>
                <p>currently, a student at University of Dar es Salaam-(CoICT) pursuing Bsc. in Telecommunication Engineering. Ambitious, passionate and skilled with various technologies...</p>

              </div>
              <div class="col-lg-6"><img src="{% static 'img/about.jpg' %}" alt="..." class="img-fluid rounded-circle d-block mx-auto"></div>
            </div>
          </div>
        </div>
      </section>
      <section class="bg-gray">
        <div class="d-flex h-100 align-items-center">
          <div class="container">
            <header class="mb-5 text-center">
              <h2 class="text-uppercase lined">Services</h2>
            </header>
            <div class="row text-center">
              <div class="col-lg-4 col-md-6 mb-4">
                <div class="icon mb-3"><i class="fas fa-desktop"></i></div>
                <h4 class="text-uppercase lined lined-compact">Web development</h4>
                <p class="text-mted">including blogs, e-commerce and content management system(cms) </p>
              </div>

                <div class="col-lg-4 col-md-6 mb-4">
                <div class="icon mb-3"><i class="fas fa-globe-americas"></i></div>
                <h4 class="text-uppercase lined lined-compact">Web hosting</h4>
                <p class="text-mted">may help you to host your site and make it live and accessible around the cosmos</p>
              </div>
              <div class="col-lg-4 col-md-6 mb-4">
                <div class="icon mb-3"><i class="fas fa-print"></i></div>
                <h4 class="text-uppercase lined lined-compact">IT research-prep</h4>
                <p class="text-mted">it needs a research before jump into it...may help you to conduct your IT based-research with the right information and great report!</p>
              </div>

              <div class="col-lg-4 col-md-6 mb-4">
                <div class="icon mb-3"><i class="far fa-lightbulb"></i></div>
                <h4 class="text-uppercase lined lined-compact">Consulting</h4>
                <p class="text-mted">having an IT project idea and dont know where to start? free consultation, dont hesitate</p>
              </div>
              <div class="col-lg-4 col-md-6 mb-4">
                <div class="icon mb-3"><i class="far fa-envelope"></i></div>
                <h4 class="text-uppercase lined lined-compact">Email marketing</h4>
                <p class="text-mted">help you to develop intact relationship with your customers and promote your product/business</p>
              </div>
              <div class="col-lg-4 col-md-6 mb-4">
                <div class="icon mb-3"><i class="fas fa-user"></i></div>
                <h4 class="text-uppercase lined lined-compact">UI &amp; UX</h4>
                <p class="text-mted">with great interfaces and easy using them...its a promice to experience the best of it</p>
              </div>
            </div>
          </div>
        </div>
      </section>
      <section>
        <div class="d-flex h-100 align-items-center">
          <div class="container">
            <header class="text-center mb-5">
              <h2 class="text-uppercase lined">Gallery</h2>
            </header>
            <div class="row">
              <div class="col-lg-12 text-center">
{#                <p>image gallery</p>#}
              </div>
              <div class="col-lg-4 col-md-6 mb-4"><a href="{% static 'img/portfolio-1.jpg' %}" data-lightbox="image-1" data-title="My caption" class="d-block mb-1"><img src="{% static 'img/portfolio-1.jpg' %}" alt="..." class="img-fluid d-block mx-auto"></a></div>
              <div class="col-lg-4 col-md-6 mb-4"><a href="{% static 'img/portfolio-2.jpg' %}" data-lightbox="image-1" data-title="My caption" class="d-block mb-1"><img src="{% static 'img/portfolio-2.jpg' %}" alt="..." class="img-fluid d-block mx-auto"></a></div>
              <div class="col-lg-4 col-md-6 mb-4"><a href="{% static 'img/portfolio-3.jpg' %}" data-lightbox="image-1" data-title="My caption" class="d-block mb-1"><img src="{% static 'img/portfolio-3.jpg' %}" alt="..." class="img-fluid d-block mx-auto"></a></div>
              <div class="col-lg-4 col-md-6 mb-4"><a href="{% static 'img/portfolio-4.jpg' %}" data-lightbox="image-1" data-title="My caption" class="d-block mb-1"><img src="{% static 'img/portfolio-4.jpg' %}" alt="..." class="img-fluid d-block mx-auto"></a></div>
              <div class="col-lg-4 col-md-6 mb-4"><a href="{% static 'img/portfolio-5.jpg' %}" data-lightbox="image-1" data-title="My caption" class="d-block mb-1"><img src="{% static 'img/portfolio-5.jpg' %}" alt="..." class="img-fluid d-block mx-auto"></a></div>
              <div class="col-lg-4 col-md-6 mb-4"><a href="{% static 'img/portfolio-6.jpg' %}" data-lightbox="image-1" data-title="My caption" class="d-block mb-1"><img src="{% static 'img/portfolio-6.jpg' %}" alt="..." class="img-fluid d-block mx-auto"></a></div>
            </div>
          </div>
        </div>
      </section>
      <section class="bg-gray">
        <div class="d-flex h-100 align-items-center">
          <div class="container">
            <header class="text-center mb-5">
              <h2 class="text-uppercase lined">Projects</h2>
            </header>
            <div class="row">
              <div class="col-lg-6">
                  <p>Here's the list of some of accomplished projects. Take a look..</p><br>
                <p><a href="#">e-commerce web</a> </p>
                   <p><a href="#">another e-commerce web</a> </p>
                  <p><a href="#">blog</a> </p>
                  <p><a href="#">content management system(cms)</a> </p>
                  <p><a href="#">another cms</a> </p>
              </div>
              <div class="col-lg-6">
                <p>The above projects are still on process. Hope to upload their links soon, very soon...</p>
              </div>
            </div>
          </div>
        </div>
      </section>
      <section>
        <div class="d-flex h-100 align-items-center">
          <div class="container">
            <header class="text-center mb-5">
              <h2 class="text-uppercase lined">Contact</h2>
            </header>
            <div class="row">
              <div class="col-lg-4">
               <ul>
                   <li class="list-inline-item"><a href="#" class="social-link social-link-email"><i class="fas fa-envelope"></i></a></li>2001stany@gmail.com<br><br>
                   <li class="list-inline-item"><a href="#" class="social-link social-link-facebook"><i class="fab fa-facebook-f"></i></a></li>maenTechie<br><br>
                  <li class="list-inline-item"><a href="#" class="social-link social-link-twitter"><i class="fab fa-twitter"></i></a></li>@maenTechie_ioi<br><br>
                   <li class="list-inline-item"><a href="#" class="social-link social-link-whatsapp"><i class="fab fa-whatsapp"></i></a></li>0717614769<br><br>
                  <li class="list-inline-item"><a href="#" class="social-link social-link-instagram"><i class="fab fa-instagram"></i></a></li>maenTechie_ioi<br>
               </ul>
              </div>
              <div class="col-lg-6">
                <p>Am glad to meet you here.Do you have an idea that needs IT consultation?</p>
                <p>Are you looking for webApp developer?</p>
                  <p>Do you want a system for automating your stuffs?</p>
                  <p>What about android apps?</p>
                   <p>Or are you looking for team project member?</p>
                   <br>
                    <br>
                   <strong><p>contact now...i develop it before the dawn!</p></strong>

              </div>
            </div>
            <footer class="py-5 mt-5">
              <div class="row">
                <div class="col-lg-6 text-center text-lg-left">
                  <p class="font-italic mb-0 text-gray">&copy; 2019 maenTechie</p>
                </div>
                <div class="col-lg-6 text-center text-lg-right">

                </div>
              </div>
            </footer>
          </div>
        </div>
      </section>
    </div>
    <!-- JavaScript files-->
    <script src="{% static 'vendor/jquery/jquery.min.js' %}"></script>
    <script src="{% static 'vendor/bootstrap/js/bootstrap.bundle.min.js' %}"></script>
    <script src="{% static 'vendor/onepage-scroll/jquery.onepage-scroll.min.js' %}"></script>
    <script src="{% static 'vendor/lightbox2/js/lightbox.min.js' %}"></script>
    <script src="{% static 'js/front.js' %}"></script>
    <!-- FontAwesome CSS - loading as last, so it doesn't block rendering-->
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.7.1/css/all.css" integrity="sha384-fnmOCqbTlWIlj8LyTjo7mOUStjsKC4pOpQbqyi7RrhN7udi9RwhKkMHpvLbHG9Sr" crossorigin="anonymous">
  </body>
</html>
