//$('h1').mouseenter(start).mouseleave(stop)

var tl = new TimelineLite({
  paused: true
})
init();
 start();

function init() {
  var fern = document.querySelector('[id^="fern"]')
  fern.parentNode.insertBefore(fern.cloneNode(true), fern)
  fern.parentNode.insertBefore(fern.cloneNode(true), fern)
  fern.parentNode.insertBefore(fern.cloneNode(true), fern)
  fern.parentNode.insertBefore(fern.cloneNode(true), fern)
  var ferns = document.querySelectorAll('[id^="fern"]')
  TweenLite.set(ferns, {
    visibility: 'visible'
  })
  TweenLite.set(ferns[0], {
    bottom: '47px',
    right: '227px',
    scaleX: -1,
    rotation: -30
  })
  TweenLite.set(ferns[1], {
    bottom: '0',
    right: '-50px',
    scaleX: -1,
    rotation: 45
  })
  TweenLite.set(ferns[2], {
    top: '5px',
    left: '148px',
    rotation: 28
  })
  TweenLite.set(ferns[3], {
    top: '0',
    left: '-50px',
    rotation: 90
  })
  TweenLite.set(ferns[4], {
    bottom: '0',
    left: '-50px',
    rotation: -20
  })

  var spirals = document.querySelectorAll('[id^="spiral"]')
  spirals.forEach(function(spiral) {
    TweenLite.set(spiral, {
      strokeDasharray: spiral.getTotalLength(),
      stroke: '#d2691e'
    })

    var g = document.createElementNS("http://www.w3.org/2000/svg", 'g')
    g.id = 'leaves'
    spiral.parentNode.insertBefore(g, spiral)
    const spacing = 10
    for (var i = 0; i < spiral.getTotalLength(); i += 1) {
      const length = 10 + i * 4
      if (length < spiral.getTotalLength()) {
        const point = spiral.getPointAtLength(length)
        const before = spiral.getPointAtLength(length - 3)
        const deg = Math.atan2(point.y - before.y, point.x - before.x) * 180 / Math.PI
        var leaf = g.appendChild(document.createElementNS("http://www.w3.org/2000/svg", "path"))
        TweenLite.set(leaf, {
          fill: ['#008000', '#228b22', '#7cfc00', '#32cd32'][i % 4],
          x: point.x,
          y: point.y,
          scale: 1,
          rotation: deg + (i % 2 == 0 ? 90 : -90),
          attr: {
            d: "M0,0 Q5,-5 10,0 5,5 0,0z"
          }
        })
      }
    }

    var leaves = g.querySelectorAll('path')
    tl.staggerFromTo(leaves, 10, {
      scale: 0
    }, {
      scale: 1
    }, 6 / leaves.length, 'start+=0.5')
    TweenMax.fromTo(leaves, 1, {
      rotation: "-=5",
      ease: Power1.easeInOut
    }, {
      rotation: "+=5",
      ease: Power1.easeInOut
    }).repeat(-1).yoyo(true)
  })

  tl.fromTo(spirals, 6, {
    strokeDashoffset: spirals[0].getTotalLength(),
    opacity: 0,
    ease: Linear.easeNone
  }, {
    strokeDashoffset: 0,
    opacity: 1,
    ease: Linear.easeNone
  }, 'start')

  var flowerGroups = document.querySelectorAll('[id^="flowers"]');
  var flowerTweens = [];
  flowerGroups.forEach(function(flowersGroup) {
    var flowers = flowersGroup.querySelectorAll('[id^="flower"]')
    flowers.forEach(function(flower) {
      TweenLite.set(flower, {
        transformOrigin: "50% 50%"
      })
    })
    tl.staggerFromTo(flowers, 5, {
      scale: 0
    }, {
      scale: 0.7,
      ease: Back.easeOut
    }, 0.8, 'start+=1')
  })

  animateSun()
}

function animateSun() {
  var sun = document.querySelector('#sun')
  TweenLite.set(sun, {
    height: 'auto',
    visibility: 'visible',
    transformOrigin: '100% 0'
  })
  var suntl = new TimelineMax({
    repeat: -1,
    yoyo: true
  })
  var ray1 = document.querySelector('#ray1')
  var ray2 = document.querySelector('#ray2')

  // Looping ray animation
  TweenLite.set([ray1, ray2], {
    transformOrigin: "50% 50%"
  })
  let out = {
    scale: 1,
    opacity: 0.5,
    ease: Power1.easeInOut
  }
  let inn = {
    scale: 0.8,
    opacity: 1,
    ease: Power1.easeInOut
  }
  suntl.fromTo(ray1, 1, out, inn)
  suntl.fromTo(ray2, 1, inn, out, "-=1")
  TweenMax.to(ray1, 2, {
    rotation: 18,
    ease: Linear.easeNone
  }).repeat(-1)

  // Scaling
  tl.fromTo(sun, 10, {
    scale: 0,
    ease: Power1.easeIn
  }, {
    scale: 1,
    ease: Power1.easeOut
  }, "start")
}

function start() {
  // tl.seek(7)
  tl.timeScale(1)
  tl.play()
}

function stop() {
  tl.timeScale(3)
  tl.reverse()
}