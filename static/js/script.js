// =========================
// TYPING ANIMATION
// =========================

const roles = [
    "Python Developer",
    "Software Developer",
    "Data Science Student"
];

let roleIndex = 0;
let characterIndex = 0;
let isDeleting = false;

const typingText =
    document.getElementById("typing-text");


function typingAnimation() {

    const currentRole = roles[roleIndex];

    if (!isDeleting) {

        typingText.textContent =
            currentRole.substring(
                0,
                characterIndex + 1
            );

        characterIndex++;

        if (characterIndex === currentRole.length) {

            isDeleting = true;

            setTimeout(
                typingAnimation,
                1400
            );

            return;
        }

    } else {

        typingText.textContent =
            currentRole.substring(
                0,
                characterIndex - 1
            );

        characterIndex--;

        if (characterIndex === 0) {

            isDeleting = false;

            roleIndex =
                (roleIndex + 1)
                % roles.length;

        }

    }

    const speed =
        isDeleting ? 45 : 90;

    setTimeout(
        typingAnimation,
        speed
    );

}


typingAnimation();


// =========================
// MOBILE MENU
// =========================

const menuBtn =
    document.getElementById("menuBtn");

const navLinks =
    document.getElementById("navLinks");


menuBtn.addEventListener(
    "click",
    function () {

        menuBtn.classList.toggle("open");

        navLinks.classList.toggle("open");

    }
);


// =========================
// CLOSE MOBILE MENU
// =========================

document
    .querySelectorAll(".nav-link")
    .forEach(function (link) {

        link.addEventListener(
            "click",
            function () {

                menuBtn.classList.remove("open");

                navLinks.classList.remove("open");

            }
        );

    });


// =========================
// NAVBAR SCROLL EFFECT
// =========================

const navbar =
    document.getElementById("navbar");


window.addEventListener(
    "scroll",
    function () {

        if (window.scrollY > 30) {

            navbar.classList.add("scrolled");

        } else {

            navbar.classList.remove("scrolled");

        }

    }
);


// =========================
// SCROLL REVEAL
// =========================

const revealElements =
    document.querySelectorAll(".reveal");


const revealObserver =
    new IntersectionObserver(

        function (entries) {

            entries.forEach(
                function (entry) {

                    if (entry.isIntersecting) {

                        entry.target
                            .classList
                            .add("visible");

                    }

                }
            );

        },

        {
            threshold: 0.12
        }

    );


revealElements.forEach(
    function (element) {

        revealObserver.observe(element);

    }
);


// =========================
// ACTIVE NAVIGATION
// =========================

const sections =
    document.querySelectorAll("section");

const navigationLinks =
    document.querySelectorAll(".nav-link");


window.addEventListener(
    "scroll",
    function () {

        let currentSection = "";

        sections.forEach(
            function (section) {

                const sectionTop =
                    section.offsetTop - 150;

                const sectionHeight =
                    section.offsetHeight;

                if (
                    window.scrollY >= sectionTop &&
                    window.scrollY <
                    sectionTop + sectionHeight
                ) {

                    currentSection =
                        section.getAttribute("id");

                }

            }
        );


        navigationLinks.forEach(
            function (link) {

                link.classList.remove("active");

                if (
                    link.getAttribute("href") ===
                    "#" + currentSection
                ) {

                    link.classList.add("active");

                }

            }
        );

    }
);


// =========================
// BACK TO TOP
// =========================

const backToTop =
    document.getElementById("backToTop");


window.addEventListener(
    "scroll",
    function () {

        if (window.scrollY > 500) {

            backToTop.classList.add("show");

        } else {

            backToTop.classList.remove("show");

        }

    }
);


backToTop.addEventListener(
    "click",
    function () {

        window.scrollTo({

            top: 0,

            behavior: "smooth"

        });

    }
);