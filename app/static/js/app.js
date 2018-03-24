var joystick = nipplejs.create({
    zone: document.getElementById('static'),
    mode: 'static',
    position: {left: '50%', top: '50%'},
    color: 'red'
});

joystick.on('move', function (event, data) {
    radius = data.force
    angle = data.angle.radian

    form_data = {
        "angle": angle,
        "radius": radius
    }

    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/ride', true);
    xhr.setRequestHeader("Content-type", "application/json");
    form_data = JSON.stringify(form_data)
    xhr.send(form_data);
})

setTimeout(function() {
    var camera_image = document.getElementById('camera')
    camera_image.src = '/camera'
}, 1000)

