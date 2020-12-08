
// Set the date we're counting down to
var countDownDate = new Date().getTime();

/* Update the count down every 1 second
var x = setInterval(function() {

    // Get todays date and time
    var now = new Date().getTime();
    
    // Find the distance between now an the count down date
    var distance = countDownDate - now;
    
    // Time calculations for days, hours, minutes and seconds
    var days = Math.floor(distance / (1000 * 60 * 60 * 24));
    var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
    var seconds = Math.floor((distance % (1000 * 60)) / 1000);
    
    // Output the result in an element with id="demo"
    document.getElementById("days").innerHTML = days;
    document.getElementById("hours").innerHTML = hours;
    document.getElementById("minutes").innerHTML = minutes;
    document.getElementById("seconds").innerHTML = seconds;
    
    
    
    // If the count down is over, write some text 
    if (distance <= 0) {
        clearInterval(x);
        document.getElementById("timer").innerHTML = "To Be Communicated";
    }
}, 1000);*/

//smoth scrolling
$(function () {
    
                $('a[href*="#"]:not([href="#"])').click(function () {
                    if (location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') &&
                        location.hostname == this.hostname) {
                        var target = $(this.hash);
                        target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');
                        if (target.length) {
                            $('html, body').animate({
                                scrollTop: target.offset().top
                            }, 1000);
                            return false;
                        }
                    }
                });
    
            });
    
                $(document).ready(function () {
                    $(window).scroll(function () {
                        if ($(this).scrollTop() > 100) {
                            $('#scrollTop').fadeIn();
                            $('nav').addClass('navbar-fixed-top');
                            $('body').addClass('scrollbody');
                        } else {
                            $('#scrollTop').fadeOut();
                            $('nav').removeClass('navbar-fixed-top');
                            $('body').removeClass('scrollbody');
                        }
                    });
                });
        
                window.sr =ScrollReveal();
                sr.reveal('.btngrov ',{
                duration: 2000,
                delay: 500,
                    origin:'bottom',
                    distance:'1000px'
                });
                sr.reveal('.anim',{
                duration: 2000,
                    origin:'top',
                    distance: '100px'
                });
                sr.reveal('.fa ',{
                    duration:2000,
                    origin:'right',
                    distance:'30px'
                })
               sr.reveal('.local,maintext',{
                   duration:2000,
                   origin:'left',
                   distance:'200px'
               })
//scroll spy
$('body').scrollspy({target: '.navbar-fixed-top'});
 
//tooltip
$(document).ready(function () {
    $('[data-toggle="tooltip"]').tooltip();
});
