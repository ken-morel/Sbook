
for(let element of  $("[hover-class]")) {
    element.addEventListener("mouseenter", function() {
        element.classList.add(
            ...element.getAttribute("hover-class").split(" ")
        );
    });
    element.addEventListener("mouseleave", function() {
        element.classList.remove(
            ...element.getAttribute("hover-class").split(" ")
        );
    });
};

for(let element of  $("[css-transition]")) {
    element.style.transition = element.getAttribute("css-transition");
};

for(let element of $("[view-class]")) {
    console.log("view-class", element);
    (new IntersectionObserver(
        (entries, observer) => {
            entries.forEach((entry) => {
                // Each entry describes an intersection change for one observed
                // target element:
                //   entry.boundingClientRect
                //   entry.intersectionRatio
                //   entry.intersectionRect
                //   entry.isIntersecting
                //   entry.rootBounds
                //   entry.target
                //   entry.time
                let cls = element.getAttribute("view-class").split(" ");
                let ncls = cls.filter((c) => c.startsWith("!"));
                cls = cls.filter((c) => !c.startsWith("!"));
                for(var i = 0; i < ncls.length; i++) ncls[i] = ncls[i].slice(1);
                if(entry.isIntersecting) {
                    console.log("added", ...element.getAttribute("view-class").split(" "));
                    element.classList.add(
                        ...cls
                    );
                    element.classList.remove(
                        ...ncls
                    );
                } else {
                    console.log("removed", ...element.getAttribute("view-class").split(" "));
                    element.classList.remove(
                        ...cls
                    );
                    element.classList.add(
                        ...ncls
                    );
                }
            });
        },
        {
            root: null,
            rootMargin: "0px",
            threshold: [1.0, 0.5, 0.0],
        },
    )).observe(element);
};