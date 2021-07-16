$(document).on("click", '[data-toggle="lightbox"]', function (event) {
  event.preventDefault();
  $(this).ekkoLightbox();
});

const spans = document.querySelectorAll(".word span");

spans.forEach((span, idx) => {
  span.addEventListener("click", (e) => {
    e.target.classList.add("active");
  });
  span.addEventListener("animationend", (e) => {
    e.target.classList.remove("active");
  });

  // Initial animation
  setTimeout(() => {
    span.classList.add("active");
  }, 750 * (idx + 1));
});

/* Demo purposes only */
$(".hover").mouseleave(function () {
  $(this).removeClass("hover");
});

new fullpage("#full-page", {});

if (window.chrome)
  $("[type=video\\/mp4]").each(function () {
    $(this).attr("src", $(this).attr("src").replace(".mp4", "_c.mp4"));
  });

function typeEffect(element, speed) {
  var text = element.innerHTML;
  element.innerHTML = "";

  var i = 0;
  var timer = setInterval(function () {
    if (i < text.length) {
      element.append(text.charAt(i));
      i++;
    } else {
      clearInterval(timer);
    }
  }, speed);
}

// application
var speed = 75;
var h1 = document.querySelector("h1");
var p = document.querySelector("p");
var delay = h1.innerHTML.length * speed + speed;

// type affect to header
// typeEffect(h1, speed);

// type affect to body
setTimeout(function () {
  p.style.display = "inline-block";
  typeEffect(p, speed);
}, delay);
