(function () {
  function initOrbit(root) {
    var apps = [];
    try {
      apps = JSON.parse(root.getAttribute("data-apps") || "[]");
    } catch (e) {
      apps = [];
    }
    if (!apps.length) return;

    var ui = {
      more: root.getAttribute("data-ui-more") || "Learn more",
      moreShort: root.getAttribute("data-ui-more-short") || "More",
      video: root.getAttribute("data-ui-video") || "Video",
      videoLong: root.getAttribute("data-ui-video-long") || "Watch on YouTube",
      soon: root.getAttribute("data-ui-soon") || "Coming soon",
      open: root.getAttribute("data-ui-open") || "Open",
      soonAria: root.getAttribute("data-ui-soon-aria") || "coming soon",
    };

    var planets = Array.prototype.slice.call(root.querySelectorAll("[data-orbit-planet]"));
    var ring = root.querySelector(".app-orbit-ring");
    var center = root.querySelector(".app-orbit-center");
    var centerArt = root.querySelector("[data-orbit-center-art]");
    var centerTitle = root.querySelector("[data-orbit-center-title]");
    var centerDesc = root.querySelector("[data-orbit-center-desc]");
    var centerActions = root.querySelector("[data-orbit-center-actions]");
    var centerVideo = root.querySelector("[data-orbit-center-video]");
    var centerSoon = root.querySelector("[data-orbit-center-soon]");
    var centerLink = root.querySelector("[data-orbit-center-link]");
    var detail = root.querySelector("[data-orbit-detail]");
    var detailTitle = root.querySelector("[data-orbit-detail-title]");
    var detailDesc = root.querySelector("[data-orbit-detail-desc]");
    var detailActions = root.querySelector("[data-orbit-detail-actions]");
    var detailVideo = root.querySelector("[data-orbit-detail-video]");
    var counter = root.querySelector("[data-carousel-counter]");
    var prev = root.querySelector("[data-carousel-prev]");
    var next = root.querySelector("[data-carousel-next]");

    var index = 0;
    var n = apps.length;
    var step = 360 / n;
    // Accumulated ring rotation so the selected planet sits at the top (0deg).
    // Applied as real transform on the ring (iOS Safari won't interpolate CSS vars in transform).
    var rotation = 0;

    planets.forEach(function (planet, i) {
      var baseAngle = step * i;
      planet.style.setProperty("--angle", baseAngle + "deg");
      planet.dataset.baseAngle = String(baseAngle);
      var app = apps[i];
      if (!app || planet.querySelector(".app-orbit-planet-name")) return;
      var billboard = document.createElement("span");
      billboard.className = "app-orbit-planet-billboard";
      var face = document.createElement("span");
      face.className = "app-orbit-planet-face";
      while (planet.firstChild) face.appendChild(planet.firstChild);
      billboard.appendChild(face);
      var label = document.createElement("span");
      label.className = "app-orbit-planet-name";
      // Keep "Transparent Screen" on two lines so it doesn't invade the center disk.
      if (app.name === "Transparent Screen") {
        label.classList.add("is-stacked");
        label.appendChild(document.createTextNode("Transparent"));
        label.appendChild(document.createElement("br"));
        label.appendChild(document.createTextNode("Screen"));
      } else {
        label.textContent = app.name;
      }
      billboard.appendChild(label);
      planet.appendChild(billboard);
    });

    function badgeHtml(href, img, alt, aria) {
      return (
        '<a class="store-badge-link" href="' +
        href +
        '" target="_blank" rel="noopener noreferrer" aria-label="' +
        aria +
        '"><img src="' +
        img +
        '" alt="' +
        alt +
        '" width="120" height="40"></a>'
      );
    }

    function renderActions(target, app, compact) {
      if (!target) return;
      var html = "";
      if (app.store) {
        html += badgeHtml(
          app.store,
          "../assets/images/download-on-the-app-store-en-us-white.svg",
          "Download on the App Store",
          "App Store · " + app.name
        );
      }
      if (app.play) {
        html += badgeHtml(
          app.play,
          "../assets/images/get-it-on-google-play-en.png",
          "Google Play",
          "Google Play · " + app.name
        );
      }
      if (app.href && !app.soon) {
        html +=
          '<a class="btn btn-secondary" href="' +
          app.href +
          '">' +
          (compact ? ui.moreShort : ui.more) +
          "</a>";
      }
      target.innerHTML = html;
    }

    function renderVideo(el, app, longLabel) {
      if (!el) return;
      var label = el.querySelector("span");
      if (label) label.textContent = longLabel ? ui.videoLong : ui.video;
      if (!app.video) {
        el.hidden = true;
        el.removeAttribute("href");
        return;
      }
      el.hidden = false;
      el.href = "https://youtu.be/" + app.video;
      var img = el.querySelector("img");
      if (img) img.src = "https://i.ytimg.com/vi/" + app.video + "/hqdefault.jpg";
    }

    function applySpin() {
      // Ring spins; center + billboards counter-rotate so icons/labels stay upright.
      if (ring) ring.style.transform = "rotate(" + -rotation + "deg)";
      if (center) center.style.transform = "rotate(" + rotation + "deg)";
      planets.forEach(function (planet) {
        var base = parseFloat(planet.dataset.baseAngle || "0") || 0;
        var billboard = planet.querySelector(".app-orbit-planet-billboard");
        if (billboard) {
          billboard.style.transform = "rotate(" + (rotation - base) + "deg)";
        }
      });
    }

    function render() {
      var app = apps[index];

      applySpin();

      planets.forEach(function (planet, i) {
        planet.classList.toggle("is-active", i === index);
        planet.setAttribute("aria-current", i === index ? "true" : "false");
      });

      if (centerArt) {
        if (app.image) {
          centerArt.innerHTML =
            '<img src="' + app.image + '" alt="" width="240" height="240" decoding="async">';
        } else {
          centerArt.innerHTML = '<span class="soon-mark">SOON</span>';
        }
      }
      if (centerLink) {
        if (app.href && !app.soon) {
          centerLink.href = app.href;
          centerLink.setAttribute("aria-label", ui.open + " " + app.name);
          centerLink.removeAttribute("aria-disabled");
          centerLink.classList.remove("is-disabled");
          centerLink.tabIndex = 0;
        } else {
          centerLink.removeAttribute("href");
          centerLink.setAttribute("aria-disabled", "true");
          centerLink.classList.add("is-disabled");
          centerLink.tabIndex = -1;
          centerLink.setAttribute("aria-label", app.name + " (" + ui.soonAria + ")");
        }
      }
      if (centerTitle) centerTitle.textContent = app.name;
      if (centerDesc) centerDesc.textContent = app.blurb;
      renderActions(centerActions, app, true);
      renderVideo(centerVideo, app, false);
      if (centerSoon) {
        centerSoon.hidden = !app.soon;
        centerSoon.textContent = ui.soon;
      }

      if (detailTitle) detailTitle.textContent = app.name;
      if (detailDesc) detailDesc.textContent = app.detail || app.blurb;
      renderActions(detailActions, app, false);
      renderVideo(detailVideo, app, true);

      if (counter) counter.textContent = index + 1 + " / " + n;
      if (detail) detail.hidden = false;
    }

    function go(to) {
      var nextIndex = ((to % n) + n) % n;
      if (nextIndex === index) return;
      var delta = nextIndex - index;
      // Shortest turn on the ring (e.g. 0 → 7 with 8 apps = one step back).
      if (delta > n / 2) delta -= n;
      if (delta < -n / 2) delta += n;
      rotation += delta * step;
      index = nextIndex;
      render();
    }

    planets.forEach(function (planet, i) {
      planet.addEventListener("click", function () {
        go(i);
      });
    });
    if (prev) prev.addEventListener("click", function () { go(index - 1); });
    if (next) next.addEventListener("click", function () { go(index + 1); });

    root.addEventListener("keydown", function (e) {
      if (e.key === "ArrowLeft") go(index - 1);
      if (e.key === "ArrowRight") go(index + 1);
    });

    root.setAttribute("tabindex", "0");
    render();
  }

  document.querySelectorAll("[data-app-carousel]").forEach(initOrbit);
})();
